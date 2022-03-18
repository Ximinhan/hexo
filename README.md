[![Data refresh workflow](https://github.com/Ximinhan/hexo/actions/workflows/manual.yml/badge.svg?branch=main)](https://github.com/Ximinhan/hexo/actions/workflows/manual.yml)
[![Node.js CI](https://github.com/Ximinhan/hexo/actions/workflows/node.js.yml/badge.svg)](https://github.com/Ximinhan/hexo/actions/workflows/node.js.yml)
# diagram of fund
Use hexo automatically collect fund data and generate report in github pages



# Usage
1. clone the repo
2. there are some core file and scripts list here

   `star_list.txt`: contains all the stock code we want to check
   
   `stock_list.txt`: contains all the stock code, if we want to change star_list we can pick up from here
   
   `update_start_list.py`: is the entry to launch an update of the star_list
   
   `render.py`: is the function script used to update the stock data called by update_start_list.py, it will call seval scripts to gather necessary data
   
3. when update_start_list.py run complete push the commit it will trigger actions to update github pages
