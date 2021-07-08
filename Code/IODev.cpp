#include <iostream>
#include <string>
#include "IODev.h"


using namespace std;

void IO_Device::device_init(bool default_on, string set_name, string set_type){
    on = default_on;
    name = set_name;
    type = set_type;
}


bool IO_Device::status(bool print_statement){
    if(print_statement){
        if(on){
            cout  << name << " is true" << endl;
            return true;
        }
        else{
            cout  << name << " is false" << endl;
            return false;
        }
    }
    else{
        if(on){
            return true;
        }
        else{
            return false;
        }       
    }

}

// will actually contain the GPIO interface later
void IO_Device::setHigh(){
    on = true;
    cout << name << " is set high" << endl;
}

void IO_Device::setLow(){
    on = false;
    cout << name << " is set low" << endl;
}