import logging
import simpy

from utils import get_parsed_arguments, logger, get_config
from machine import Machine


@logger
def start_simulation(machine_name, machine_properties, cycle_time, work_period):
    logging.info("Starting simulation")
    real_time_env = simpy.rt.RealtimeEnvironment(factor=cycle_time)
    Machine(real_time_env, machine_properties, machine_name)
    simulation_cycles = work_period / cycle_time
    real_time_env.run(until=simulation_cycles)
    logging.info("Simulation fininshed")


config = get_config()
args = get_parsed_arguments()


start_simulation(
    args.name,
    machine_properties=config["machineProperties"],
    cycle_time=config["cycleTime"],
    work_period=10,
)
