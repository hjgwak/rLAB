#ifndef __OPTIONS_H__
#define __OPTIONS_H__

#include <string>
#include <vector>

class Options {
	public:
		Options();

		void parseOptions(std::vector<std::string> argv);
		void help();
		int k();
		std::string input();
		std::string output();
		std::string db();

	private:
		bool _help;
		int _k;
		std::string _input;
		std::string _output;
		std::string _db;
};

#endif //__OPTIONS_H__