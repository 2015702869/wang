from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
dr = webdriver.Chrome()
dr.get('https://ljlykz.gzkz.chaoxing.com')
elem_user = dr.find_element(By.XPATH, '//*[@id="phoneName"]')#获取用户名输入框
elem_user.send_keys('账号')#输入用户名
elem_pass = dr.find_element(By.XPATH, '//*[@id="phonepassword"]')#获取密码输入框
elem_pass.send_keys('密码')
dr.find_element(By.XPATH, '//*[@type="submit"]').click()
time.sleep(2)
dr.get('https://ljlykz.gzkz.chaoxing.com/studyApp/studying?s=8bba95c05159f88aa656375676682848')#
time.sleep(2)
list = []
cartl = dr.find_elements(By.XPATH, '//*[@class="w_cour_row"]/dd[2]/p[2]')
for val in cartl:
    new = val.text.split(' ')
    list.append(new[3])
i = 1
for value in list:
    if(value != "100%"):
        break
    else:
        i = i+1
html = dr.find_elements(By.XPATH, '//*[@class="w_cour_row"]/dd[1]/a[1]')
z = 1
for elems in html:
    if(z == i):
        elems.click()
        time.sleep(2)
        break
    else:
        z = z+1

def timevoid(listtime):
    timivoid = listtime.split(":")
    forwhe = int(timivoid[0])*60 + int(timivoid[1]) + 5
    return forwhe
class Start:
    voidtim = 1
    void = ""
    def window():
        time.sleep(2)
        iframe = dr.find_element(By.XPATH, '//*[@id="iframe"]')
        dr.switch_to.frame(0)
        time.sleep(2)
        dr.switch_to.frame(0)
        dr.find_element(By.XPATH, '//*[@class="vjs-big-play-button"]').click()
        time.sleep(2)
        Start.void = dr.find_element(By.XPATH, '//*[@class="vjs-control-bar"]/div[4]/span[2]')
        timer = threading.Timer(1, Start.fun_timer, (timevoid(Start.void.text),))
        timer.start()
    def fun_timer(voidtims):
        global timerb
        if(int(Start.voidtim) < voidtims):
            Start.voidtim = Start.voidtim + 1
            timer = threading.Timer(1, Start.fun_timer, (voidtims,))#重复调用方法达到定时器模式
            timer.start()
            print(Start.voidtim)
        else:
            dr.implicitly_wait(10)  # 设置最最长等待时间10s
            # dr.switch_to.default_content()
            # dr.find_element(By.XPATH, '//*[@class="tabtags"]/span[2]').click()  # 切换到课后答题也米娜
            # dr.implicitly_wait(10)  # 设置最最长等待时间10s
            # dr.switch_to.frame(0)  # 进入iframe框架第一层
            # dr.implicitly_wait(10)  # 设置最最长等待时间10s
            # dr.switch_to.frame(0)  # 进入iframe框架第一层中的第一层
            # dr.implicitly_wait(10)  # 设置最最长等待时间10s
            # dr.switch_to.frame(0)  # 进入iframe框架第一层中的第一层的第一层
            # timu = dr.find_elements(By.XPATH, '//*[@class="TiMu"]/div[@class="clearfix"]/ul/li[3]')  # 获取选择题单选框
            # for tival in timu:
            #     tival.click()
            # timebutt = dr.find_elements(By.XPATH, '//input[@value="false"]')  # 获取判断题单选按钮
            # for buttval in timebutt:
            #     buttval.click()  # 选择单选按钮
            # dr.find_element(By.XPATH, '//a[@class="Btn_blue_1 marleft10"]').click()
            # dr.implicitly_wait(50)  # 设置最最长等待时间10s
            # dr.find_element(By.XPATH, '//*[@class="marTop30"]/a[1]').click()  # 点击connimt提示框点击确认
            dr.switch_to.default_content()  # 切换到最上层窗口
            # dr.implicitly_wait(10)  # 等待页面加载最长时间十秒
            #dr.find_element(By.XPATH, '//*[@class="right2"]').click()  # 点击下一题
            dr.find_element(By.XPATH, '//*[@class="tabtags"]/div[2]').click()
            Start.voidtim = 1
            Start.window()
all_h = dr.window_handles
dr.switch_to.window(all_h[1])
allhtml = dr.find_element(By.XPATH, '//*[@class="orange"]')
allhtml.click()
Start.window()

