# What is Hacking-with-Python?

<img align="right" src="https://github.com/drsh4rky/hacking-with-python/blob/master/hwp_menu.png">

Hacking-with-Python is a simple and extensible tool intended for the initiation to ethical hacking activities and python scripting. This tool integrates well-known hacking libraries (e.g. shodan, Scapy, nmap) and provides a friendly interface that **permits users to perform the essential stages of a hacking process without dealing with complexities**. The interface displays a menu which permits choosing:

* **Information collection**, including DNS queries, WHOIS queries, geoIP queries, Google hacking, Shodan searches and metadata analysis. 
* **Vulnerability analysis**, including Nmap scanning, port scanning with Scapy and banner grabbing.
* **Attacks**, including (D)DoS and dictionary attacks. 

Additional options for attacks and post-exploitation will be added in the future.

# Get Started

* `git clone https://github.com/drsh4rky/hacking-with-python.git`
* `cd hacking-with-python`
* `pip install -r requirements.txt`
* `python ./launcher.py`  

# Configuration 

* Paste your shodan key in `./Keys/shodanKeys` to enable Shodan searches
* Optionally, you can also modify the `config_params.py` file to:
	* Modify the look & feel of the tool (e.g. change the color of regular text to blue `"color": "blue"`)
	* Modify the parameters of the tool (e.g. get a higher number of `MAX_NUMBER_THREADS` to speed up dictionary attacks if your machine supports it)
* Add new files to existing folders under `./DDBB/` to create new possibilities (e.g. add new password dictionaries in `./DDBB/Dictionaries/`)
* Edit existing files under `./DDBB/` with new information of value (e.g. add new vulnerable banners in `./DDBB/Banners/vulnerable_banners.txt`) so that they are detected when performing banner grabbing)

# Extension

This tool is currently divided into four packages:
* common_utils
* information_collection
* vulnerability_analysis
* attack

Any of these packages can be extended with new modules. Please use functions from common_utils.menu_utils.py to manage user I/O. To make the new module(s) available in the tool menu:
* Place it within the corresponding package folder
* Add the module name in the `__init_.py`file of the corresponding package
* Edit the `*menu.py` of the package to add the module as a new option in the tool menu

# License

The project is released under the [MIT license](https://github.com/drsh4rky/hacking-with-python/blob/master/license.txt)

# Contact
If you have any question, please file an issue or contact the author:
```
Oscar J. Rubio: oscar.rubio.martin@gmail.com
```
