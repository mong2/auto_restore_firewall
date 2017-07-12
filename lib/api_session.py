from lib.config_helper import ConfigHelper
import cloudpassage


class ApiSession(ConfigHelper):
    def __init__(self):
        super(ApiSession, self).__init__()
        self.session = cloudpassage.HaloSession(self.halo_key, self.halo_secret)
