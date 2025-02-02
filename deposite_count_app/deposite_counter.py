from decimal import Decimal
from dateutil.relativedelta import relativedelta

from schemas import QuerySchema


def deposite_counter(query: QuerySchema) -> dict[str, Decimal]:
    result = dict()
    last_month_amount = query.amount
    last_date = query.date

    for period_item in range(1, query.periods + 1):
        if period_item == 1:
            deposite_date = last_date
        else:
            deposite_date = last_date + relativedelta(months=period_item - 1)

        last_month_amount = last_month_amount * (1 + query.rate / 12 / 100)
        deposite_amount = Decimal(str(last_month_amount)).quantize(Decimal("1.00"))
        result[deposite_date.strftime("%d.%m.%Y")] = deposite_amount

    return result


if __name__ == "__main__":
    amount = 10000
    periods = 7
    rate = 6.0
    date = "31.01.2021"

    query = QuerySchema(date=date, rate=rate, periods=periods, amount=amount)

    print(deposite_counter(query))
