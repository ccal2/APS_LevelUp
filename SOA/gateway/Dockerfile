FROM python:3.8.5

WORKDIR /gateway

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "main.py"]
