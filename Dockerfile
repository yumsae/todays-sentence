FROM python:3.9.0

WORKDIR /home/

RUN echo "wb07"

RUN git clone https://github.com/ssorn88/todays-sentence.git

WORKDIR /home/todays-sentence/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=today.settings.deploy && python manage.py migrate --settings=today.settings.deploy && gunicorn today.wsgi --env DJANGO_SETTINGS_MODULE=today.settings.deploy --bind 0.0.0.0:8000"]