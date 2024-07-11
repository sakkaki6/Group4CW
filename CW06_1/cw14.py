from urllib.parse import urlparse


class URLHandler:
    @classmethod
    def parse_url(cls, url):
        parsed_url = urlparse(url)
        return {
            "protocol": parsed_url.scheme,
            "domain": parsed_url.netloc,
            "path": parsed_url.path,
            "query": parsed_url.query,
            "fragment": parsed_url.fragment
        }


url = "https://lms.maktabsharif.ir/mod/folder/view.php?id=6226#test"
components = URLHandler.parse_url(url)
print(components)
