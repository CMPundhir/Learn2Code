'''
Q. What is JSON?
And. 1. JSON stands for JavaScript Object Notation
	2. JSON is a lightweight format for storing and transporting data
	3. JSON is often used when data is sent from a server to a web page
	4. JSON is "self-describing" and easy to understand


{
  "login": "CMPundhir",
  "id": 26346858,
  "node_id": "MDQ6VXNlcjI2MzQ2ODU4",
  "avatar_url": "https://avatars.githubusercontent.com/u/26346858?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/CMPundhir",
  "html_url": "https://github.com/CMPundhir",
  "followers_url": "https://api.github.com/users/CMPundhir/followers",
  "following_url": "https://api.github.com/users/CMPundhir/following{/other_user}",
  "gists_url": "https://api.github.com/users/CMPundhir/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/CMPundhir/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/CMPundhir/subscriptions",
  "organizations_url": "https://api.github.com/users/CMPundhir/orgs",
  "repos_url": "https://api.github.com/users/CMPundhir/repos",
  "events_url": "https://api.github.com/users/CMPundhir/events{/privacy}",
  "received_events_url": "https://api.github.com/users/CMPundhir/received_events",
  "type": "User",
  "site_admin": false,
  "name": "CM Pundhir",
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": "I am a coder and I love coding. I had an experience of 5+ years as a developer. As a trainer, I trained 500+ programming enthusiast. I always keep myself up",
  "twitter_username": null,
  "public_repos": 58,
  "public_gists": 1,
  "followers": 52,
  "following": 2,
  "created_at": "2017-03-11T14:56:29Z",
  "updated_at": "2021-07-15T13:40:24Z"
}

'''

import json


str = '''{
  "login": "CMPundhir",
  "id": 26346858,
  "node_id": "MDQ6VXNlcjI2MzQ2ODU4",
  "avatar_url": "https://avatars.githubusercontent.com/u/26346858?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/CMPundhir",
  "html_url": "https://github.com/CMPundhir",
  "followers_url": "https://api.github.com/users/CMPundhir/followers",
  "following_url": "https://api.github.com/users/CMPundhir/following{/other_user}",
  "gists_url": "https://api.github.com/users/CMPundhir/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/CMPundhir/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/CMPundhir/subscriptions",
  "organizations_url": "https://api.github.com/users/CMPundhir/orgs",
  "repos_url": "https://api.github.com/users/CMPundhir/repos",
  "events_url": "https://api.github.com/users/CMPundhir/events{/privacy}",
  "received_events_url": "https://api.github.com/users/CMPundhir/received_events",
  "type": "User",
  "site_admin": false,
  "name": "CM Pundhir",
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": "I am a coder and I love coding. I had an experience of 5+ years as a developer. As a trainer, I trained 500+ programming enthusiast. I always keep myself up",
  "twitter_username": null,
  "public_repos": 58,
  "public_gists": 1,
  "followers": 52,
  "following": 2,
  "created_at": "2017-03-11T14:56:29Z",
  "updated_at": "2021-07-15T13:40:24Z"
}'''


#print(str)

jsonObj = json.loads(str)

print(jsonObj['type'])
print(jsonObj['bio'])



