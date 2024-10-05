#include <CodeCell.h>
#include "esphome.h"

CodeCell singleCodeCell;

using namespace esphome;

class MyCodeCell : public PollingComponent, public Sensor {

public:

Sensor *rawLight_sensor = new Sensor();

MyCodeCell() : PollingComponent(1000) {}

float get_setup_priority() const override { return esphome::setup_priority::BUS; }

void setup() override {
    singleCodeCell.Init(LIGHT);
}

void update() override {
    uint16_t brightness = (myCodeCell.Light_WhiteRead()) >> 3; 
    rawLight_sensor->publish_state(brightness);
}

};
