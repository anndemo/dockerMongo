FROM python

WORKDIR /app

COPY . .

VOLUME ["/app/data"]

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]