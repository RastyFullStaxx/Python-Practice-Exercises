# Implement a function to parse a URL and extract its components.
from urllib.parse import urlparse

def parse_url(url):
    parsed_url = urlparse(url)
    return {
        "scheme": parsed_url.scheme,
        "netloc": parsed_url.netloc,
        "path": parsed_url.path,
        "params": parsed_url.params,
        "query": parsed_url.query,
        "fragment": parsed_url.fragment
    }

url = "https://www.example.com/path?param1=value1&param2=value2"
parsed_info = parse_url(url)
print(parsed_info)
