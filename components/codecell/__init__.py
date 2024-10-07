import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, UNIT_EMPTY, ICON_EMPTY, ICON_GAUGE, UNIT_LUX, ICON_BRIGHTNESS_5, DEVICE_CLASS_ILLUMINANCE, STATE_CLASS_MEASUREMENT

AUTO_LOAD = ['sensor']

codecell_ns = cg.esphome_ns.namespace('codecell')
CodeCellSensor = codecell_ns.class_('CodeCellSensor', cg.Component)

CONF_PROX = "proximity"
CONF_LUX = "lux"
CONF_WHITE = "rawlight"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(CodeCellSensor),
        cv.Optional(CONF_PROX): sensor.sensor_schema(
            icon=ICON_GAUGE,
            # accuracy_decimals=1,
            device_class=DEVICE_CLASS_ILLUMINANCE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_LUX): sensor.sensor_schema(
            unit_of_measurement=UNIT_LUX,
            icon=ICON_BRIGHTNESS_5,
            # accuracy_decimals=1,
            device_class=DEVICE_CLASS_ILLUMINANCE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_WHITE): sensor.sensor_schema(
            # unit_of_measurement=UNIT_LUX,
            icon=ICON_BRIGHTNESS_5,
            # accuracy_decimals=1,
            device_class=DEVICE_CLASS_ILLUMINANCE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
    }
).extend(cv.polling_component_schema('10s'))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if CONF_PROX in config:
        sens1 = await sensor.new_sensor(config[CONF_PROX])
        cg.add(var.set_prox_sensor(sens1))
    if CONF_LUX in config:
        sens2 = await sensor.new_sensor(config[CONF_LUX])
        cg.add(var.set_lux_sensor(sens2))
    if CONF_WHITE in config:
        sens3 = await sensor.new_sensor(config[CONF_WHITE])
        cg.add(var.set_rawlight_sensor(sens3))
