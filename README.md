### With the help of existing openLDAP：jermine/openldap ###

run:<br>
docker run -it --rm --name openldap \ <br>
          -p 389:389 \ <br>
          -e DEBUG_LEVEL=1 \<br>
          -e DOMAIN=my-company.com \<br>
          -e ORGANIZATION="My Company" \ <br>
          -e PASSWORD=1234567890 \<br>
         jermine/openldap <br>
### Installing python images ###

** Build a complete python environment in ubuntu：**<br>
 docker pull ubuntu<br>
 docker run -i -t ubuntu /bin/bash <br>
 apt-get update <br>
 apt-get install python3<br>
 输入python3试一下<br>
 apt-get install python3-pip(这个命令好像会同时安装python2.7)<br>
 输入pip试一下<br>
 apt-get install python3-dev<br>
 apt-get install openssl<br>
 apt-get install libssl-dev<br>
 apt-get install libffi-dev<br>
 
** 打包装了python的容器: ** <br>
 docker commit  <容器id>  docker/python3env <br>
 
** 进入容器互动： ** <br>
 docker run -it python:3.7 打开容器<br>

** 完成认证 **<br>
 docker run -v /c/Users/qtt/py:/py -w /py docker/python3env python3 hello.py 