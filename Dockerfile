FROM registry.cn-hangzhou.aliyuncs.com/ayunw/python-basic:23-fb3bd572
LABEL author="allen_jol"

ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /data
COPY . /data

RUN chmod +x /data/start/startApp.sh \
    && mkdir -p /data/logs \
    && apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install nginx \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/* \
    && pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn \
    && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

COPY ./nginx/opssite.conf /etc/nginx

EXPOSE 8080

ENTRYPOINT ["/bin/bash", "/data/bin/startApp.sh"]
