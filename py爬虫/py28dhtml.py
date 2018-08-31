# Selenium 的使用
# 通过 WebDriver 操作百度进行查找

from selenium import webdriver
import time


# 通过 Keys 模拟键盘
# 也就是放入需要输入的东西，就不用键盘输入了
from selenium.webdriver.common.keys import Keys

# 操作哪个浏览器就对哪个浏览器创建一个实例，这里是 PhantomJS
# 自动按照环境变量查找相应浏览器，如果没有配置环境变量就将路径作为参数
driver = webdriver.PhantomJS(executable_path=r"D:\app\phantomjs-2.1.1-windows\bin\phantomjs.exe")

driver.get("http://www.baidu.com")

# 通过函数查找 title 标签
print("Title: {0}".format(driver.title))
