#include "SeqHash.h"

using namespace std;

SeqHash::SeqHash() {
	hash_map.clear();
	size = 0;
	available = true;
}

SeqHash::~SeqHash() {
	hash_map.clear();
	size = 0;
	available = false;
}

bool SeqHash::is_available() {
	return available;
}

int SeqHash::getSize() {
	return size;
}

void SeqHash::addSeq(string seq, int pos) {
	if (!seq.empty()) {
		hash_map[seq].push_back(pos);
	}
}

void SeqHash::rmSeq(string seq) {
	if (this->isSeqExist(seq)) {
		hash_map.erase(seq);
	}
}

pair<string, vector<int> > SeqHash::getSeq(string name) {
	vector<int> empty;

	if (this->isSeqExist(name)) {
		return make_pair(name, hash_map[name]);
	}

	return make_pair("", empty);
}

bool SeqHash::isSeqExist(string seq) {
	map<string, vector<int> >::iterator it;

	it = hash_map.find(seq);

	return (it != hash_map.end()) ? true : false;
}

vector<string> SeqHash::getKeys() {
	vector<string> keys;
	map<string, vector<int> >::iterator it;
	for (it = hash_map.begin(); it != hash_map.end(); ++it) {
		keys.push_back(it->first);
	}

	return keys;
}