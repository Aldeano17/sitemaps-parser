import requests
import xmltodict
import Functions


class SitemapParser:
    def __init__(self, urls):
        self.urls = urls


    def load(self):
        for url in self.urls:
            sitemapurl = url

            response = requests.get(sitemapurl)
            list = xmltodict.parse(response.text)

            list2 = []
            for e in list["urlset"]["url"]:
                obj = {
                    "url": e["loc"],
                    "udpated": e["lastmod"]
                }

                list2.append(obj)
                break

            obj = {
                "host": Functions.get_host(sitemapurl),
                "name": Functions.get_name(sitemapurl),
                "size": len(list2),
                "urls": list2
            }


            Functions.save_to_db(obj)

            print(obj)

listStrings = [
    "https://www.walmart.com/sitemap_tp1.xml",
    "https://www.walmart.com/sitemap_bp1_https.xml"
]
parser = SitemapParser(listStrings)