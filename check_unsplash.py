import urllib.request
import re

ids = [
    "1595815771614-ade9d652a65d",
    "1581793745862-99fde7fa73d2",
    "1612438214708-f428a707dd4e",
    "1518002171953-a080ee817e1f",
    "1459749411175-04bf5292ceea"
]

for img_id in ids:
    url = f"https://unsplash.com/photos/{img_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        title = re.search(r'<title>(.*?)</title>', html)
        print(f"{img_id}: {title.group(1) if title else 'No title'}")
    except Exception as e:
        print(f"{img_id}: {e}")
