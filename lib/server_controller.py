import cloudpassage
import sys
from lib.api_session import ApiSession


class ServerController(ApiSession):
    def __init__(self):
        super(ServerController, self).__init__()
        self.api = cloudpassage.HttpHelper(self.session)
        self.srv = cloudpassage.Server(self.session)

    def show(self, server_id):
    	return self.srv.describe(server_id)

    def restore_firewall(self, server_id):
        endpoint = "/v2/servers/%s/commands/firewall" % server_id
        self.api.post(endpoint, None)
        return None


