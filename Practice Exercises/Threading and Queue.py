import threading
import requests
import queue

def download_image(url, filename, q):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    q.put(filename)

def main():
    urls = ['url1.jpg', 'url2.jpg', 'url3.jpg']
    q = queue.Queue()
    threads = []

    for i, url in enumerate(urls):
        filename = f'image_{i}.jpg'
        thread = threading.Thread(target=download_image, args=(url, filename, q))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    while not q.empty():
        print(f"Downloaded: {q.get()}")

if __name__ == '__main__':
    main()
