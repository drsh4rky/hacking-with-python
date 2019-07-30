#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Very relevant constants

GEO_FILE = "./DDBB/GEO_IP/GeoLiteCity.dat"  							# Location of the file with the Geo IP info
GOOGLE_HACKS_FOLDER = "./DDBB/Google_hacking/"  						# Location of the folder with Google Hack files
SHODAN_SEARCHES_FILE = "./DDBB/Shodan_hacking/saved_searches.json"  	# Location of the Shodan searches file
SHODAN_FACETS_FILE = "./DDBB/Shodan_hacking/saved_facets.json"  		# Location of the Shodan facets file
SHODAN_KEY_FILE = "./Keys/ShodanKey"  									# Location of the Shodan developer key
VULNERABLE_BANNERS = "./DDBB/Banners/vulnerable_banners.txt"			# Location of the file with vulnerable banners
CREDENTIALS_DICTIONARIES_FOLDER = "./DDBB/dictionaries/"				# Location of the credentials dictionaries

SCAPY_TIMEOUT = 0.2														# Timeout for receiving of packet reply
BANNER_TIMEOUT = 15														# Timeout for receiving a banner
FTP_SERVER_TIMEOUT = 20													# Timeout for a FTP connection
DDOS_INTERPACKET_INTERVAL = 0											# Interval between consecutive DDoS packets
MAX_NUMBER_THREADS = 200												# Maximum number of threads in multi-thread computing

# Parametrized display format: 

DISPLAY = {
	"color": "green",     	  			# Font color for regular text
	"color_attrs": ["bold"],  			# Style for regular menu text
	"color_error": "red",  				# Color for error text
	"color_attrs_error": ["blink"],  	# Style for error text
	"title_width": 64,  				# Width (in characters) of a title
	"banner": [							# Initial banner
		"                                         						  ",
		"=================================================================",
		"																  ",
		"            ___               ___               ___      		  ",
		"           /\__\             /\__\             /\  \     		  ",
		"          /:/  /            /:/ _/_           /::\  \    		  ",
		"         /:/__/            /:/ /\__\         /:/\:\  \   		  ",
		"        /::\  \ ___       /:/ /:/ _/_       /::\~\:\  \  		  ",
		"       /:/\:\  /\__\     /:/_/:/ /\__\     /:/\:\ \:\__\ 	      ",
		"       \/__\:\/:/  /     \:\/:/ /:/  /     \/__\:\/:/  / 		  ",
		"            \::/  /       \::/_/:/  /           \::/  /  		  ",
		"            /:/  /         \:\/:/  /             \/__/   		  ",
		"           /:/  /           \::/  /                 			  ",
		"           \/__/             \/__/                  			  ",
		"                               								  ",
		"=========================== drsh4rky ============================"
	],
	"exit_message": "\n\nThanks for using Hacking-With-Python, see you soon !\n",
	"progress_bar_width": 50			# Width of the progress bar
}


