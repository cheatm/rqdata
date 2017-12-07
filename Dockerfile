FROM registry.docker-cn.com/continuumio/miniconda3

ENV BUNDLE_DIR="/data" PYTHONPATH="/rqdata"
VOLUME /data /radata

ADD ./rqdata.yml /rqdata.yml
RUN conda env update -f=/rqdata.yml & conda clean --all -y

RUN apt-get update
RUN apt-get install -y locales cron

RUN echo 'Asia/Shanghai' >/etc/timezone & cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen & locale-gen

