from fastapi import FastAPI

import uvicorn

from math_solution import deposite_counter
from schemas import MonthDeposite, QuerySchema


app = FastAPI()


@app.post('/')
async def get_deposite(query: QuerySchema) -> list[MonthDeposite]:
    return deposite_counter(query)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
