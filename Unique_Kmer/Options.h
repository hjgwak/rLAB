#ifndef __OPTIONS_H__
#define __OPTIONS_H__

#include <string>
#include <vector>

class Options {
	public:
		Options();
		Options(std::vector<std::string> argv, std::string program);

		void parseOptions(std::vector<std::string> argv, std::string program);
		void help(std::string program);
		bool quiet();
		bool each();
		int k();
		double threshold_common();
		std::string input();
		std::string output();
		std::string db();

	private:
		bool _quiet;
		bool _help;
		bool _each;
		int _k;
		double _threshold_common;
		std::string _input;
		std::string _output;
		std::string _db;
};

#endif //__OPTIONS_H__