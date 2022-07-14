# gen_random_pwd_dj3
---
[![OSCS Status](https://www.oscs1024.com/platform/badge/allenjol/gen_random_passwd_dj.svg?size=small)](https://www.oscs1024.com/project/allenjol/gen_random_passwd_dj?ref=badge_small)

django 3.2 随机密码生成器

### 构建镜像
```shell
docker build -t your-image:tag -f ./Dockerfile .
```

### docker-compose 启动服务
```shell
sed -i 's@yourImageName@your-image:tag@' docker-compose/docker-compose.yml
cd docker-compose
docker-compose up -d
```
