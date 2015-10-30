#include "Sequence.h"
#include <fstream>

using namespace std;

Seq::Seq() {
	seq_name = "";
	sequence = "";
	length = 0;
	has_data = false;
}

Seq::Seq(string seq_name, string sequence) {
	this.seq_name = seq_name;
	this.sequence = sequence;
	length = sequence.length();

	available = (length > 0) ? true : false;
}

Seq::~Seq() {
	seq_name.clear();
	sequence.clear();
	length = 0;
	available = false;
}

bool Seq::is_available() {
	return available;
}

string Seq::getName() {
	return seq_name;
}

string Seq::getSequence() {
	return sequence;
}

string Seq::getLength() {
	return length;
}

void Seq::addSequence(std::string seq) {
	sequence += seq;
	length += seq.length();

	if (!available && length > 0)
		available = true;
}

std::string Seq::getSubSeq(int pos) {
	if (available && pos < length)
		return sequence.substr(pos);

	return NULL;
}

std::string Seq::getSubSeq(int pos, int length) {
	if (available && pos + length < this.length)
		return sequence.substr(pos, length);

	return NULL;
}

SeqList::SeqList() {
	count = 0;
	available = false;
}

SeqList::~SeqList() {
	seq_list.clear();
	count = 0;
	available = false;
}

void SeqList::addSeq(Seq seq) {
	if (Seq.is_available()) {
		seq_list.push_back(seq);
		count++;

		if (!available && count > 0)
			available = true;
	}
}

Seq SeqList::getSeq(int pos) {
	if (available && pos < count) {
		return seq_list[pos];
	}

	return NULL;
}

Seq SeqList::getSeq(std::string seq_name) {
	if (available) {
		for (vector<Seq>::iterator it = seq_list.begin(); 
			it != seq_list.end(); ++it) {
			if (seq_name.compare(it->getName()) == 0) {
				return *it;
			}
		}

		return NULL;
	}

	return NULL;
}

void readSeqsFromFile(const char* file_name) {
	ifstream fasta;
	string line;
	Seq seq;

	fasta.open(file_name, ifstream::in);

	while (!fasta.eof()) {
		fasta >> line;

		if (line[0] == '>') {
			if (seq.is_available()) {
				this.addSeq(seq);
			}
			seq = new Seq(line.substr(1), "");
		} else {
			seq.addSequence(line);
		}
	}
	
	if (seq.is_available()) {
		this.addSeq(seq);
	}

	fasta.close();
}