#!/usr/bin/env python
# -*- coding: utf-8 -*-

from termcolor import colored               # external package
from time import sleep
import config_params
import os
import sys

""" This module provides utils for handling interactive menus """


def cls():

    os.system('cls' if os.name == 'nt' else 'clear')


def banner():

    cls()
    for i in range(0, len(config_params.DISPLAY['banner'])):
        highlighted_info(config_params.DISPLAY['banner'][i])
        if i == len(config_params.DISPLAY['banner']) - 3:
            print(colored("                                           ENJOY IT :)",
                          config_params.DISPLAY['color_error'], attrs=config_params.DISPLAY['color_attrs_error']))
        sleep(0.1)


def see_you_soon():

    super_highlighted_info(config_params.DISPLAY["exit_message"])
    exit()


def header(title):

    print("")
    # line with config_params.DISPLAY['title_width'] characters =
    print(colored("=", config_params.DISPLAY['color'],
                  attrs=config_params.DISPLAY['color_attrs']) * config_params.DISPLAY['title_width'])
    # centering the text of the title
    print(" " * int((config_params.DISPLAY['title_width'] - len(title))/2), end="")
    # centered title
    print(colored(title, config_params.DISPLAY['color'], attrs=config_params.DISPLAY['color_attrs']))
    # line with config_params.DISPLAY['title_width'] characters =
    print(colored("=", config_params.DISPLAY['color'],
                  attrs=config_params.DISPLAY['color_attrs']) * config_params.DISPLAY['title_width'])
    print("")


def nice_menu(title, options):

    # full_text = '\n\t' + title.upper() + ': \n\n'
    full_text = ""
    header(title.upper())

    for i in range(0, len(options)):
        full_text += '\t' + str(i+1) + ') ' + options[i] + ' \n'
    full_text += '\n\tOther) Exit   --> '

    try:
        option = int(float(input(colored(full_text, config_params.DISPLAY['color'],
                                         attrs=config_params.DISPLAY['color_attrs']))))

    except ValueError:
        print(colored('You should introduce a number', config_params.DISPLAY['color_error'],
                      attrs=config_params.DISPLAY['color_attrs_error']))
        option = -1

    return option


def mixed_info(info1, info2):

    print(colored(info1, config_params.DISPLAY['color'], attrs=config_params.DISPLAY['color_attrs']), end=" ")
    print(info2)


def highlighted_info(info):

    print(colored(info, config_params.DISPLAY['color'], attrs=config_params.DISPLAY['color_attrs']))


def super_highlighted_info(info):

    print(colored(info, config_params.DISPLAY['color'], attrs=config_params.DISPLAY['color_attrs_error']))


def warning(warn):

    print(colored(warn, config_params.DISPLAY['color_error'], attrs=config_params.DISPLAY['color_attrs']))


def error(e):

    warning('There has been an error: %s' % e)


def highlighted_input(question):

    return input(colored("\n Introduce the %s : " % question, config_params.DISPLAY['color'],
                         attrs=config_params.DISPLAY['color_attrs']))


def conditional_highlighting(info, positive_word, negative_word):

    lines = info.split('\n')
    for line in lines:
        if positive_word in line:
            highlighted_info(line)
        elif negative_word in line:
            warning(line)
        else:
            print(line)


def erase_last_line():

    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line


def overwrite_last_line(info):

    erase_last_line()
    print(info)


def progress_bar(percentage, bar_width, additional_info):

    filled_bar = int(percentage/100*bar_width)
    overwrite_last_line(str(percentage) + "% " + "[" + filled_bar*"=" + (bar_width-filled_bar)*" " + "] "
                        + additional_info)

