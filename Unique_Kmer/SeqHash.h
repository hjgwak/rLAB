#ifndef __SEQHASH_H__
#define __SEQHASH_H__

#include <map>
#include <string>
#include <vector>
#include <utility>
#include <fstream>
#include <iostream>

class SeqHash {
	public:
		SeqHash();
		~SeqHash();

		bool is_available();
		int getSize();
		std::string getName();

		void readHashFromFile(std::string file_name);
		void printHash(std::ostream& output);

		void setName(std::string name);
		void addSeq(std::string seq, int pos);
		void rmSeq(std::string seq);
		std::pair<std::string, std::vector<int> > getSeq(std::string name);
		bool isSeqExist(std::string seq);

		std::vector<std::string> getKeys();

	private:
		std::string name;
		std::map<std::string, std::vector<int> > hash_map;
		int size;
		bool available;
};

class SeqHashList {
	public:
		SeqHashList();
		~SeqHashList() {};

		void addSeqHash(SeqHash* seq_hash);
		SeqHash* getSeqHash(int pos);
		SeqHash* getSeqHash(std::string hash_name);

		bool is_available();
		int getCount();

		void readHashsFromFile(std::string file_name);

	private:
		std::vector<SeqHash*> hash_list;
		int count;
		bool available;
};

#endif //__SEQHASH_H__
