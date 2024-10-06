import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, UNIT_EMPTY, ICON_EMPTY, UNIT_LUX, ICON_BRIGHTNESS_5, DEVICE_CLASS_ILLUMINANCE, STATE_CLASS_MEASUREMENT

AUTO_LOAD = ['sensor']

codecell_ns = cg.esphome_ns.namespace('codecell')
CodeCellSensor = codecell_ns.class_('CodeCellSensor', sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = (
    sensor.sensor_schema(
        CodeCellSensor,
        # unit_of_measurement=UNIT_LUX,
        # accuracy_decimals=1,
        device_class=DEVICE_CLASS_ILLUMINANCE,
        state_class=STATE_CLASS_MEASUREMENT,
    )
    .extend(cv.polling_component_schema('10s'))
)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)

