#!usr/bin/sh
echo "Packages installation: "
apt-get install python3 tor whois python-shodan
echo "Setting Python3 as default."
update-alternatives --install /usr/bin/python python /usr/bin/python3 10
echo "Dependencies installation: "
python3 -m pip install -r requirements.txt
echo "Please enter your Shodan API Key : (https://account.shodan.io)"
read shodan_apikey
sed -i "s/SHODAN_API_KEY = \"\"/SHODAN_API_KEY = \"$shodan_apikey\"/g" modules.py
echo "Starting tor service."
echo "Please enter your Wappalyzer API Key : (https://www.wappalyzer.com/apikey)"
read wappalyzer_apikey
sed -i s/\'\'/\'$wappalyzer_apikey\'/g modules.py
systemctl start tor
