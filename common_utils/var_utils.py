#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from netaddr import *           # external package

""" This module provides utils for handling variables """


def _parse_range(rng):

    parts = rng.split('-')
    if 1 > len(parts) > 2:
        raise ValueError("Bad range: '%s'" % (rng,))
    parts = [int(i) for i in parts]
    start = parts[0]
    end = start if len(parts) == 1 else parts[1]
    if start > end:
        end, start = start, end
    return range(start, end + 1)


def parse_ports(ports):

    return sorted(set(itertools.chain(*[_parse_range(rng) for rng in ports.split(',')])))


def parse_cidr_ips(ips):

    ip_list = []

    for ip in IPSet(ips.replace(" ", "").strip().split(',')):
        ip_list.append(str(ip))

    return ip_list


def list_2_string(list_or_iterator):
    return "[" + ", ".join(str(x) for x in list_or_iterator) + "]"


def numbers_2_ranges(numbers_list):

    result = []
    if not numbers_list:
        return result
    idata = iter(numbers_list)
    first = prev = next(idata)
    for following in idata:
        if following - prev == 1:
            prev = following
        else:
            result.append((first, prev + 1))
            first = prev = following
    # There was either exactly 1 element and the loop never ran,
    # or the loop just normally ended and we need to account
    # for the last remaining range.
    result.append((first, prev + 1))
    return result
