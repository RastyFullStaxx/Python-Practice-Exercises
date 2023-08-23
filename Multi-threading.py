import threading
import requests

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {filename}")

urls = [
    ('https://example.com/image1.jpg', 'image1.jpg'),
    ('https://example.com/image2.jpg', 'image2.jpg'),
    ('https://example.com/image3.jpg', 'image3.jpg')
]

threads = []
for url, filename in urls:
    thread = threading.Thread(target=download_image, args=(url, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All downloads completed")
