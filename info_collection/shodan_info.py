#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shodan                               # external package
from common_utils import file_utils
from common_utils import menu_utils
import config_params


""" This module uses shodan in order to retrieve data from search strings or IPs """


def load_facets():

    """This loads the facets stored in the corresponding file"""

    return file_utils.load_dictionary_from_file(config_params.SHODAN_FACETS_FILE)


def load_searches():

    """This loads the searches stored in the corresponding file"""

    return file_utils.load_dictionary_from_file(config_params.SHODAN_SEARCHES_FILE)


def update_searches(searches_dict):

    """This updates the searches file"""

    file_utils.write_file_from_dictionary(searches_dict, config_params.SHODAN_SEARCHES_FILE)


def from_facets(search_string, chosen_facets):

    """This prints the result from a shodan search with a given facet"""

    # Developer Shodan API key
    shodan_key_string = open(config_params.SHODAN_KEY_FILE).readline().rstrip('\n')
    # Connecting to the SHODAN DB
    shodan_api = shodan.Shodan(shodan_key_string)
    facets = load_facets()

    try:
        # Use the count() method because it doesn't return results and doesn't require a paid API plan
        # And it also runs faster than doing a search().
        result = shodan_api.count(search_string, facets=chosen_facets)
        menu_utils.highlighted_info('Results found: %s' % result['total'])
        # Print the summary info from the facets
        if 'facets' in result.keys():
            for facet in result['facets']:
                if facet in facets.keys():
                    menu_utils.header(facets[facet] % chosen_facets[0][1])
                for term in result['facets'][facet]:
                    menu_utils.mixed_info("[+] " + str(term['value']) + ": ", str(term['count']))

    except shodan.APIError as e:
        menu_utils.error(e)


def from_search(search_string):

    """This prints the result from a shodan search with a given string"""

    # Developer Shodan API key
    shodan_key_string = open(config_params.SHODAN_KEY_FILE).readline().rstrip('\n')
    # Connecting to the SHODAN DB
    shodan_api = shodan.Shodan(shodan_key_string)

    try:
        results = shodan_api.search(search_string)    # apache

        # Print results
        menu_utils.highlighted_info('Results found: %s' % results['total'])
        counter = 0
        for i in results['matches']:
            counter += 1
            menu_utils.header('Result #%s' % counter)
            if i['ip_str']:
                if i['ip_str'] != "":
                    menu_utils.mixed_info("[+] IP: ", i['ip_str'])
            if i['port']:
                if i['port'] != "":
                    menu_utils.mixed_info("[+] Port: ", i['port'])
            if i['hostnames']:
                if i['hostnames'] != "":
                    print('Hostnames: ' % i['hostnames'])
                    menu_utils.mixed_info("[+] Hostnames: ", i['hostnames'])
            if i['os']:
                if i['os'] != "":
                    menu_utils.mixed_info("[+] Operating system: ", i['os'])
            if i['data']:
                if i['data'] != "":
                    menu_utils.mixed_info("[+] Data: ", i['data'])
            if i['timestamp']:
                if i['timestamp'] != "":
                    menu_utils.mixed_info("[+] Timestamp: ", i['timestamp'])
            print('')

    except shodan.APIError as e:
            menu_utils.error(e)


def from_ip(ip):

    """This prints the result from a shodan search with a given IP"""

    # Developer Shodan API key
    shodan_key_string = open(config_params.SHODAN_KEY_FILE).readline().rstrip('\n')
    # Connecting to the SHODAN DB
    shodan_api = shodan.Shodan(shodan_key_string)

    try:
        host = shodan_api.host(ip)
        menu_utils.header("Info retrieved")
        menu_utils.mixed_info("[+] IP: ", host['ip_str'])
        menu_utils.mixed_info("[+] Organization: ", host.get('org', 'n/a'))
        menu_utils.mixed_info("[+] Operating system: ", host.get('os', 'n/a'))
        for item in host['data']:
            menu_utils.mixed_info("[+] Port: ", item['port'])
            menu_utils.mixed_info("[+] Banner: ", item['data'])

    except shodan.APIError as e:
        menu_utils.error(e)
