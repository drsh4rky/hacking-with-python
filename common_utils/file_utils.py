#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads, dumps

""" This module provides utils for handling files """


def load_file_as_list(file):

    with open(file, 'r') as f:
        return [line.rstrip('\n') for line in f]


def load_dictionary_from_file(file):

    s = load_file_as_list(file)[0] # everything is in the first line
    return loads(s)


def write_file_from_dictionary(dictionary, file):

    with open(file, 'w+') as f:
        f.write(dumps(dictionary))


def append_line_to_file(file, line):

    with open(file, 'a+') as f:
        f.write(line + "\r\n")


def remove_line_from_file(file, line_number):

    lines = load_file_as_list(file)

    with open(file, 'w+') as f:
        for i in range(len(lines)):
            if i != line_number-1:
                f.write(lines[i] + "\r\n")

