#include "SeqHash.h"
#include "Error.h"

using namespace std;

SeqHash::SeqHash() {
	name = "";
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

string SeqHash::getName() {
	return name;
}

static void Tokenize(const string& str, 
	vector<string>& tokens, const string& delimiters = " ") {
	string::size_type lastPos = str.find_first_not_of(delimiters, 0);
	string::size_type pos = str.find_first_of(delimiters, lastPos);

	while (string::npos != pos || string::npos != lastPos) {
		tokens.push_back(str.substr(lastPos, pos - lastPos));
		lastPos = str.find_first_not_of(delimiters, pos);
		pos = str.find_first_of(delimiters, lastPos);
	}
}

void SeqHash::readHashFromFile(string file_name) {
	ifstream hl_f;
	string line;
	string name;
	bool singleton = true;

	hl_f.open(file_name.c_str(), ifstream::in);

	getline(hl_f, name);
	if (name[0] == '#') {
		this->name = name;
	} else {
		Exit_Failure("ERROR : Hash name missing");
	}

	while(!hl_f.eof()) {
		getline(hl_f, line);
		if (line.empty()) break;
		if (line[0] == '#') {
			hl_f.close();
			Exit_Failure("ERROR : input file is not single hash");
		} else {
			vector<string> tokens;
			Tokenize(line, tokens, " ");
			vector<int> positions;
			for (int i = 1; i < tokens.size(); ++i)
				positions.push_back(stoi(tokens[i]));
			hash_map[tokens[0]] = positions;
		}
		line.clear();
	}
	hl_f.close();
}

void SeqHash::printHash(ostream& output) {
	vector<string> keys = this->getKeys();
	pair<string, vector<int> > elem;
	for (vector<string>::iterator it = keys.begin(); it != keys.end(); ++it) {
		elem = this->getSeq(*it);
		output << elem.first;
		for (vector<int>::iterator it_2 = elem.second.begin(); it_2 != elem.second.end(); ++it_2) {
			output << " " << *it_2;
		}
		output << endl;
	}
}

void SeqHash::setName(string name) {
	this->name = name;
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

SeqHashList::SeqHashList() {
	count = 0;
	available = false;
}
/*
SeqHashList::~SeqHashList() {
	for (vector<SeqHash*>::iterator it = hash_list.begin();
		it != hash_list.end(); ++it) {
		delete *it;
	}
	hash_list.clear();
	count = 0;
	available = false;
}
*/
void SeqHashList::addSeqHash(SeqHash* seq_hash) {
	if (seq_hash->is_available()) {
		hash_list.push_back(seq_hash);
		count++;

		if (!available && count > 0)
			available = true;
	}
}

SeqHash* SeqHashList::getSeqHash(int pos) {
	if (available && pos < count) {
		return hash_list[pos];
	}

	return NULL;
}

SeqHash* SeqHashList::getSeqHash(std::string hash_name) {
	if (available) {
		for (vector<SeqHash*>::iterator it = hash_list.begin();
			it != hash_list.end(); ++it) {
			if (hash_name.compare((*it)->getName()) == 0) {
				return *it;
			}
		}

		return NULL;
	}

	return NULL;
}

bool SeqHashList::is_available() {
	return available;
}

int SeqHashList::getCount() {
	return count;
}

void SeqHashList::readHashsFromFile(std::string file_name) {
	ifstream hl_f;
	string line;
	SeqHash* hash = NULL;

	hl_f.open(file_name.c_str(), ifstream::in);

	while(!hl_f.eof()) {
		getline(hl_f, line);

		if (line[0] == '#') {
			if (hash && hash->is_available()) {
				this->addSeqHash(hash);
			}
			hash = new SeqHash();
			hash->setName(line.substr(1));
		} else {
			vector<string> tokens;
			Tokenize(line, tokens, " ");
			for (int i = 1; i < tokens.size(); ++i)
				hash->addSeq(tokens[0], stoi(tokens[i]));		}
		line.clear();
	}

	if (hash->is_available()) {
		this->addSeqHash(hash);
	}

	hl_f.close();
}
