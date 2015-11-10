#include "Error.h"
#include <iostream>
#include <cstdlib>

using namespace std;

void Exit_Failure(const char* message) {
	cerr << message << endl;
	exit(EXIT_FAILURE);
}