#pragma once

#include <Adafruit_VCNL4040.h>
#include "esphome.h"
#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

Adafruit_VCNL4040 vcnl4040 = Adafruit_VCNL4040();

namespace esphome {
namespace codecell {

class CodeCellSensor : public PollingComponent {

protected:
sensor::Sensor *prox_sensor{nullptr};
sensor::Sensor *lux_sensor{nullptr};
sensor::Sensor *rawLight_sensor{nullptr};

public:

CodeCellSensor() : PollingComponent(1000) {}

float get_setup_priority() const override { return esphome::setup_priority::BUS; }

void setup() override {
    if (!vcnl4040.begin()) {
        while (1);
    }
}

void update() override {
    if (this->prox_sensor != nullptr) {
        int prox = vcnl4040.getProximity();
        prox_sensor->publish_state(prox);
    }

    if (this->lux_sensor != nullptr) {
        int lux = vcnl4040.getLux();
        lux_sensor->publish_state(lux);
    }

    if (this->rawLight_sensor != nullptr) {
        int raw = vcnl4040.getWhiteLight();
        rawLight_sensor->publish_state(raw);
    }
}

void set_prox_sensor(sensor::Sensor *sensor) { this->prox_sensor = sensor; }
void set_lux_sensor(sensor::Sensor *sensor) { this->lux_sensor = sensor; }
void set_rawlight_sensor(sensor::Sensor *sensor) { this->rawLight_sensor = sensor; }

};

} // ns codecell
} // ns esphome