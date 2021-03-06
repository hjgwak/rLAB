#ifndef __Sequence_H__
#define __Sequence_H__

#include <vector>
#include <string>

class Seq {
	public:
		Seq();
		Seq(std::string seq_name, std::string sequence);
		~Seq();

		bool is_available();
		std::string getName();
		std::string getSequence();
		int getLength();

		void readSeqFromFile(std::string file_name);
		void addSequence(std::string seq);

		std::string getSubSeq(int pos);
		std::string getSubSeq(int pos, int length);

	private:
		std::string seq_name;
		std::string sequence;
		int length;
		bool available;
};

class SeqList {
	public:
		SeqList();
		~SeqList() {};

		void addSeq(Seq* seq);
		Seq* getSeq(int pos);
		Seq* getSeq(std::string seq_name);

		bool is_available();
		int getCount();

		void readSeqsFromFile(std::string file_name);

	private:
		std::vector<Seq*> seq_list;
		int count;
		bool available;
};

#endif //__Sequence_H__
