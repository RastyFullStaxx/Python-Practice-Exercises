import asyncio
import aiohttp

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["http://example.com", "http://google.com", "http://python.org"]
    tasks = [fetch_page(url) for url in urls]
    pages = await asyncio.gather(*tasks)
    for url, page in zip(urls, pages):
        print(f"URL: {url}, Length: {len(page)}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
