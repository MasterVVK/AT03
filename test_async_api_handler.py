import pytest
from aiohttp import ClientSession
from aioresponses import aioresponses
from async_api_handler import fetch_data


@pytest.mark.asyncio
async def test_fetch_data_success():
    api_url = "https://api.example.com/data"

    with aioresponses() as m:
        m.get(api_url, payload=[{"id": 1, "name": "Test"}])

        result = await fetch_data(api_url)
        assert result == [{"id": 1, "name": "Test"}]


@pytest.mark.asyncio
async def test_fetch_data_failure():
    api_url = "https://api.example.com/data"

    with aioresponses() as m:
        m.get(api_url, status=404)

        result = await fetch_data(api_url)
        assert result is None
