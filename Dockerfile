FROM python:3
COPY ./ /app
WORKDIR /app
CMD [ "python", "./10/part1.py" ]
