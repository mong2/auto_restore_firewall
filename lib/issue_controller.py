import cloudpassage
import lib
from lib.api_session import ApiSession


class IssueController(ApiSession):
    def __init__(self):
        super(IssueController, self).__init__()
        self.issue_obj = cloudpassage.Issue(self.session)

    def list_all(self, **kwargs):
        try:
            result = self.issue_obj.list_all(**kwargs)
            if not result:
                raise TypeError
        except TypeError:
            result = self.issue_obj.list_all(**kwargs)
        return result
