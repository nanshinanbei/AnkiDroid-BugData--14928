import uiautomator2 as u2
import time

d = u2.connect('10CD890ATZ0015H')  # 连接设备

d.app_start('com.ichi2.anki.debug')  # 启动应用
d.app_wait('com.ichi2.anki.debug')

d.click(0.1, 0.1)  # 点击左上角的菜单
d(text='卡片浏览器').click()  # 点击卡片浏览器
time.sleep(3)  # 等待3秒

d.click(0.95, 0.05)  # 点击右上角的菜单
d(text='预览').click()  # 点击预览
