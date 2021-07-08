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
    //I
    Start.device_init(false, "Start", "input"); 
    Stop.device_init(false, "Stop", "input"); 
    Crossover.device_init(false, "Crossover", "input");  
    Auto.device_init(false, "Auto", "input"); 
    On_Reset.device_init(false, "On_Reset", "input"); 
    Manual.device_init(false, "Manual", "input");
    Vent.device_init(false,"Vent","input"); 
    Rough_S2.device_init(false, "Rough_S2", "input");
    HI_VAC_Valve.device_init(false,"High vacuum valve", "input");
    Cryo_Rough.device_init(false,"Cryo rough", "input");
    Cryo_Purge.device_init(false,"Cryo purge", "input");
    Vacuum_In.device_init(false, "Vacuum_In", "input");  
    Rough_SW.device_init(false,"Rough_SW", "input");
    Water_Lock.device_init(false, "Water_Lock", "input"); 
    Vent_Auto.device_init(false, "Vent_Auto", "input"); 
    //O
    OUT1.device_init(false, "OUT1", "output");
    OUT2.device_init(false, "OUT2", "output");
    OUT3.device_init(false, "OUT3", "output");
    OUT4.device_init(false, "OUT4", "output");
    OUT5.device_init(false, "OUT5", "output");
    OUT6.device_init(false, "OUT6", "output");
    OUT7.device_init(false, "OUT7", "output");
    OUT8.device_init(false, "OUT8", "output");
    OUT9.device_init(false, "OUT9", "output");
    SUCCESSFULSTART();

    //would be done by reading GPIO ports
    On_Reset.setHigh();
    Manual.setHigh();
    Rough_SW.setHigh();

    cout << "Start up"<< endl;

    //system in manual mode
    cout << endl << "Putting system in Manual mode..." << endl;
    if(Manual.status(1) || On_Reset.status(1)){
        OUT1.setHigh();
        OUT1.status(true);
        SUCCESSFULSTART();
    }
    else{
        ERROR("Manual mode", ERROR1);
    }


    //starting mechanical pump
    cout  << endl << "Starting mechanical pump..." << endl;
    if(OUT1.status(1) && Rough_SW.status(1)){
        OUT9.setHigh();
        OUT9.status(true);
        SUCCESSFULSTART();
    }
    else{
        ERROR("Mechanical pump", ERROR2);
    }

    //Rough system
    cout << endl << "Starting rough system" << endl;
    if(OUT9.status(1) && !HI_VAC_Valve.status(1) && !Vent.status(1) &&
    Rough_S2.status(1) && !Cryo_Rough.status(1) && !Cryo_Purge.status(1)){
        OUT3.setHigh();
    }
    else{
        ERROR("Rough system",ERROR3);
    }

    //Cryo-rough
    cout << endl << "Starting cryo-rough" << endl;
    if(OUT9.status(1) && !HI_VAC_Valve.status(1) && !Rough_S2.status(1) 
    && !Vent.status(1) && Cryo_Rough.status(1)){
        OUT5.setHigh();
    }
    else{
        ERROR("Cryo-rough",ERROR4);
    }


    //Open sys to cyropump
    cout << endl << "Opening system to cryo-pump" << endl;
    if(Crossover.status(1) && Vacuum_In.status(1) && !Rough_S2.status(1) && !Vent.status(1)
    && HI_VAC_Valve.status(1)){
        OUT7.setHigh();
    }
    else{
        ERROR("Opening system to cryo-pump",ERROR5);
    }

    //Water lock
    cout << endl << "Starting water lock" << endl;
    if((Vacuum_In.status(1) || OUT7.status(1)) && !Vent.status(1) && Water_Lock.status(1)){
        OUT8.setHigh();
    }
    else{
        ERROR("Water lock start up",ERROR6);
    } 

    return 0;
}