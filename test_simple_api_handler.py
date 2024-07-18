# test_simple_api_handler.py

import pytest
from aioresponses import aioresponses
from simple_api_handler import fetch_data

@pytest.mark.asyncio
async def test_fetch_data_success():
    with aioresponses() as m:
        url = 'https://api.example.com/data'
        m.get(url, payload={'key': 'value'})

        result = await fetch_data()
        assert result == {'key': 'value'}

@pytest.mark.asyncio
async def test_fetch_data_failure():
    with aioresponses() as m:
        url = 'https://api.example.com/data'
        m.get(url, status=404)

        result = await fetch_data()
        assert result is None
