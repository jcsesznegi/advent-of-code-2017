FROM python:3
COPY ./ /app
WORKDIR /app
CMD [ "python", "./13/part1.py" ]
