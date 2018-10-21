

### With the help of existing openLDAP：jermine/openldap ###

run:
- docker run -it --rm --name openldap `\` 
-          -p 389:389 `\`
-          -e DEBUG_LEVEL=1 `\` 
-          -e DOMAIN=my-company.com `\`
-          -e ORGANIZATION="My Company" `\`
-          -e PASSWORD=1234567890 `\`
-          jermine/openldap
### Installing python images ###

** Build a complete python environment in ubuntu：**
- docker pull ubuntu
- docker run -i -t ubuntu /bin/bash 
- apt-get update 
- apt-get install python3
- 输入python3试一下
- apt-get install python3-pip(这个命令好像会同时安装python2.7)
- 输入pip试一下
- apt-get install python3-dev
- apt-get install openssl
- apt-get install libssl-dev
- apt-get install libffi-dev
** 打包装了python的容器: ** 
- docker commit  <容器id>  docker/python3env 
** 进入容器互动： ** 
- docker run -it python:3.7 打开容器

** 完成认证 **
- docker run -v /c/Users/qtt/py:/py -w /py docker/python3env python3 hello.py 