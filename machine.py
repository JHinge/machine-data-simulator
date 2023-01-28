import logging
import random
from datetime import datetime

number_type = {"int": int, "float": float}


class Machine(object):
    def __init__(self, environment, property_settings, name, cycle_time):
        self.environment = environment
        self.cycle_time = cycle_time
        self.name = name
        self.property_settings = property_settings
        self.property_values = dict()
        self.process = environment.process(self.work())

    def get_current_property_value(self, property_name):
        result = dict()
        result["value"] = self.property_values[property_name]
        result["unit"] = self.property_settings[property_name]["unit"]
        result["timestamp"] = str(datetime.now())
        return result

    def work(self):
        while True:
            done = False
            while not done:
                yield self.environment.timeout(self.cycle_time)
                done = True

            for name, settings in self.property_settings.items():
                print(name, settings)
                property_value_type = number_type[settings["type"]]
                self.property_values[name] = property_value_type(
                    random.uniform(settings["minValue"], settings["maxValue"])
                )

                logging.info(self.get_current_property_value(name))
