#-*-coding:utf-8-*-
import os
import wget
import time
print("部署Nginx测试脚本（Python版）")
time.sleep(1)
print("请选择安装方式\n1.Yum快速安装\n2.编译安装")
time.sleep(2)
cn = input("请输入数字选择安装方式:")
if cn != "1" and cn != "2":
    print("请输入正确的数字")
    cn
if cn == "1":
    print("开始Yum安装，开始获取Nginx安装包")
    cmd = os.popen('rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm')
    print(cmd.read())
    print("开始安装Nginx")
    time.sleep(1)
    ccd = os.popen('yum -y install nginx')
    print(ccd.read())
    cbd = os.popen('service nginx start')
    print(cbd.read())
    cfd = os.popen('netstat -nltp | grep nginx')
    print(cfd.read())
elif cn == "2":
    print("开始编译安装，开始下载tar文件版本:1.14.2")
    url = 'http://nginx.org/download/nginx-1.14.2.tar.gz'
    wget.download(url)
    print("开始编译安装...")
    time.sleep(1)
    os.system('cp ./nginx-1.14.2.tar.gz /usr/src')
    os.system('cd /usr/src')
    os.system('tar xf ./nginx-1.14.2.tar.gz')
    os.system('cd ./nginx-1.14.2')
    bu = os.popen('./configure --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --with-stream')
    print(bu.read())
    be = os.popen('make && make install')
    print(be.read())
    os.system("/usr/local/nginx/sbin/nginx")
    os.system("netstat -nltp | grep 80")
    print("编译安装完成")


