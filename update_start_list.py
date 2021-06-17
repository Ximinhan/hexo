#!/usr/bin/python3
import time
with open('./star_list.txt') as f:
    star_list=f.readlines()
print(star_list[0].strip())
import subprocess
for item in star_list:
  print(item)
  subprocess.Popen('python3 render.py {}'.format(item.strip()),stdout=subprocess.PIPE,shell=True)
  time.sleep(30)
