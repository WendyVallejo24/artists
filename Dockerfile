FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /artists
WORKDIR /artists
COPY requirements.txt /artists/
RUN pip install -r requirements.txt
COPY . /artists/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080