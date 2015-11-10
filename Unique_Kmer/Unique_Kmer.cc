#include "Sequence.h"
#include "SeqHash.h"
#include "Options.h"
#include "Error.h"
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]) {
	vector<string> options (argv, argv+argc);
	Options opts;

	opts.parseOptions(options);
	opts.help();

	//for output
	ofstream output_f;

	output_f.open(opts.output().c_str(), ofstream::out);
	if(!output_f.is_open()) {
		Exit_Failure("ERROR : Output file open error!");
	}

	//get genome sequence from input file
	cerr << "get genome sequence from input file" << endl;
	Seq genome;
	genome.readSeqFromFile(opts.input());

	//make k-mer hash_table of genome
	cerr << "make k-mer hash_table of genome" << endl;
	SeqHash genome_hash; 
	for (int i = 0; i < genome.getLength() - opts.k(); ++i) {
		genome_hash.addSeq(genome.getSubSeq(i, opts.k()), i);
	}

	//get database sequences from db file (multi fasta)
	cerr << "get database sequences from db file (multi fasta)" << endl;
	SeqList database;
	database.readSeqsFromFile(opts.db());

	//make k-mer hash_table of db
	cerr << "make k-mer hash_table of db" << endl;
	SeqHash database_hash;
	for (int i = 0; i < database.getCount(); ++i) {
		Seq* data_seq = database.getSeq(i);
		for (int j = 0; j < data_seq->getLength() - opts.k(); ++j) {
			database_hash.addSeq(data_seq->getSubSeq(j, opts.k()), j);
		}
	}

	//remove not unique k-mer in genome
	cerr << "remove not unique k-mer in genome" << endl;
	vector<string> keys = genome_hash.getKeys();

	for (vector<string>::iterator it = keys.begin(); it != keys.end(); ++it) {
		if (database_hash.isSeqExist(*it)) {
			genome_hash.rmSeq(*it);
		}
	}

	//report unique sub_seqs and positions
	cerr << "report unique sub_seqs and positions" << endl;
	keys = genome_hash.getKeys();
	pair<string, vector<int> > elem;
	for (vector<string>::iterator it = keys.begin(); it != keys.end(); ++it) {
		elem = genome_hash.getSeq(*it);
		output_f << elem.first;
		for (vector<int>::iterator it_2 = elem.second.begin(); it_2 != elem.second.end(); ++it_2) {
			output_f << " " << *it_2;
		}
		output_f << endl;
	}

	output_f.close();

	return 0;
}
