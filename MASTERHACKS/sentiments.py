import requests
# pprint is used to format the JSON response
from pprint import pprint
import os
import hashlib
import random
import pandas as pd

_axxx= "es"

subscription_key = "10ed6ba7b3d4497096beabf32a4c9d39"
endpoint = "https://nrrecluters.cognitiveservices.azure.com/"
keyphrases_url = endpoint + "/text/analytics/v3.0/keyphrases"

documents2 = {"documents": [
    {"id": "1", "language": _axxx,
        "text": "Bien vestido, con mucho flow. Buen manejo del ingles y el frances. malos conocimientos técnicos y básicos" }
    ]}
headers2 = {"Ocp-Apim-Subscription-Key": subscription_key}
response2 = requests.post(keyphrases_url, headers=headers2, json=documents2)
key2 = response2.json()
pprint(key2 )
wa= key2['documents'][0]['keyPhrases']
print(wa)

s="'"
r=""
q="["
qq="]"
was=str(wa)
texto=was.replace(s,r)
wal=texto.replace(q,r)
w=wal.replace(qq,r)
print(w)

