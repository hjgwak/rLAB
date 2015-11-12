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

	opts.parseOptions(options, "unique");
	opts.help("unique");

	
	//get genome sequence_hash from input file
	if (!opts.quiet())
		cerr << "get genome sequence_hash from input file" << endl;
	SeqHash genome;
	genome.readHashFromFile(opts.input());

	//get database sequences_hash from db file
	if (!opts.quiet())
		cerr << "get database sequences_hash from db file" << endl;
	SeqHash database;
	database.readHashFromFile(opts.db());

	//remove not unique k-mer in genome
	if (!opts.quiet())
		cerr << "remove not unique k-mer in genome" << endl;
	vector<string> keys = genome.getKeys();

	for (vector<string>::iterator it = keys.begin(); it != keys.end(); ++it) {
		if (database.isSeqExist(*it)) {
			genome.rmSeq(*it);
		}
	}

	//open output fi;e
	ofstream output_f;

	output_f.open(opts.output().c_str(), ofstream::out);
	if(!output_f.is_open()) {
		Exit_Failure("ERROR : Output file open error!");
	}

	//report unique sub_seqs and positions
	if (!opts.quiet())
		cerr << "report unique sub_seqs and positions" << endl;
	genome.printHash(output_f);

	output_f.close();

	return 0;
}
