#include "Options.h"
#include <cstdlib>
#include <iostream>

using namespace std;

static void printUSAGE() {
	cout << "\n############################################################\n" << endl;
	cout << "Unique_kmer [Options]\n" << endl;
	cout << "Options\n" << endl;
	cout << "\t-i\tinput filename in fasta format, required" << endl;
	cout << "\t-o\toutput filename, required" << endl;
	cout << "\t-k\twindow size for split, required" << endl;
	cout << "\t-db\tdirectory which has sequences for compare between input file, required" << endl;
	cout << endl;
}

Options::Options() {
	_help = false;
	_k = 0;
	_input = "";
	_output = "";
	_db = "";
}

void Options::parseOptions(vector<string> argv) {
	bool r_k = false, r_i = false, r_o = false, r_db = false;

	for(int i = 0; i < argv.size(); ++i) {
		if (argv[i] == "-h" || argv[i] == "-help") {
			_help = true;
		} else if (argv[i] == "-k") {
			_k = atoi(argv[i+1].c_str());
			r_k = true;
		} else if (argv[i] == "-i") {
			_input = argv[i+1];
			r_i = true;
		} else if (argv[i] == "-o") {
			_output = argv[i+1];
			r_o = true;
		} else if (argv[i] == "-db") {
			_db = argv[i+1];
			r_db = true;
		}
	}

	if (!_help && !(r_k && r_i && r_o && r_db)) {
		cout << "ERROR : Lack of required option!" << endl;
		exit(EXIT_FAILURE);
	}
}

void Options::help() {
	if(_help) {
		printUSAGE();
		exit(0);
	}
}

int Options::k() {
	return _k;
}

string Options::input() {
	return _input;
}

string Options::output() {
	return _output;
}

string Options::db() {
	return _db;
}