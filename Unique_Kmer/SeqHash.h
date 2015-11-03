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

		int getSize();
		bool is_available();

		void addSeq(std::string seq, int pos);
		std::pair<std::string, std::vector<int> > getSeq(std::string name);
		bool isSeqExist(std::string seq);

	private:
		std::map<std::string, std::vector<int> > hash_map;
		int size;
		bool available;
};

#endif //__SEQHASH_H__