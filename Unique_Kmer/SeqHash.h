#ifndef __SEQHASH_H__
#define __SEQHASH_H__

#include <map>
#include <string>
#include <vector>
#include <utility>

class SeqHash {
	public:
		SeqHash();
		~SeqHash();

		bool is_available();
		int getSize();

		void addSeq(std::string seq, int pos);
		void rmSeq(std::string seq);
		std::pair<std::string, std::vector<int> > getSeq(std::string name);
		bool isSeqExist(std::string seq);

		vector<std::string> getKeys();

	private:
		std::map<std::string, std::vector<int> > hash_map;
		int size;
		bool available;
};

#endif //__SEQHASH_H__