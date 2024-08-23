import asyncio


from httpx import AsyncClient
import pytest

from deposite_count_app.app import app as fastapi_app


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
