FROM python:3.10

ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

USER prj

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
