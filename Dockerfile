FROM python:3
COPY ./ /app
WORKDIR /app
CMD [ "python", "./12/part2.py" ]
