FROM python:3
COPY ./ /app

RUN pip install pytest

ENV AC_2017_PATH /app
ENV AC_2017_DAY 18
ENV AC_2017_PART 2

WORKDIR $AC_2017_PATH/$AC_2017_DAY

# CMD pytest
CMD python ./part$AC_2017_PART.py
# CMD pytest && python ./part$AC_2017_PART.py
