FROM python:3.11-slim as base

RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN pipenv install --keep-outdated

COPY . .

RUN echo "cd /usr/src/app; pipenv run start" > /docker-entrypoint.sh; chmod +x /docker-entrypoint.sh

EXPOSE 8080
CMD ["pipenv", "run", "start"]
