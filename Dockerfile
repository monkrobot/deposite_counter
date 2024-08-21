FROM python:3.11

RUN mkdir /deposite_count_app

WORKDIR /deposite_count_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY deposite_count_app .

CMD ["gunicorn", "app:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]