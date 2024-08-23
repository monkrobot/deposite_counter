from httpx import AsyncClient
import pytest


@pytest.mark.parametrize("date, periods, amount, rate, status_code, result", [
    (
        "31.01.2021", 2, 10000, 6.0, 200,
        {
            "31.01.2021": "10050.00",
            "28.02.2021": "10100.25"
        }
    ),
    (
        "31-01-2021", 2, 10000, 6, 400,
        {
            "detail": [
                {
                "error": "date: Value error, time data '31-01-2021' does not match format '%d.%m.%Y'"
                }
            ]
        }
    ),
    (
        "31.01.2021", 100, 10000, 6, 400,
        {
            "detail": [
                {
                "error": "periods: Input should be less than or equal to 60"
                }
            ]
        }
    ),
    (
        "31.01.2021", 2, 100, 6, 400,
        {
            "detail": [
                {
                "error": "amount: Input should be greater than or equal to 10000"
                }
            ]
        }
    ),
    (
        "31.01.2021", 2, 10000, 66, 400,
        {
            "detail": [
                {
                "error": "rate: Input should be less than or equal to 8"
                }
            ]
        }
    ),
    (
        "31-01-2021", 100, 100, 66, 400,
        {
            "detail": [
                {
                "error": "date: Value error, time data '31-01-2021' does not match format '%d.%m.%Y'"
                },
                {
                "error": "periods: Input should be less than or equal to 60"
                },
                {
                "error": "amount: Input should be greater than or equal to 10000"
                },
                {
                "error": "rate: Input should be less than or equal to 8"
                }
            ]
        }
    ),
],)
async def test_get_deposite(
    date: str,
    periods: int,
    amount: int,
    rate: float,
    status_code: int,
    result: dict[str, str | list[dict[str, str]]],
    ac: AsyncClient,
):
    response = await ac.post(url="/", json={
        "date": date,
        "periods": periods,
        "amount": amount,
        "rate": rate,
    })

    assert response.status_code == status_code

    assert response.json() == result
