#pragma once

#include <Adafruit_VCNL4040.h>
#include "esphome.h"
#include <Wire.h>


namespace esphome {
namespace codecell {

class CodeCellSensor : public PollingComponent, public Sensor {

public:

CodeCellSensor() : PollingComponent(1000) {}

float get_setup_priority() const override;

void setup() override;

void update() override;

};

} // ns codecell
} // ns esphome
