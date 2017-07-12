import os
import yaml


class ConfigHelper(object):
    def __init__(self):
        config = self.read_yml('configs')
        self.halo_key = config["halo"]["api_key"]
        self.halo_secret = config["halo"]["api_secret_key"]
        self.rule_key = config["rule_key"]

    @classmethod
    def read_yml(self, f):
        yml_path = os.path.join(os.path.dirname(__file__), "../configs/%s.yml" % f)
        return yaml.load(file(yml_path, 'r'))
