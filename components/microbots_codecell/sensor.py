import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, UNIT_EMPTY, ICON_EMPTY, UNIT_LUX, ICON_BRIGHTNESS_5

microbots_codecell_ns = cg.esphome_ns.namespace('microbots_codecell')
MyCodeCell = microbots_codecell_ns.class_('MyCodeCell', sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = sensor.sensor_schema(UNIT_LUX, ICON_BRIGHTNESS_5, 1).extend({
    cv.GenerateID(): cv.declare_id(MyCodeCell)
}).extend(cv.polling_component_schema('10s'))

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)
  
