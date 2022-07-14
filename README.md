# gen_random_pwd_dj3
---
[![OSCS Status](https://www.oscs1024.com/platform/badge/allenjol/gen_random_passwd_dj.svg?size=small)](https://www.oscs1024.com/project/allenjol/gen_random_passwd_dj?ref=badge_small)

django 3.2 随机密码生成器

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
