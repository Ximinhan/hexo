from selenium import webdriver
import re
urls = ['https://www.banban.cn/gupiao/list_sh.html',
            'https://www.banban.cn/gupiao/list_sz.html',
            'https://www.banban.cn/gupiao/list_cyb.html']
classs = ['上证','深证','创业']

driver = webdriver.Firefox()

for index in range(len(urls)):
    class_ = classs[index]
    driver.get(urls[index])
    contents = driver.find_elements_by_xpath('//*[@id="ctrlfscont"]/ul/li')
    for content in contents:
        content = content.text
        with open("./stock_list.txt","a") as f:
            f.write("{} {} {} \n".format(re.compile(r'\d+').findall(content)[0],class_,content.split('(')[0]))

driver.close()
