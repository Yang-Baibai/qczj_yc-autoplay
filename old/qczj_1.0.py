import pyautogui
from time import sleep

# 间隔时间(根据网络情况调整)
Intervals = 5
# 发布次数(初始值)
qczj_set = 0
# 复制发布(变动值)
qczj_fz_x = 1777
qczj_fz_y = 370

def qczj():
    # 按钮位置
    qczj_cg = (66, 325)
    qczj_fb = (490,960)
    qczj_qd = (1100, 580)
    # 点击草稿箱
    pyautogui.click(qczj_cg,clicks=2,interval=1)
    sleep(Intervals)
    # 点击复制发布
    pyautogui.click(qczj_fz_x,qczj_fz_y)
    sleep(Intervals)
    # 模拟滚轮
    pyautogui.click(1482,227)
    pyautogui.press('pgdn', presses=5)
    sleep(0.5)
    # 点击发布
    pyautogui.click(qczj_fb)
    sleep(0.5)
    # 点击确定
    pyautogui.click(qczj_qd)
    sleep(0.5)

# 汽车之家发布次数(6次)
while qczj_set<=5:
    qczj()
    qczj_fz_y += 50
    qczj_set+=1