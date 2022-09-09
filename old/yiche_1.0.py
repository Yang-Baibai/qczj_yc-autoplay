import pyautogui
from time import sleep

class yc:
    def __init__(self):
        # 间隔时间(根据网络情况调整)
        self.Intervals = 3
        # 发布次数(初始值)
        self.yc_set = 0
        # 优惠金额
        self.price = ['4', '4', '10', '6', '7', '6.5']
        self.price_ct5 = ['3.5', '3']
        # 车型位置
        self.yc_ct4_x = 315
        self.yc_ct4_y = 400
        # 按钮位置
        self.yc_1 = (20, 220)
        self.yc_2 = (202, 243)
        self.yc_qx = (240, 449)
        self.yc_del = (363, 392)
        self.yc_del2 = (888, 602)
        # 按钮位置
        self.yc_fb = (260, 390)
        self.yc_day2 = (675, 488)
        self.yc_tj = (315, 538)
        self.yc_je = (500, 520)
        self.yc_kjfb = (460, 755)
        self.yc_jxfb = (907, 438)
    def yc_del(self):
        # 首页--进入界面
        pyautogui.click(self.yc_1)
        sleep(self.Intervals)
        pyautogui.moveTo(self.yc_2,1)
        pyautogui.click(self.yc_2)
        sleep(self.Intervals)
        # 全选删除
        pyautogui.click(self.yc_qx)
        pyautogui.click(self.yc_del)
        pyautogui.click(self.yc_del2)
        sleep(self.Intervals)
    def yc(self):
        # 发布促销
        sleep(self.Intervals)
        pyautogui.click(self.yc_fb)
        sleep(1)
        # 车型选择
        pyautogui.click(self.yc_ct4_x, self.yc_ct4_y)
        sleep(1)
        # 日期选择
        pyautogui.click(self.yc_day2)
        sleep(1)
        # 优惠条件
        pyautogui.click(self.yc_tj)
        sleep(1)
        # 模拟滚轮
        pyautogui.press('pgdn', presses=5)
        sleep(1)
        # 优惠金额
        pyautogui.click(self.yc_je)
        sleep(1)
        pyautogui.write(self.price[self.yc_set])
        sleep(1)
        pyautogui.click(1000, 550)
        sleep(1)
        # 快捷发布
        pyautogui.click(self.yc_kjfb)
        sleep(1)
        # 继续发布
        pyautogui.click(self.yc_jxfb)
        sleep(1)
    def yc_ct5(self):
        pyautogui.click(1133, 838)
        sleep(0.2)
        pyautogui.write(self.price_ct5[0])
        sleep(0.2)
        pyautogui.click(1129, 900)
        sleep(0.2)
        pyautogui.write(self.price_ct5[1])
        sleep(0.2)
        pyautogui.click(1119, 965)
        sleep(0.2)
        pyautogui.write(self.price_ct5[1])
        sleep(0.2)
    def yc_ct6(self):
        pass


# 易车发布
# yc_del()
# while yc_set <= 5:
#     yc()
#     yc_ct4_x += 168
#     yc_set += 1