#include "Options.h"
#include "Error.h"
#include <iostream>

using namespace std;

static void printUSAGE(string program) {
	cout << "\n############################################################\n" << endl;
	cout << "Kmer_unique [Options]\n" << endl;
	cout << "Options\n" << endl;
	cout << "\t-i\tinput filename in hl format, required" << endl;
	cout << "\t-o\toutput filename, required" << endl;
	if (program.compare("build") == 0) {
		cout << "\t-k\twindow size for split, required" << endl;
		cout << "\t-e\tmake hash list for each sequence" << endl;
	}
	if (program.compare("unique") == 0 || program.compare("common") == 0)
		cout << "\t-db\tdirectory which has sequences for compare between input file, required" << endl;
	cout << "\t-q\tquiet, if set this option, do not print any error msg" << endl;
	cout << "\nOuput" << endl;
	cout << "\t(output filename).hl" << endl;
	cout << "\t#(seq name)" << endl;
	cout << "\tkmer\tposition" << endl;
	cout << endl;
}

Options::Options() {
	_help = false;
	_each = false;
	_quiet = false;
	_k = 0;
	_input = "";
	_output = "";
	_db = "";
}

Options::Options(vector<string> argv, string program) {
	this->parseOptions(argv, program);
}

void Options::parseOptions(vector<string> argv, string program) {
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
		} else if (argv[i] == "-e") {
			_each = true;
		} else if (argv[i] == "-q") {
			_quiet = true;
		}
	}

	if (!_help && (program.compare("unique") == 0 || 
		program.compare("common") == 0) &&
		!(r_i && r_o && r_db)) {
		Exit_Failure("ERROR : Lack of required option!");
	} else if (!_help && (program.compare("build") == 0) &&
		!(r_i && r_o && r_k)) {
		Exit_Failure("ERROR : Lack of required option!");
	}
}

void Options::help(string program) {
	if(_help) {
		printUSAGE(program);
		exit(0);
	}
}

bool Options::quiet() {
	return _quiet;
}

bool Options::each() {
	return _each;
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