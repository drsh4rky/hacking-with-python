#!/usr/bin/env python
# -*- coding: utf-8 -*-

import whois                                    # external package
import pprintpp                                 # external package
from common_utils import menu_utils

""" This module uses pythonwhois API in order to retrieve data from a given domain """


def from_domain(domain):

    """This prints GEO info about a given domain, retrieved from the given geoDB"""

    try:
        info = whois.whois(domain)
        menu_utils.header("Info retrieved")
        pprintpp.pprint(info)

    except whois.parser.PywhoisError as e:
        menu_utils.error(e)




