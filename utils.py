import argparse
import json
import logging

from functools import wraps

DEFAULT_CONFIG_FILE_PATH = "config.json"


def get_config():
    with open(DEFAULT_CONFIG_FILE_PATH, "r") as f:
        config_data = json.load(f)

    return config_data


def get_parsed_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--runtime",
        help="How long simulator should work in seconds",
        default=10,
        type=int,
    )
    parser.add_argument("--name", help="Simulated machine name", required=True)

    return parser.parse_args()


def start_logging(filename):
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[logging.FileHandler(filename), logging.StreamHandler()],
    )


def stop_logging():
    logging.shutdown()


def logger(func):
    def wrapper(*args, **kwargs):
        config = get_config()
        start_logging(config["outputFileName"])
        func(*args, **kwargs)
        stop_logging()

    return wrapper
