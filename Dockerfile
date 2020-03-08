FROM python:3
COPY ./ /app
WORKDIR /app
CMD [ "python", "./11/part1.py" ]
