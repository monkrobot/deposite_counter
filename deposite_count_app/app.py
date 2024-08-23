from decimal import Decimal

from fastapi import FastAPI
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import uvicorn

from deposite_counter import deposite_counter
from schemas import QuerySchema


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        error.pop("type")
        error.pop("input")
        error.pop("ctx")
        error["error"] = f"{error.pop('loc')[1]}: {error.pop('msg')}"

    return JSONResponse(
        content=jsonable_encoder({"detail": exc.errors()}), status_code=status.HTTP_400_BAD_REQUEST
    )


@app.post("/")
async def get_deposite(query: QuerySchema) -> dict[str, Decimal]:
    return deposite_counter(query)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
