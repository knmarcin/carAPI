FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/knmarcin/CarAPI.git /CarAPI

WORKDIR /CarAPI

RUN pip install -r requirements.txt

VOLUME CarAPI

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000