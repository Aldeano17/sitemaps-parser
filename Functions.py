from google.cloud import firestore

def save_to_db(obj):
    db = firestore.Client("futbooool-1530472667061")

    doc_reference = db.collection(u'sitemap').document()
    doc_reference.set(obj)

def get_host(url):
    return url.split("//")[1].split("/")[0]

def get_name(url):
    return url.split(".")[1]
