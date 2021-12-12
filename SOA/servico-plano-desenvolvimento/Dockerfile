FROM python:3.8.5

WORKDIR /plano_desenvolvimento

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["python3", "main.py"]
