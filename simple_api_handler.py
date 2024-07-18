# simple_api_handler.py

import aiohttp

async def fetch_data():
    url = 'https://api.example.com/data'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None
