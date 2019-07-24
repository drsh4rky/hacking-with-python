#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygeoip                                      # external package
import pprintpp                                     # external package
import config_params
from common_utils import menu_utils

""" This module uses pygeoip in order to retrieve geo data from either domains or IPs """


def from_domain(domain):

    """This prints GEO info about a given domain, retrieved from the given geoDB"""

    try:
        gi = pygeoip.GeoIP(config_params.GEO_FILE)
        menu_utils.header("Info retrieved")
        menu_utils.mixed_info("[+] Server country code from domain: ", gi.country_code_by_name(domain))

    except pygeoip.socket.gaierror as e:
        menu_utils.error(e)


def from_ip(ip):

    """This prints GEO info about a given IP, retrieved from the given geoDB"""

    try:
        gi = pygeoip.GeoIP(config_params.GEO_FILE)
        menu_utils.header("Info retrieved")
        menu_utils.mixed_info("[+] Server country code from IP: ", gi.country_code_by_addr(ip))
        menu_utils.mixed_info("[+] Server time zone from IP: ", gi.time_zone_by_addr(ip))
        menu_utils.highlighted_info("[+] Server complete info from IP: ")
        pprintpp.pprint(gi.record_by_addr(ip))

    except OSError as e:
        menu_utils.error(e)
