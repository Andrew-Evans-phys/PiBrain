#ifndef ERRORS
#define ERRORS
#include <string>
#include "structures.h"

ERROR_TYPE ERROR1 = {"Manual Startup failure", "The process did not meet the specified condition", 0001};
ERROR_TYPE ERROR2 = {"Mechanical pump failure", "The process did not meet the specified condition", 0002};
ERROR_TYPE ERROR3 = {"Mechanical pump failure", "Quiting process after too maanyt failed attempts", 0003};


#endif

