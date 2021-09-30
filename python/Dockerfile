FROM python:3

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install flask
# flask-corsのインストール（開発のみ）
RUN pip install flask-cors
RUN pip install mysqlclient

RUN mkdir -p /var
WORKDIR /var
COPY ./ /var

ENTRYPOINT ["python","hello.py"]