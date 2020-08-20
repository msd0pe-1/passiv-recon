<a target="_blank" href="https://img.shields.io/badge/platform-linux-success.svg" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-linux-success.svg">
</a>
<a target="_blank" href="https://img.shields.io/badge/version-1.0-yellow" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/version-1.0-yellow">
</a>
<a href="https://www.python.org/" rel="nofollow">
    <img src="https://img.shields.io/badge/python-3.7-red">
</a>
<a href="https://github.com/msd0pe-1/cve-maker-master/blob/master/LICENSE" rel="nofollow">
    <img src="https://img.shields.io/badge/license-GPLv3-9cf.svg">
</a>
<h1>PASSIV-RECON</h1>

Use this software <strong>only for legal purposes</strong>.<br />
I am in no way responsible for your actions.<br />
Use python 3.7<br />
<strong>Made by msd0pe</strong><br />

<h2>WHAT IS IT ?</h2>

Passiv-Recon is a tool for making the environment of a target passively.<br />
It uses third party sites to collect information.
It is intended to save you time.

<h2>HOW IT WORKS ?</h2>

Passiv-Recon will use the APIs of different sites in order to return the public information on a given site.<br />
The tool allows you to add your own detection modules to get more information about a target..<br /><br />

<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/86165478-a24dc580-bb13-11ea-90f3-43d25fedb9b9.gif">
</p>

<h2>INSTALLATION</h2>
Download the project:
<code>git clone https://github.com/msd0pe-1/passiv-recon</code><br />
You only need to execute install.sh to get the libraries useful to the program : <code>sh install.sh</code><br />
Specify your shodan & wappalyzer api key during installation or add it later in the modules.py file.<br />

<h2>USAGE</h2>
<pre>
    <code>
Usage: python passiv-recon.py [options] url

Options:
  --version          show program's version number and exit
  -h, --help         show this help message and exit
  -m MOD, --mod=MOD  execute only one module
  -e EXC, --exc=EXC  exclude one module of the execution list

  Available Modules:
    Whois Shodan Wappalyzer Exploitdb

  Examples:
    python passiv-recon.py https://www.google.com
    python passiv-recon.py -m Shodan  https://www.google.com
    python passiv-recon.py -e Wappalyzer https://google.com

  Tool for making the environment of a target passively.
  Source code put in public domain by msd0pe,no Copyright
  Any malicious or illegal activity may be punishable by law
  Use at your own risk
    </code>
</pre>

<h2>CONTRIBUTING</h2>

This project is in active development. Feel free to suggest a new feature/module or open a pull request !
