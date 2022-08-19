FROM python:3.9.0

WORKDIR /home/

RUN echo wb01

RUN git clone gh repo clone yumsae/todays-sentence

WORKDIR /home/todays-sentence/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=/todays-sentence/.settings.deploy && python manage.py migrate --settings=/todays-sentence/.settings.deploy && gunicorn /todays-sentence/.wsgi --env DJANGO_SETTINGS_MODULE=/todays-sentence/.settings.deploy --bind 0.0.0.0:8000"]