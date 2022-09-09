import re
import pyautogui
from time import sleep
import datetime

# 修改地址
class http:
    def __init__(self):
        self.ct4 = ['newsId=873151453']
        self.ct5 = ['newsId=674133349']
        self.ct6 = ['newsId=553208387']
        self.xt4 = ['newsId=880141277']
        self.xt5 = ['newsId=737665584']
        self.xt6 = ['newsId=728445290']
        self.newhttplist = []
        self.http_1 = 'https://ics.autohome.com.cn/price/promotion/edit?temp=1&newsId=873151453'
    def res(self,i,s):
        http1 = re.sub('newsId=(\w*)',i,s)
        self.newhttplist.append(http1)
    def newhttp(self,s):
        for i in s:
            self.res(i,self.http_1)

# 点击操作
class click:
    def __init__(self):
        # 间隔时间(根据网络情况调整)
        self.Intervals = 5
        # 发布次数(初始值)
        self.set = 0
        # 地址栏位置
        self.Bar = (963,46)
        # 发布位置
        self.Confirm = (488,960)
        # 确定位置
        self.Confirm2 = (1100,575)
    def click(self,i):
        while self.set <= i:
            # 点击地址栏
            pyautogui.click(self.Bar)
            sleep(1)
            # 输入地址
            pyautogui.write(qczj_http.newhttplist[self.set])
            print(qczj_http.newhttplist[self.set])
            sleep(0.5)
            # 回车
            pyautogui.press('enter')
            sleep(self.Intervals)
            # 点击页面
            pyautogui.click(1355,295)
            sleep(1)
            # 模拟滚轮
            pyautogui.press('pgdn',presses=5)
            sleep(1)
            # 点击发布
            pyautogui.click(self.Confirm)
            sleep(1)
            pyautogui.click(self.Confirm2)
            sleep(self.Intervals)
            self.set += 1

# 主函数
def run():
    global loop
    if loop == 4:
        exit()
    choose = pyautogui.confirm(text=f'汽车之家自动发文程序即将运行,请确认后台是否登录,地址栏输入法是否为英文,英文是否为小写,确认无误后打开浏览器点击确认即可运行.    点击关闭或取消,将会于下次整点再次弹出.   如需使用推荐名额请等程序运行结束后手动修改------这是第{loop}次发文', title='汽车之家自动发文',buttons=['OK', 'Cancel'])
    if choose == 'OK':
        qczj_http.newhttp(qczj_http.ct4)
        qczj_http.newhttp(qczj_http.ct5)
        qczj_http.newhttp(qczj_http.ct6)
        qczj_http.newhttp(qczj_http.xt4)
        qczj_http.newhttp(qczj_http.xt5)
        qczj_http.newhttp(qczj_http.xt6)
        qczj_click.click(5)
        print(qczj_http.newhttplist)
        loop += 1
    else:
        sleep(60)

# 自动运行函数
def timeloop(time):
    if time in ['10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','17:40','17:45','17:50','17:55']:
        run()
    sleep(10)

# 运行函数
if __name__ == '__main__':
    # 实例化
    qczj_http = http()
    qczj_click = click()
    # 存储执行次数
    loop = 1
    # 存储当前时间
    re_time = []
    while True:
        # 获取当前时间
        date = datetime.datetime.now()
        re_time.append((re.search('(\w+):(\w+)', str(date))))
        # 运行
        qczj_click.set = 0
        print(re_time[0].group(),loop)
        timeloop(re_time[0].group())
        del re_time[0]