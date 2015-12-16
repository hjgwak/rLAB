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

	opts.parseOptions(options, "Kmer");
	opts.help("Kmer");

	//get input sequences from file (fasta)
	if (!opts.quiet())
		cerr << "get input sequence from file (fasta)" << endl;
	SeqList input_seq;
	input_seq.readSeqsFromFile(opts.input());

	//make k-mer hash_table of input sequence
	if (!opts.quiet())
		cerr << "make k-mer hash_table of input sequence" << endl;
	SeqHash* input_hash = new SeqHash();

	for (int i = 0; i < input_seq.getCount(); ++i) {
		Seq* data_seq = input_seq.getSeq(i);
		input_hash->setName(data_seq->getName());

		for (int j = 0; j <= data_seq->getLength() - opts.k(); ++j) {
			input_hash->addSeq(data_seq->getSubSeq(j, opts.k()), j);
		}
	}

	//get db sequence(s) from file (fasta)
	if (!opts.quiet())
		cerr << "get db sequence(s) from file (fasta)" << endl;
	SeqList db_seq;
	db_seq.readSeqsFromFile(opts.db());

	//make k-mer hash_table of sequence(s)
	if (!opts.quiet())
		cerr << "make k-mer hash_table of db" << endl;
	SeqHash* db_hash;
	SeqHashList db_hash_list;
	if (opts.prog().compare("common") == 0) {
		//if set each option, make hash for each sequences
		db_hash = new SeqHash[db_seq.getCount()];
	} else {
		db_hash = new SeqHash();
	}

	for (int i = 0; i < db_seq.getCount(); ++i) {
		Seq* data_seq = db_seq.getSeq(i);
		if (opts.prog().compare("common") == 0)
			db_hash[i].setName(data_seq->getName());
		else
			db_hash->setName(data_seq->getName());

		for (int j = 0; j <= data_seq->getLength() - opts.k(); ++j) {
			if (opts.prog().compare("common") == 0)
				db_hash[i].addSeq(data_seq->getSubSeq(j, opts.k()), j);
			else
				db_hash->addSeq(data_seq->getSubSeq(j, opts.k()), j);
		}
	}

	if (opts.prog().compare("common") == 0) {
		for (int i = 0; i < db_seq.getCount(); ++i) {
			db_hash_list.addSeqHash(&db_hash[i]);
		}
	}

	vector<string> keys = input_hash->getKeys();
	if (opts.prog().compare("unique") == 0) {
		if (!opts.quiet())
			cerr << "remove not unique k-mer in genome" << endl;
		for (vector<string>::iterator it = keys.begin(); it != keys.end(); ++it) {
			if (db_hash->isSeqExist(*it)) {
				input_hash->rmSeq(*it);
			}
		}
	} else if (opts.prog().compare("common") == 0) {
		if (!opts.quiet())
			cerr << "remove not common k-mer in genome" << endl;
		for (vector<string>::iterator it = keys.begin(); it != keys.end(); ++it) {
			double count = 0.0;
			for (int i = 0; i < db_hash_list.getCount(); ++i) {
				count += db_hash_list.getSeqHash(i)->isSeqExist(*it) ? 1.0 : 0.0;
			}
			bool common = (count / db_hash_list.getCount()) >= opts.threshold_common() ? true : false;
			if (!common) {
				input_hash->rmSeq(*it);
			}
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
	output_f << input_hash->getName() << "." << opts.prog() << endl;
	input_hash->printHash(output_f);

	output_f.close();

	delete input_hash;
	if (opts.prog().compare("common") == 0) {
		delete[] db_hash;
	} else {
		delete db_hash;
	}

	return 0;
}