import requests

url = "https://jsonplaceholder.typicode.com/posts/5"

response = requests.get(url)
data = response.json()

for user in data:
    print(f"Post ID: {user['id']} - Title: {user['title']}")