FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

RUN apk --no-cache --update add --virtual .build-deps \
    gcc musl-dev postgresql-dev &&
    apk --no-cache --update add libpq &&
    pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements-pgsql.txt
RUN apk del --no-cache --purge .build-deps &&
    apk del --purge &&
    rm -rf /var/cache/apk/* requirements*.txt

CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
