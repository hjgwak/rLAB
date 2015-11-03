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