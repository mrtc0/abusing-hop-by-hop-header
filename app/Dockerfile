FROM python:3.6

COPY app/app.py /app/app.py

WORKDIR /app

RUN pip install flask
# RUN pip install -r requirements.txt

CMD ["python", "app.py"]
