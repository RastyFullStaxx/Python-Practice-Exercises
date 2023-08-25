import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

for post in posts:
    print(f"Post ID: {post['id']}")
    print(f"Title: {post['title']}")
    print("-" * 30)
