# ################################################################################
# ## DATE: 2018-19-03
# ## AUTHOR: Óscar J. Rubio
# ##3
# ################################################################################
# ## 1.0 initial release

from common_utils import menu_utils
from info_collection import info_collection_menu
from vulnerability_analysis import vulnerability_analysis_menu
from attack import attack_menu
import signal


def main_keyboard_interrupt_handler(signal, frame):
    menu_utils.super_highlighted_info("\n\nThanks for using Hacking-With-Python, see you soon !\n")
    exit()


signal.signal(signal.SIGINT, main_keyboard_interrupt_handler)
menu_utils.banner()

while 1:

    """ MAIN MENU """

    option = menu_utils.nice_menu('Select category', ['Info collection', 'Vulnerability analysis', 'Attack'])
    if (option < 1) | (option > 3):
        break

    if option == 1:
        info_collection_menu.menu()

    elif option == 2:
        vulnerability_analysis_menu.menu()

    elif option == 3:
        attack_menu.menu()


    












