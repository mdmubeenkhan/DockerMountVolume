FROM python
WORKDIR /app
ADD . .
CMD ["python", "./main.py"]
