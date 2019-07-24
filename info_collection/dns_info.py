#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dns                                  # external package
import dns.resolver                         # external package
from common_utils import menu_utils

""" This module uses dns in order to retrieve dns registry data from domains """


def from_domain(domain):

    """This prints registry info about a given domain"""

    try:
        """ Consult IPV4 registry """
        ans_a = dns.resolver.query(domain, 'A')

        """ Consult IPV6 registry """
        ans_aaaa = dns.resolver.query(domain, 'AAAA')

        """ Consult MailServers registry """
        ans_mx = dns.resolver.query(domain, 'MX')

        """ Consult NameServers registry """
        ans_ns = dns.resolver.query(domain, 'NS')

        menu_utils.header("Response of hacking tools for IPV4")
        print(ans_a.response.to_text())

        menu_utils.header("Response of hacking tools for IPV6")
        print(ans_aaaa.response.to_text())

        menu_utils.header("Response of hacking tools for MailServers")
        print(ans_mx.response.to_text())

        menu_utils.header("Response of hacking tools for NameServers")
        print(ans_ns.response.to_text())

    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
        menu_utils.error(e)
