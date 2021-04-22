#!/usr/bin/env python
# SECUREAUTH LABS. Copyright 2021 SecureAuth Corporation. All rights reserved.
#
# This software is provided under under a slightly modified version
# of the Apache Software License. See the accompanying LICENSE file
# for more information.
#
# Utility and helper functions for the example scripts
#
import re


target_regex = re.compile(r"(?:(?:([^/@:]*)/)?([^@:]*)(?::([^@]*))?@)?(.*)")


def parse_target(target):
    """ Helper function to parse target information. The expected format is:

    <DOMAIN></USERNAME><:PASSWORD>@HOSTNAME

    :param target: target to parse
    :type target: string

    :return: tuple of domain, username, password and remote name or IP address
    :rtype: (string, string, string, string)
    """
    domain, username, password, remote_name = target_regex.match(target).groups('')

    # In case the password contains '@'
    if '@' in remote_name:
        password = password + '@' + remote_name.rpartition('@')[0]
        remote_name = remote_name.rpartition('@')[2]

    return domain, username, password, remote_name
