FROM python:3

# setup basics
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# setup server
EXPOSE 8080
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0:8080"]
