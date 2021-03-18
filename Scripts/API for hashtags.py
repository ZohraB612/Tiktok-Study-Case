import os
import json
import re
import pandas as pd
import requests
import math
import ast

df = pd.read_csv("/Users/princessspotty/Desktop/tiktokdata_missingmusichashtag.csv")

if "hashtag_data" not in df.columns:
    df["hashtag_data"] = ""


df.to_csv(".../tiktokdata_missingmusichashtag.csv", index = False)

headers = {
    'x-rapidapi-key': "9eb90dd9e4mshbcb1271b027f0ecp18cb50jsn04e5bb1cda23",
    'x-rapidapi-host': "tiktok.p.rapidapi.com"
}

url = "https://tiktok.p.rapidapi.com/live/hashtag/v2"

for row in range(1600,1628):
    print(row)

    # if isinstance(df["country"][row], float) and not math.isnan(df["country"][row]):
    #     print("here")
    #     continue

    hashtag = df["hashtags"][row]
    # print(hashtag)

    hashtag = hashtag[2:-1]

    hashtags = hashtag.split(",{")

    final_hashtags= []
    for hasht in hashtags:
        hashtag_data = {}
        hasht = "{"+hasht
        if hasht.startswith("{") and hasht.endswith("}"):
            h = ast.literal_eval(hasht)
            hashtag_data['name'] = h['name']
            querystring = {"hashtag":h['name']}

            response = requests.request("GET", url, headers=headers, params=querystring)

            hash_dict = json.loads(response.text)

            if 'stats' in hash_dict.keys():
                stats = hash_dict['stats']
                hashtag_data['posts'] = stats['videoCount']
                hashtag_data['views'] = stats['viewCount']
        final_hashtags.append(hashtag_data)
    
    hash_data_string = json.dumps(final_hashtags)
    print(hash_data_string)
    df["hashtag_data"][row] = hash_data_string

    if row % 5 == 0:
        df.to_csv(".../tiktokdata_missingmusichashtag.csv", index=False)

    
   
