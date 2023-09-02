import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com", "https://openai.com", "https://python.org"]

    tasks = [fetch_url(url) for url in urls]
    pages = await asyncio.gather(*tasks)

    for i, page in enumerate(pages):
        print(f"Page {i+1} content length: {len(page)}")

if __name__ == "__main__":
    asyncio.run(main())
