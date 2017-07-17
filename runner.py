#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib
import logging
import sys


class AutoRestoreFw():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.server = lib.ServerController()
        self.issue = lib.IssueController()

    def matched_issues(self):
        print self.config.rule_key
        return self.issue.list_all(status="active", rule_key=self.config.rule_key)

    def log_server_info(self, srv_id):
        srv = self.server.show(srv_id)
        srv_info = ("Requested to restore firewall policy for agent id: {agent_id}, "
                    "agent hostname: {agent_hostname}, "
                    "group name: {group_name}, "
                    "group_id: {group_id}")

        sys.stdout.write(srv_info.format(agent_id=srv["id"], agent_hostname=srv["reported_fqdn"],
                                         group_name=srv["group_name"], group_id=srv["group_id"]))
        return None

    def run(self):
        for i in self.matched_issues():
            self.server.restore_firewall(i["agent_id"])
            self.log_server_info(i["agent_id"])


def main():
    sys.stdout = lib.Logger(logging.info)
    sys.stderr = lib.Logger(logging.warning)
    halo_arf = AutoRestoreFw()
    halo_arf.run()
if __name__ == "__main__":
    main()

