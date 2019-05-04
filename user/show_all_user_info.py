# -*- coding:utf-8 -*-  
import json

f = file("/usr/local/shadowsocksr/mudb.json");

json = json.load(f);

print "用户名\t\t端口\t\t加密方式\t\t密码"

for x in json:
  print "%s\t\t%s\t\t%s\t\t%s" %(x[u"user"],x[u"port"],x[u"method"],x[u"passwd"])
f.close();

