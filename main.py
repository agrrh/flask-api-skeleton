#!/usr/bin/env python3

import sys
import os.path

from lib.config import Config
from lib.api import API


if __name__ == '__main__':
    try:
        config_path = sys.argv[1] if os.path.isfile(sys.argv[1]) else './config/example.yml'
    except (IndexError, OSError):
        config_path = './config/example.yml'

    config = Config(config_path)

    api = API(config)
    api.run()
