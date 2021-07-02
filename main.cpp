#include <iostream>
#include <string>
#include "IODev.h"
#include "structures.h"
#include "errors.h"
#include <unistd.h>

using namespace std;

//Change to show what job process went wrong! (Maybe Job Queue sys)
void ERROR(string step, ERROR_TYPE errorcode){ 
    cout << "\033[1;31mERROR\033[0m " << step  << " did not complete." << endl << endl 
    <<  "Termination type: " << errorcode.name << 
    " (Error #" << errorcode.code << ")" << endl;

}

void SUCCESSFULSTART(){
    cout << "\033[1;32mcomplete\033[0m\n";
}

int main(){

    /*for now I will just define the input channels as boolean, later in maybe a seperate branch 
    I will add the wiringpi lib to actually interface with the GPIO */

    IO_Device Start; //0000
    IO_Device Stop; //0001
    IO_Device Crossover; //0002
    IO_Device Auto; //0003
    IO_Device On_Reset; //0004
    IO_Device Manual; //0005
    IO_Device Vent; //0006
    IO_Device Rough_S2; //0007
    IO_Device HI_VAC_Valve; //0008
    IO_Device Cryo_Rough; //0009
    IO_Device Cryo_Purge; //0010
    IO_Device Vacuum_In; //0011
    IO_Device Rough_SW; //0012
    IO_Device Water_Lock; //0013
    IO_Device Vent_Auto; //0014
    //0015 not set! potential GPIO we could use!
    IO_Device OUT1; //0501
    IO_Device OUT2; //0502
    IO_Device OUT3; //0503
    IO_Device OUT4; //0504
    IO_Device OUT5; //0505
    IO_Device OUT6; //0506
    IO_Device OUT7; //0507
    IO_Device OUT8; //0508
    IO_Device OUT9; //0509

    //Initializtion
    cout  << "Initializing" << endl;
    On_Reset.device_init(false, "On_Reset", "input");
    Manual.device_init(false, "Manual", "input");
    Rough_SW.device_init(false, "Rough_SW", "input"); 
    OUT1.device_init(false, "OUT1", "output");
    OUT2.device_init(false, "OUT2", "output");
    OUT3.device_init(false, "OUT3", "output");
    OUT4.device_init(false, "OUT4", "output");
    OUT5.device_init(false, "OUT5", "output");
    OUT6.device_init(false, "OUT6", "output");
    OUT7.device_init(false, "OUT7", "output");
    OUT8.device_init(false, "OUT8", "output");
    OUT9.device_init(false, "OUT9", "output");

    //would be done by reading GPIO ports
    On_Reset.setHigh();
    Manual.setHigh();

    cout << "Start up"<< endl;

    //system in manual mode
    cout << endl << "Putting system in Manual mode..." << endl;
    if(Manual.status(false) || On_Reset.status(false)){
        OUT1.setHigh();
        OUT1.status(true);
        SUCCESSFULSTART();
    }
    else{
        ERROR("Manual mode", ERROR1);
    }

    //for  test
    cout << endl;
    //Rough_SW.setHigh();


    //starting mechanical pump


cout  << endl << "Starting mechanical pump..." << endl;
if(OUT1.status(false) && Rough_SW.status(false)){
    OUT9.setHigh();
    OUT9.status(true);
    SUCCESSFULSTART();
}
else{
    ERROR("Mechanical pump", ERROR2);
}

    return 0;
}