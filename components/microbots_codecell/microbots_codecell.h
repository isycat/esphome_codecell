#include <CodeCell.h>
#include "esphome.h"

CodeCell singleCodeCell;

namespace esphome {
namespace microbots_codecell {

class CodeCellSensor : public PollingComponent, public Sensor {

public:

CodeCellSensor() : PollingComponent(1000) {}

float get_setup_priority() const override { return esphome::setup_priority::BUS; }

void setup() override {
    singleCodeCell.Init(LIGHT);
}

void update() override {
    uint16_t brightness = (CodeCellSensor.Light_WhiteRead()) >> 3; 
    this->publish_state(brightness);
}

};

} // ns microbots_codecell
} // ns esphome
