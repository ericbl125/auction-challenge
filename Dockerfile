FROM python:3.8


COPY . .

CMD ["python", "-m", "auction.py"]