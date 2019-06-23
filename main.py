import requests
import xmltodict
import sys
import Functions


from google.cloud import firestore

def save_to_db(obj):
    db = firestore.Client("futbooool-1530472667061")

    doc_reference = db.collection(u'sitemap').document()
    doc_reference.set(obj)

def get_host(url):
    return url.split("//")[1].split("/")[0]

def get_name(url):
    return url.split(".")[1]


if len(sys.argv) < 2:
    print("not enough arguments")
    exit()

sitemapurl = sys.argv[1]


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
    "host": get_host(sitemapurl),
    "name": get_name(sitemapurl),
    "size": len(list2),
    "urls": list2
}


save_to_db(obj)

print(obj)
