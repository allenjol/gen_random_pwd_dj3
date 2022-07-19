<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [django 3.2 随机密码生成器](#django-32-%E9%9A%8F%E6%9C%BA%E5%AF%86%E7%A0%81%E7%94%9F%E6%88%90%E5%99%A8)
    - [构建镜像](#%E6%9E%84%E5%BB%BA%E9%95%9C%E5%83%8F)
    - [docker 命令行启动服务](#docker-%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%90%AF%E5%8A%A8%E6%9C%8D%E5%8A%A1)
    - [docker-compose 启动服务](#docker-compose-%E5%90%AF%E5%8A%A8%E6%9C%8D%E5%8A%A1)
    - [kubernetes 运行服务](#kubernetes-%E8%BF%90%E8%A1%8C%E6%9C%8D%E5%8A%A1)
    - [值得参考的别人的项目](#%E5%80%BC%E5%BE%97%E5%8F%82%E8%80%83%E7%9A%84%E5%88%AB%E4%BA%BA%E7%9A%84%E9%A1%B9%E7%9B%AE)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# django 3.2 随机密码生成器

[![OSCS Status](https://www.oscs1024.com/platform/badge/allenjol/gen_random_passwd_dj.svg?size=small)](https://www.oscs1024.com/project/allenjol/gen_random_passwd_dj?ref=badge_small)
[![CI](https://github.com/allenjol/gen_random_pwd_dj3/actions/workflows/docker-image.yml/badge.svg?branch=master)](https://github.com/allenjol/gen_random_pwd_dj3/actions/workflows/docker-image.yml)



### 构建镜像
```shell
docker build -t your-image:tag -f ./Dockerfile .
```

### docker 命令行启动服务
```shell
docker run -itd --name django3-genPasswd -p youPort:8080 your-image:tag
```

### docker-compose 启动服务
```shell
sed -i 's@yourImageName@your-image:tag@' docker-compose/docker-compose.yml
cd docker-compose
docker-compose up -d
```

### kubernetes 运行服务

这里用ingress来演示

```shell
cd kubernetes-deploy
# 更新你的镜像后执行以下命令
kubectl apply -f .
```

### 值得参考的别人的项目
```consle
https://github.com/liangliangyy/DjangoBlog/blob/master/djangoblog/settings.py
```
