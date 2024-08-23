from decimal import Decimal
from typing import Any
import pytest

from deposite_count_app.deposite_counter import deposite_counter
from deposite_count_app.schemas import QuerySchema


@pytest.mark.parametrize(
    "date, periods, amount, rate, res",
    [
        (
            "31.01.2021",
            2,
            10000,
            6.0,
            {"31.01.2021": Decimal("10050.00"), "28.02.2021": Decimal("10100.25")},
        ),
        (
            "31.01.2020",
            5,
            100000,
            6.0,
            {
                "31.01.2020": Decimal("100500.00"),
                "29.02.2020": Decimal("101002.50"),
                "31.03.2020": Decimal("101507.51"),
                "30.04.2020": Decimal("102015.05"),
                "31.05.2020": Decimal("102525.13"),
            },
        ),
    ],
)
async def test_get_deposite(
    date: str,
    periods: int,
    amount: int,
    rate: float,
    res: dict[str, str],
):
    query = QuerySchema(
        date=date,
        periods=periods,
        amount=amount,
        rate=rate,
    )
    result = deposite_counter(query)
    assert res == result


@pytest.mark.parametrize(
    "data",
    [
        ("some_string"),
        ({"amount": 10000, "periods": 7, "rate": 6.0, "date": "31.01.2021"}),
    ],
)
async def test_get_deposite_wrong_data(
    data: Any,
):
    with pytest.raises(AttributeError):
        deposite_counter(data)
