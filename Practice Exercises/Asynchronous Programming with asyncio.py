import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://example.com', 'https://example.org', 'https://example.net']
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(len(result))  # Print the length of each fetched content

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
