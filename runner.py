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

    def run(self):
        for i in self.matched_issues():
            self.server.restore_firewall(i["agent_id"])


def main():
    sys.stdout = lib.Logger(logging.info)
    sys.stderr = lib.Logger(logging.warning)
    halo_arf = AutoRestoreFw()
    halo_arf.run()

if __name__ == "__main__":
    main()

