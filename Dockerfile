FROM python:3.10.9-alpine3.17

RUN mkdir -p /home/app

RUN  apk update \
	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

COPY ./requirements.txt /home/app

EXPOSE 8000

RUN pip install -r requirements.txt

COPY ./ /home/app

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]