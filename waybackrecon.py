import requests
import sys
import json

class WaybackMachine:

    def __init__(self, domain):
        self.domain = domain
        self.wayback_url = f"https://web.archive.org/cdx/search?url={domain}%2F&matchType=prefix&collapse=urlkey&output=json&fl=original%2Cmimetype%2Ctimestamp%2Cendtimestamp%2Cgroupcount%2Cuniqcount&filter=!statuscode%3A%5B45%5D..&limit=100000"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
        }

    def get_urls(self):
        try:
            response = requests.get(self.wayback_url, headers=self.headers)
            response.raise_for_status()
            return json.loads(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Wayback Machine: {e}")
            return []

def main():
    if len(sys.argv) != 2:
        print("Usage: python waybackrecon.py <target.com>")
        sys.exit(1)

    domain = sys.argv[1]
    wbm = WaybackMachine(domain)
    urls = wbm.get_urls()

    if urls:
        for row in urls:
            print(row[0])
    else:
        print(f"No URLs found for domain: {domain}")

if __name__ == "__main__":
    main()
