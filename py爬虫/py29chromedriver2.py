# Selenium + Chrome 案例2
# 打开的浏览器可能会弹窗，点击【取消】或者【不管它】都行
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 默认不需要路径，如果没有环境变量就需要加上
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url)

# 根据id查找，后面加.text 表示拿看到的文本数据
text = driver.find_element_by_id('wrapper').text

print(driver.title)

# 对页面截屏，保存为 baidu.png
driver.save_screenshot('py29baidu.png')

# 控制 Chrome 在输入框输入大熊猫
driver.find_element_by_id('kw').send_keys(u"大熊猫")
# 单击搜索按钮，id = 'su'
driver.find_element_by_id('su').click()

# 缓冲秒，让页面加载图片等
time.sleep(3)
# 截屏，保存
driver.save_screenshot("py29daxiongmao.png")

# 获取当前页面的 cookie 常用在需要登录的页面
print(driver.get_cookie('cookie'))

# 模拟 按下两个按键 Ctrl + a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# 模拟 按下两个按键 Ctrl + c
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')
