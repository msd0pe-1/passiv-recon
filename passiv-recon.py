#!/usr/bin/env python3

__description__ = 'Tool for making the environment of a target passively.'
__author__ = 'msd0pe'
__version__ = '1.1'
__date__ = '2020/07/28'

"""
https://github.com/msd0pe-1
Source code put in public domain by msd0pe, no Copyright
Any malicious or illegal activity may be punishable by law
Use at your own risk
"""

"""
CHANGELOG:
        2020/07/28 : V1.1 - Adding the exploit-db module.
        2020/06/30 : V1.0 - Project Start.
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
    import optparse
    import modules as modules
    from pyfiglet import Figlet
    from urllib.parse import urlparse

except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 passiv-recon.py ....")
    print(infos.INFO + "./passiv-recon.py ....\n")

def Main():
    Menu = optparse.OptionParser(usage='python %prog [options] url', version='%prog ' + __version__)
    Menu.add_option('-m', '--mod', type="str", dest="mod", help='execute only one module')
    Menu.add_option('-e', '--exc', type="str", dest="exc", help='exclude one module of the execution list')
    (options, args) = Menu.parse_args()

    Mods = optparse.OptionGroup(Menu, "Available Modules", "Whois\nShodan\nWappalyzer\nExploitdb")
    Menu.add_option_group(Mods)

    Examples = optparse.OptionGroup(Menu, "Examples", """python passiv-recon.py https://www.google.com
                                                         python passiv-recon.py -m Shodan  https://www.google.com
                                                         python passiv-recon.py -e Wappalyzer https://google.com""")

    Menu.add_option_group(Examples)

    if len(args) != 1:
        Menu.print_help()
        print('')
        print('  %s' % __description__)
        print('  Source code put in public domain by ' + bcolors.PURPLE + bcolors.BOLD + 'msd0pe' + bcolors.ENDC + bcolors.ENDC + ',' + bcolors.RED + bcolors.BOLD + 'no Copyright' + bcolors.ENDC + bcolors.ENDC)
        print('  Any malicious or illegal activity may be punishable by law')
        print('  Use at your own risk')

    elif len(args) == 1:
        font = Figlet(font='slant')
        print(bcolors.RED + font.renderText('PASSIV-RECON') + bcolors.ENDC)
        site = urlparse(args[0]).netloc
        if site != "":
            pass
        else:
            print(infos.ERROR + "The URL seems to be incorrect. Use http(s)://... !\n")
            exit(1)

        try:
            if options.mod == None and options.exc == None:
                print("Searching on :")
                for module in modules.Modules_List.modules_list:
                    print(infos.GOOD + module)
                print()

                for module in modules.Modules_List.modules_list:
                    if module == "Exploitdb":
                        pass
                    else:
                        modules.Modules_List.modules_list[module](site, options.mod, options.exc)

            elif options.mod != None and options.exc == None:
                if options.mod.lower().capitalize() in modules.Modules_List.modules_list:
                    if options.mod.lower().capitalize() == "Exploitdb":
                        print(infos.ERROR + "Exploitdb need Wappalyzer to be launch ! \n")
                    else:
                        print("Searching on :")
                        if options.mod.lower().capitalize() == "Wappalyzer":
                            print(infos.GOOD + "Wappalyzer")
                            print(infos.GOOD + "Exploitdb")
                            print()
                        else:
                            print(infos.GOOD + options.mod.lower().capitalize())
                            print()
                        modules.Modules_List.modules_list[options.mod.lower().capitalize()](site, options.mod, options.exc)

                else:
                    print(infos.ERROR + "Enter a valid module ! Use --help to see the module list. \n")

            elif options.exc != None and options.mod == None:
                mod_list = dict(modules.Modules_List.modules_list)
                del mod_list[options.exc.lower().capitalize()]
                print("Searching on :")
                for module in mod_list:
                    print(infos.GOOD + module)
                print()

                for module in mod_list:
                    if module == "Exploitdb":
                        pass
                    else:
                        modules.Modules_List.modules_list[module](site, options.mod, options.exc)

            elif options.exc != None and options.mod != None:
                if options.exc.lower().capitalize() == "Exploitdb" and options.mod.lower().capitalize() == "Wappalyzer":
                    print("Searching on :")
                    print(infos.GOOD + "Wappalyzer")
                    print()
                    modules.Modules_List.modules_list['Wappalyzer'](site, options.mod, options.exc)
                else:
                    print(infos.ERROR + ("You can't use -m and -e at the same time with this module !\n"))
                    exit(1)

        except:
            print(infos.ERROR + "Invalid argument !\n")


if __name__ == '__main__':
    Main()

