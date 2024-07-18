import aiohttp

async def fetch_data(api_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                return await response.json()
            return None
