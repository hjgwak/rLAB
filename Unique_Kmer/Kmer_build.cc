#include "Error.h"
#include "Options.h"
#include "SeqHash.h"
#include "Sequence.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
	vector<string> options (argv, argv+argc);
	Options opts;

	opts.parseOptions(options, "build");
	opts.help("build");

	//get sequence(s) from file (fasta)
	if (!opts.quiet())
		cerr << "get sequence(s) from file (fasta)" << endl;
	SeqList sequence;
	sequence.readSeqsFromFile(opts.input());

	//make k-mer hash_table of sequence
	if (!opts.quiet())
		cerr << "make k-mer hash_table of db" << endl;
	SeqHash* sequence_hash;
	if (opts.each()) {
		//if set each option, make hash for each sequences
		sequence_hash = new SeqHash[sequence.getCount()];
	} else {
		sequence_hash = new SeqHash();
	}

	for (int i = 0; i < sequence.getCount(); ++i) {
		Seq* data_seq = sequence.getSeq(i);
		if (opts.each())
			sequence_hash[i].setName(data_seq->getName());
		else
			sequence_hash->setName(data_seq->getName());
		for (int j = 0; j < data_seq->getLength() - opts.k(); ++j) {
			if (opts.each())
				sequence_hash[i].addSeq(data_seq->getSubSeq(j, opts.k()), j);
			else
				sequence_hash->addSeq(data_seq->getSubSeq(j, opts.k()), j);
		}
	}

	//open output file
	ofstream output_f;

	output_f.open(opts.output().c_str(), ofstream::out);
	if(!output_f.is_open()) {
		Exit_Failure("ERROR : Output file open error!");
	}

	//report unique sub_seqs and positions
	if (!opts.quiet())
		cerr << "report unique sub_seqs and positions" << endl;

	if (opts.each()) {
		for (int i = 0; i < sequence.getCount(); ++i) {
			cout << "#" << sequence_hash[i].getName() << endl;
			sequence_hash[i].printHash(output_f);
		}
	} else {
		cout << "#" << sequence_hash->getName() << endl;
		sequence_hash->printHash(output_f);
	}

	output_f.close();

	return 0;
}