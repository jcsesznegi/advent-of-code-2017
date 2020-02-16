FROM python:3
COPY ./ /app
WORKDIR /app
CMD [ "python", "./9/part2.py" ]
