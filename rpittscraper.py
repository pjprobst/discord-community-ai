CLIENT_ID = 'LyUjP3-7l6r2v4PBmwRxiA'
SECRET_KEY = 'NqVqFd2rKqFofUyyT9ld1_hCPNZWzA'
import requests
import time
import datetime
import json
import glob
import os
import re
four_years_ago = time.time() - 5*365*24*60*60
duplicates = 0
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {
    'grant_type' : 'password',
    'username' : 'Alarmed-Phase3009',
    'password' : 'Lions2006!'
}
headers = {'User-Agent' : 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'
all_posts = []
after = None
filename = "rpitt_query_2.jsonl"
existing_ids = set()
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
                if "id" in obj:
                    existing_ids.add(obj["id"])
            except:
                continue
def get_comments(subreddit, post_id, limit=500):
    url = f"https://oauth.reddit.com/r/{subreddit}/comments/{post_id}"
    res = requests.get(url, headers=headers, params={"limit": limit})
    data = res.json()
    comments = data[1]['data']['children']
    return comments
with open("rpitt_query_2.jsonl", "a", encoding="utf-8") as out_file:
    while True:
        # computer science
        # data science
        # information science
        # infsci
        # Digital Narrative and Interactive Design
        # DNID
        # SCI
        # cs
        # comp sci
        # computational biology
        # Computational Social Science
        # java
        # CMPINF
        # Physics and Quantum Computing
        # Software Engineering
        # School of Computing and Information
        params = {'q': '"School of Computing and Information"',
                  "restrict_sr": True,
                  'limit': 100,
                  'sort': 'new',
                  'after': after}
        print(params['q'])
        res = requests.get('https://oauth.reddit.com/r/pitt/search/', headers=headers, params=params)
        data = res.json()['data']
        for post in data['children']:
            created = post['data']['created_utc']
            if created >= four_years_ago:
                all_posts.append(post)

        after = data.get('after')
        if not after:
            print(len(all_posts))
            break
    for post in all_posts:
         post_id = post['data']['id']
         if post_id in existing_ids:
            duplicates += 1
            continue
         post_data= {
            "id": post['data']['id'],
            "question": post['data']['title'],
            "context": post['data']['selftext'],
            "answers": []
        }
         comments = get_comments(post['data']['subreddit'], post_id)

         for c in comments:
            if c['kind'] == 't1':
                post_data["answers"].append(c['data']['body'])
         with open(filename, "a", encoding="utf-8") as out_file:
            out_file.write(json.dumps(post_data, ensure_ascii=False) + "\n")
         existing_ids.add(post_id)
print("done!")
print(duplicates, "duplicates found!")


    
