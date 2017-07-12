import cloudpassage
from lib.api_session import ApiSession


class ServerController(ApiSession):
    def __init__(self):
        super(ServerController, self).__init__()
        self.api = cloudpassage.HttpHelper(self.session)
        self.sanity = SanityCheck()

    def restore_firewall(self, server_id):
        endpoint = "/v2/servers/%s/commands/firewall" % server_id
        self.srv.post(endpoint, None)
        return None
