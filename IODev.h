#ifndef IODev
#define IODev
#include <string>

class IO_Device{
    public:
    bool status(bool print_statement);
    void device_init(bool default_on, std::string set_name, std::string set_type);
    // will actually contain the GPIO interface later
    void setHigh();

    private:
        bool on, NO; //NO means normally open
        std::string name, type;
        
};
    


#endif

