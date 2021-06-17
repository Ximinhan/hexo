#!/usr/bin/python3
import jinja2.defaults as defaults
#import jinja2
import os
import sys
import time
import subprocess
from jinja2.environment import Environment, Template
from jinja2.loaders import FileSystemLoader
#print(Environment.BLOCK_START_STRING)

env = Environment(
        block_start_string = '((*',
        block_end_string = '*))',
        loader=FileSystemLoader('./')
        )
temp = env.get_template('template.md')



dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
p = subprocess.Popen('sh create_data.sh {}'.format(sys.argv[1]),stdout=subprocess.PIPE,shell=True)
vl = p.stdout.readlines()
vl2 = []
for line in vl:
  vl2.append(line.decode().strip())

ll2 = []
p = subprocess.Popen('sh create_line.sh {}'.format(sys.argv[1]),stdout=subprocess.PIPE,shell=True)
for line in p.stdout.readlines():
    ll2.append(line.decode().strip())

p = subprocess.Popen("sh get_data.sh name {}".format(sys.argv[1]),stdout=subprocess.PIPE,shell=True)
name = p.stdout.readline().decode().strip()

p = subprocess.Popen("sh get_data.sh 1m {}".format(sys.argv[1]),stdout=subprocess.PIPE,shell=True)
m1 = p.stdout.readline().decode().strip()
p = subprocess.Popen("sh get_data.sh 3m {}".format(sys.argv[1]),stdout=subprocess.PIPE,shell=True)
m3 = p.stdout.readline().decode().strip()
p = subprocess.Popen("sh get_data.sh 6m {}".format(sys.argv[1]),stdout=subprocess.PIPE,shell=True)
m6 = p.stdout.readline().decode().strip()


temp_out = temp.render(
        datetime=dt,
        valuelist=vl2,
        linelist=ll2,
        name='{}-{}'.format(sys.argv[1],name),
        m1=m1,
        m3=m3,
        m6=m6)
with open(os.path.join('./source/_posts/','{}_{}.md'.format(sys.argv[1],name)), 'w', encoding='utf-8') as f:
    f.writelines(temp_out)
    f.close()

