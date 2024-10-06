#include codecell.h


Adafruit_VCNL4040 vcnl4040 = Adafruit_VCNL4040();


float CodeCellSensor::get_setup_priority() { return esphome::setup_priority::BUS; }

void CodeCellSensor::setup() {
    if (!vcnl4040.begin()) {
        while (1);
    }
}

void CodeCellSensor::update() {
    int raw = vcnl4040.getWhiteLight();
    this->publish_state(raw);
}
