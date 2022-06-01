#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import csv
import sys

csv_fn = "../data/vscode-ext.lst"
with open(csv_fn, newline="") as fh:
    csv_iter = csv.reader(fh)  # delimiter=';', quotechar='"'))
    for item in csv_iter:
        ext_id = item[0]
        # print(f"-=[ {ext_id}")
        url = f"https://marketplace.visualstudio.com/items?itemName={ext_id}"
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            title_a = soup.find_all("title")
            if len(title_a) > 0:
                val: str = title_a[0].decode_contents()
                val = val.strip()
                print(f"{val}\t{ext_id}\t{url}")
            else:
                print(title_a,file=sys.stderr)
        else:
            print(f"error: {ext_id} {url} : {resp.status_code}", file=sys.stderr)
    data = list(csv_iter)

print(data)
