# ################################################################################
# ## DATE: 2019-18-07
# ## AUTHOR: Óscar J. Rubio
# ##
# ################################################################################
# ## 1.0 initial release

from common_utils import menu_utils
from common_utils import var_utils
import config_params
from os.path import join
from attack import *


def menu():

    while 1:

        """ ATTACK MENU """
        option = menu_utils.nice_menu('Select hacking tool', ['DDoS attack', 'Dictionary attack'])

        if (option < 1) | (option > 2):
            return

        elif option == 1:
            """ DDoS submenu """

            attackers_ips = var_utils.parse_cidr_ips(menu_utils.highlighted_input('attacker IPs (in CIDR format, e.g. '
                                                                                  '192.168.1.2/28, 192.168.2.3)'))
            ips = var_utils.parse_cidr_ips(menu_utils.highlighted_input('target IPs (in CIDR format, e.g. '
                                                                        '192.168.1.4/30, 192.168.2.7)'))
            ports = var_utils.parse_ports(menu_utils.highlighted_input('target ports (e.g. 20-22, 80)'))
            duration = int(menu_utils.highlighted_input('attack duration (in seconds)'))
            ddos_attack.ddos_attack(attackers_ips, ips, ports, duration)

        elif option == 2:
            """ Dictionary attack submenu """

            sub_option = menu_utils.nice_menu("Select the protocol", ["FTP", "SSH"])
            if (sub_option < 1) | (sub_option > 2):
                break
            else:
                login_dictionaries = dictionary_attack.load_dictionaries_list()
                sub_sub_option = menu_utils.nice_menu("Select a dictionary", login_dictionaries)
                if (sub_sub_option < 1) | (sub_sub_option > len(login_dictionaries)):
                    break
                else:
                    ip = menu_utils.highlighted_input('target IP')
                    port = int(menu_utils.highlighted_input('port (typically 21 for FTP, 22 for SSH)'))
                    interval = int(menu_utils.highlighted_input('interval between attempts (in milliseconds)'))
                    user = menu_utils.highlighted_input('user (e.g. "root", "user", "msfadmin")')
                    dictionary_file = join(config_params.CREDENTIALS_DICTIONARIES_FOLDER,
                                           login_dictionaries[sub_sub_option-1])
                if sub_option == 1:
                    dictionary_attack.dictionary_attack("FTP", ip, port, interval, user, dictionary_file)
                elif sub_option == 2:
                    dictionary_attack.dictionary_attack("SSH", ip, port, interval, user, dictionary_file)



