# ################################################################################
# ## DATE: 2018-30-12
# ## AUTHOR: Óscar J. Rubio
# ##
# ################################################################################
# ## 1.0 initial release

from common_utils import menu_utils
from info_collection import *


def menu():
    while 1:

        """ INFO COLLECTION MENU """
        option = menu_utils.nice_menu('Select hacking tool', ['DNS', 'Whois', 'GeoIP', 'Google', 'Shodan', 'Metadata'])

        if (option < 1) | (option > 6):
            return

        elif option == 1:
            """ DNS submenu """
            while 1:
                sub_option = menu_utils.nice_menu('Select info retrieval mode', ['Based on domain'])
                if sub_option == 1:
                    # Domain example: dragonjar.org
                    dns_info.from_domain(menu_utils.highlighted_input('domain'))
                else:
                    break

        elif option == 2:
            """ WHOIS submenu """
            while 1:
                sub_option = menu_utils.nice_menu('Select info retrieval mode', ['Based on domain'])
                if sub_option == 1:
                    # Domain example: dragonjar.org
                    whois_info.from_domain(menu_utils.highlighted_input('domain'))
                else:
                    break

        elif option == 3:
            """ GEO submenu """
            while 1:
                sub_option = menu_utils.nice_menu("Select info retrieval mode", ["Based on domain", "Based on IP"])
                if sub_option == 1:
                    # Domain example: dragonjar.org
                    geoip_info.from_domain(menu_utils.highlighted_input('domain'))
                elif sub_option == 2:
                    # IP example: 104.27.161.40
                    geoip_info.from_ip(menu_utils.highlighted_input('IP'))
                else:
                    break

        elif option == 4:
            """ GOOGLE submenu """
            while 1:
                google_hacks = google_info.load_google_hacks_list()
                sub_option = menu_utils.nice_menu("Select a Google hack", google_hacks)
                if (sub_option < 1) | (sub_option > len(google_hacks)):
                    break
                else:
                    google_info.from_site(menu_utils.highlighted_input('site'), google_hacks[sub_option - 1])
                break

        elif option == 5:
            """ SHODAN submenu """
            while 1:
                sub_option = menu_utils.nice_menu("Select info retrieval mode", ["Based on Facets (global search)",
                                                                                 "Based on search string", "Based on IP"])
                if sub_option == 1:
                    # Domain example: nginx
                    search_str = menu_utils.highlighted_input('Shodan global search (based on facets)')
                    number_results = menu_utils.highlighted_input('number of TOP results')
                    facets_available = shodan_info.load_facets()
                    facets_list = list(facets_available.keys())
                    facets_list.insert(0, 'Your own search')
                    facets_list.append('All')
                    sub_sub_option = menu_utils.nice_menu("Select info (facet) to be retrieved",
                                                          facets_list)
                    if (sub_sub_option < 1) | (sub_sub_option > len(facets_list)):
                        break
                    elif sub_sub_option == 1:
                        user_facet = menu_utils.highlighted_input('Shodan Facet')
                        facets = [(user_facet, number_results)]
                    elif (sub_sub_option > 1) & (sub_sub_option <= len(facets_list) - 1):
                        facets = [(facets_list[sub_sub_option - 1], number_results)]
                    else:  # sub_sub_option == len(facets_list)
                        facets = []
                        for i in range(1, len(facets_list)):
                            facets.append((facets_list[i], number_results))
                    shodan_info.from_facets(search_str, facets)
                elif sub_option == 2:
                    # Domain example: apache
                    searches_available = shodan_info.load_searches()
                    if not searches_available:
                        menu_utils.warning("The file with search suggestions is empty")
                        searches_available = {}
                    searches_list = list(searches_available.values())
                    searches_list.insert(0, 'Your own search')
                    searches_list.append('Remove element from list')
                    sub_sub_option = menu_utils.nice_menu("Type of search", searches_list)
                    if (sub_sub_option < 1) | (sub_sub_option > len(searches_list)):
                        break
                    elif sub_sub_option == len(searches_list):
                        to_be_removed = int(menu_utils.highlighted_input('element from the list to be removed'))
                        if (to_be_removed > 1) & (to_be_removed < len(searches_list)):
                            del searches_available[list(searches_available.keys())[to_be_removed - 2]]
                            shodan_info.update_searches(searches_available)
                        continue
                    elif sub_sub_option == 1:
                        search_str = menu_utils.highlighted_input('Shodan search (e.g. based on city, country, geo, '
                                                                  'hostname, net, os, port)')
                        shodan_info.from_search(search_str)
                        to_be_saved = menu_utils.highlighted_input('search in the menu: (Y/n)')
                        if (to_be_saved.lower() == 'y') | (to_be_saved.lower() == 'yes'):
                            description_str = menu_utils.highlighted_input('short description')
                            searches_available[search_str] = description_str
                            shodan_info.update_searches(searches_available)
                    elif sub_sub_option > 1:
                        search_str = list(searches_available)[sub_sub_option - 2]
                        shodan_info.from_search(search_str)
                elif sub_option == 3:
                    # IP example: 104.27.161.40
                    shodan_info.from_ip(menu_utils.highlighted_input('IP'))
                else:
                    break

        elif option == 6:
            """ METADATA submenu """
            while 1:
                sub_option = menu_utils.nice_menu("Select metadata retrieval mode", ["From image", "From PDF"])
                if sub_option == 1:
                    # From image file
                    metadata_info.from_image(menu_utils.highlighted_input('image file name'))
                elif sub_option == 2:
                    # From PDF file
                    metadata_info.from_pdf(menu_utils.highlighted_input('PDF file name'))
                else:
                    break
