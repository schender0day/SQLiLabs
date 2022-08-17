import requests
import urllib3
import re
from bs4 import BeautifulSoup
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'https':'https://127.0.0.1:8080'}


def sqli_password(url):




def main():
    if len(sys.argv) != 2:
        print(f"[+] Usage: {sys.argv[0]}")
        print(f"[+] Example: {sys.argv[0]} www.example.com")

        url = sys.argv[1]
        print(f"[+] Retrieving administrator passowrd...")

        sqli_password(url)
if __name__ == "__main__":
    main()