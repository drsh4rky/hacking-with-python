#!/usr/bin/env python
# -*- coding: utf-8 -*-

import whois                                    # external package
import pprintpp                                 # external package
from common_utils import menu_utils

""" This module uses python-whois API in order to retrieve data from a given domain """


def from_domain(domain):

    """This prints WHOIS info about a given domain"""

    info = whois.query(domain)
    menu_utils.header("Info retrieved")
    info = {"name": info.name,
            "name servers": info.name_servers,
            "registrar": info.registrar,
            "creation date": info.creation_date,
            "expiration date": info.expiration_date,
            "last updated": info.last_updated}
    pprintpp.pprint(info)




