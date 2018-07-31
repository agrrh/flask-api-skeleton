import yaml


class Config(object):
    """Translate config.yml to namespace."""
    def __init__(self, fpath):
        with open(fpath) as fp:
            data = yaml.load(fp)

        for var in data:
            setattr(self, var, data[var])
