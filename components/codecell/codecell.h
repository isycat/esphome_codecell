#include "Adafruit_VCNL4040.h"
#include "esphome.h"
#include "Wire.h"

Adafruit_VCNL4040 vcnl4040 = Adafruit_VCNL4040();

namespace esphome {
namespace codecell {

class CodeCellSensor : public PollingComponent, public Sensor {

public:

CodeCellSensor() : PollingComponent(1000) {}

float get_setup_priority() const override { return esphome::setup_priority::BUS; }

void setup() override {
    if (!vcnl4040.begin()) {
        while (1);
    }
}

void update() override {
    int raw = vcnl4040.getWhiteLight();
    this->publish_state(raw);
}

};

} // ns codecell
} // ns esphome
