import re
import pyautogui
from time import sleep
import datetime

# 修改延期地址
class http:
    def __init__(self):
        self.ct4 = ['newsId=808927428&','newsId=808590117&']
        self.ct5 = ['newsId=808927358&','newsId=808590151&']
        self.ct6 = ['newsId=808927276&','newsId=808590208&']
        self.xt4 = ['newsId=808926431&','newsId=808590347&']
        self.xt5 = ['newsId=808925359&','newsId=808590246&']
        self.xt6 = ['newsId=808925063&','newsId=808590288&']
        self.startdate = f'startdate=20{year}-{moon}-{day+1}&'
        self.enddate = f'enddate=20{year}-{moon}-{day+1}'
        self.newhttplist = []
        self.http_1 = 'https://das.yichehuoban.cn/dasplat/news/edit?newsType=1&homePageName=discount_list&action=delay&source=1&newsId=808925359&startdate=2022-08-29&enddate=2022-09-27'
        self.http_2 = 'https://das.yichehuoban.cn/dasplat/news/edit_fixed?newsType=2&homePageName=replace_list&action=delay&source=2&newsId=808590117&startdate=2022-08-28&enddate=2022-08-28'
    def res(self,i,s):
        http1 = re.sub('newsId=(\w*)&',i,s)
        http2 = re.sub(r'startdate=(.*?)&', self.startdate, http1)
        self.newhttplist.append(re.sub(r'enddate=(.*)', self.enddate, http2))
    def newhttp(self,s):
        for i in s:
            if i == s[0]:
                self.res(i,self.http_1)
            if i == s[1]:
                self.res(i,self.http_2)

# 点击操作
class click:
    def __init__(self):
        # 间隔时间(根据网络情况调整)
        self.Intervals = 5
        # 发布次数(初始值)
        self.set = 0
        # 地址栏位置
        self.Bar = (963,46)
        # 确定位置
        self.Confirm = (351,754)
    def click(self,i):
        while self.set <= i:
            # 点击地址栏
            pyautogui.click(self.Bar)
            sleep(1)
            # 输入地址
            pyautogui.write(yc_http.newhttplist[self.set])
            print(yc_http.newhttplist[self.set])
            sleep(0.5)
            # 回车
            pyautogui.press('enter')
            sleep(self.Intervals)
            # 模拟滚轮
            pyautogui.press('pgdn',presses=5)
            sleep(1)
            # 点击发布
            pyautogui.click(self.Confirm)
            sleep(1)
            self.set += 1

# 主函数
def run():
    choose = pyautogui.confirm(text='易车自动发文程序即将运行,请确认后台是否登录,地址栏输入法是否为英文,英文是否为小写,确认无误后打开浏览器点击确认即可运行.    点击关闭或取消,将会于10分钟后再次弹出', title='易车自动发文',buttons=['OK', 'Cancel'])
    if choose == 'OK':
        yc_http.newhttp(yc_http.ct4)
        yc_http.newhttp(yc_http.ct5)
        yc_http.newhttp(yc_http.ct6)
        yc_http.newhttp(yc_http.xt4)
        yc_http.newhttp(yc_http.xt5)
        yc_http.newhttp(yc_http.xt6)
        yc_click.click(11)
        # print(yc_http.newhttplist)
        exit()
    else:
        sleep(600)

# 主运行
if __name__ == '__main__':
    # 时间参数
    date = datetime.datetime.now()
    year = int(date.strftime('%y'))
    moon = int(date.strftime('%m'))
    day = int(date.strftime('%d'))

    # 月初判断
    if day < 10:
        day = int('0' + str(day))
    # 月底判断
    if moon in [1, 3, 5, 7, 8, 10, 12]:
        if day == 31:
            day = 0
            moon += 1
    if moon not in [1, 3, 5, 7, 8, 10, 12, 2]:
        if day == 30:
            day = 0
            moon += 1
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if moon == 2 and day == 29:
            day = 0
            moon += 1
    else:
        if moon == 2 and day == 28:
            day = 0
            moon += 1

    # 实例化
    yc_http = http()
    yc_click = click()

    while True:
        run()