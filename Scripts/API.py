import os
import json
import re
import pandas as pd
import requests
import math

df = pd.read_csv(".../tiktokdata.csv")

if "follower_count" not in df.columns:
    df["follower_count"] = ""

if "following_count" not in df.columns:
    df["following_count"] = ""

if "video_count" not in df.columns:
    df["video_count"] = ""

if "verification_type" not in df.columns:
    df["verification_type"] = ""

if "total_favorited" not in df.columns:
    df["total_favorited"] = ""

if "country" not in df.columns:
    df["country"] = ""


df.to_csv(".../tiktokdata.csv", index = False)


headers = {
    'x-rapidapi-key': "9eb90dd9e4mshbcb1271b027f0ecp18cb50jsn04e5bb1cda23",
    'x-rapidapi-host': "tiktok.p.rapidapi.com"
}

for row in range(1999,2082):
    print(row)

    if isinstance(df["country"][row], float) and not math.isnan(df["country"][row]):
        print("here")
        continue

    username = df["authorMeta.name"][row]
    url = "https://tiktok.p.rapidapi.com/live/user"

    querystring = {"username":username}

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    person_dict = json.loads(response.text)
    
    if "follower_count" in person_dict.keys():
        df["follower_count"][row] = person_dict["follower_count"]
    if "following_count" in person_dict.keys():
        df["following_count"][row] = person_dict["following_count"]
    if "total_favorited" in person_dict.keys():
        df["total_favorited"][row] = person_dict["total_favorited"]
    if "video_count" in person_dict.keys():
        df["video_count"][row] = person_dict["video_count"]
    if "verification_type" in person_dict.keys():
        df["verification_type"][row] = person_dict["verification_type"]
    if "country" in person_dict.keys():
        df["country"][row] = person_dict["country"]

    if row % 10 == 0:
        df.to_csv(".../tiktokdata.csv", index=False)





# obj = json.loads(output)

# print (obj)
