#!/usr/bin/env python3

"""
https://github.com/msd0pe-1
Source code put in public domain by msd0pe, no Copyright
Any malicious or illegal activity may be punishable by law
Use at your own risk
"""

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class infos:
    INFO = "[" + bcolors.OCRA + bcolors.BOLD + "?" + bcolors.ENDC + bcolors.ENDC + "] "
    ERROR = "[" + bcolors.RED + bcolors.BOLD + "X" + bcolors.ENDC + bcolors.ENDC + "] "
    GOOD = "[" + bcolors.GREEN + bcolors.BOLD + "+" + bcolors.ENDC + bcolors.ENDC + "] "
    PROCESS = "[" + bcolors.BLUE + bcolors.BOLD + "*" + bcolors.ENDC + bcolors.ENDC + "] "

try:
    import json
    import whois
    import shodan
    import socket
    import requests

except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 passiv-recon.py ....")
    print(infos.INFO + "./passiv-recon.py ....\n")


class Modules_List():

#---------------------------

    def Exploitdb(app_name, versions):
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
        for version in versions:
            url = "https://www.exploit-db.com/search?q=" + str(app_name) + " " + str(version)
            exploitdb_output = requests.get(url, headers=headers).json()
            exploitdb_output = json.dumps(exploitdb_output, sort_keys=False, indent=4)
            exploitdb_output = json.loads(exploitdb_output)
            exploitdb = exploitdb_output['data']

            for i in range(0,len(exploitdb)):
                exploitdb_tmp = exploitdb[i]
                name = exploitdb_tmp['description'][1]
                date = exploitdb_tmp['date_published']
                edb_id = exploitdb_tmp['id']

                print("\t\t" + bcolors.RED + bcolors.BOLD + "EDB-ID-" + bcolors.ENDC + bcolors.ENDC + edb_id + " : " + name + " - " + date)

#---------------------------

    def Whois(site, mod, exc):
        try:
            print(infos.PROCESS + bcolors.BOLD + bcolors.BLUE + "WHOIS\n" + bcolors.ENDC + bcolors.ENDC)
            whois_output = whois.query(site)
            print(infos.INFO + "Name : " + bcolors.RED + whois_output.name + bcolors.ENDC)
            print(infos.INFO + "Registrar : " + bcolors.RED +  whois_output.registrar + bcolors.ENDC)
            print(infos.INFO + "Creation Date : " + str(whois_output.creation_date))
            print(infos.INFO + "Expiration Date : " + str(whois_output.expiration_date))
            print(infos.INFO + "Last Update : " + str(whois_output.last_updated))
            print(infos.INFO + "Name Servers : " + bcolors.RED + str(whois_output.name_servers) + bcolors.ENDC)
            print("\n")

        except:
            print(infos.ERROR + "Whois seems unreachable !\n")

#---------------------------

    def Wappalyzer(site, mod, exc):
        try:
            if exc == None:
                print(infos.PROCESS + bcolors.BOLD + bcolors.BLUE + "WAPPALYZER AND EXPLOITDB\n" + bcolors.ENDC + bcolors.ENDC)
            elif exc.lower().capitalize() == "Exploitdb":
                print(infos.PROCESS + bcolors.BOLD + bcolors.BLUE + "WAPPALYZER\n" + bcolors.ENDC + bcolors.ENDC)
            else:
                print(infos.PROCESS + bcolors.BOLD + bcolors.BLUE + "WAPPALYZER AND EXPLOITDB\n" + bcolors.ENDC + bcolors.ENDC)

            headers = {'x-api-key' : ''} ## ENTER WAPPALYZER API KEY HERE !
            params = {'urls' : "https://" + site}
            wappalyzer_output = requests.get('https://api.wappalyzer.com/lookup/v2/', headers=headers, params=params).json()
            wappalyzer_output = json.dumps(wappalyzer_output, sort_keys=False, indent=4)
            wappalyzer_output = json.loads(wappalyzer_output)

            wappalyzer = wappalyzer_output[0]
            wappalyzer = wappalyzer['technologies']

            print(infos.GOOD + "Detected technologies :\n")

            for i in range(0,len(wappalyzer)):
                wappalyzer_tmp = wappalyzer[i]
                app_name = wappalyzer_tmp['name']
                versions = wappalyzer_tmp['versions']
                categories = wappalyzer_tmp['categories'][0]['name']
                print("\t" + bcolors.RED + str(app_name) +  bcolors.ENDC + " " + str(categories) + " Version : " + bcolors.RED + str(versions) + bcolors.ENDC)
                if versions != [] and exc == None:
                    Modules_List.Exploitdb(app_name, versions)
            print("")

        except KeyError:
            print(infos.ERROR + "API Key seems to be incorrect. Edit it on the modules.py file !\n")

        except:
            print(infos.ERROR + "Wappalyzer seems unreachable !\n")

#---------------------------

    def Shodan(site, mod, exc):
       try:
            print(infos.PROCESS + bcolors.BOLD + bcolors.BLUE + "SHODAN\n" + bcolors.ENDC + bcolors.ENDC)

            SHODAN_API_KEY = "" ## ENTER SHODAN API KEY HERE !
            api = shodan.Shodan(SHODAN_API_KEY)

            site_ip = socket.gethostbyname(site)
            host = api.host(site_ip)

            print(infos.INFO + "IP: " + bcolors.RED + "{}".format(host['ip_str']) + bcolors.ENDC)
            print(infos.INFO + "Organization: " + bcolors.RED + "{}".format(host.get('org', 'n/a')) + bcolors.ENDC)
            print(infos.INFO + "Operating System: " + bcolors.RED + "{}".format(host.get('os', 'n/a')) + bcolors.ENDC)
            print(infos.INFO + "Country : " + bcolors.RED + "{}\n".format(host.get('country_name', 'n/a')) + bcolors.ENDC)

            for item in host['data']:
                print(infos.GOOD + "Port: " + bcolors.CYAN + "{}\n".format(item['port']) + bcolors.ENDC)
                print(bcolors.PURPLE + "Banner: {}".format(item['data']) + bcolors.ENDC)

       except shodan.exception.APIError:
           print(infos.ERROR + "API Key seems to be incorrect. Edit it on the modules.py file !\n")

       except:
           print(infos.ERROR + "Shodan seems unreachable !\n")

#---------------------------

    modules_list = {'Whois':Whois, 'Shodan':Shodan, 'Wappalyzer':Wappalyzer, 'Exploitdb':Exploitdb}
