#!/usr/bin/python3
import time
import ramdom
with open('./star_list.txt') as f:
    star_list=f.readlines()
print(len(star_list))
import subprocess
for k,item in enumerate(star_list):
  print("{}--{}/{}".format(item,k,len(star_list)))
  subprocess.Popen('python3 render.py {}'.format(item.strip()),stdout=subprocess.PIPE,shell=True)
  time.sleep(radom.randint(1,30))
