# 初始模式，0 表示控制权由开发板管理
mode = 0 
'''
# 模拟写入 GPIO 引脚的值
def write_pin(state):
    if state:
        print("LED is ON")
    else:
        print("LED is OFF")
'''
# 控制 LED 的方法
#为了方便规约，on,off,con分别表示打开，关闭，控制权返还给开发板,对应0,1,2
def set_led(msg,state=True):
    global mode
    #ON-0,OFF-1,CON-2
    msg = int(msg)
    if msg == 0:
        mode = 1
        #write_pin(True)  # 模拟打开 LED
        #print(f"{msg} turn on led")
        state  = True
    elif msg == 1:
        mode = 1
        #write_pin(False)  # 模拟关闭 LED
        #print(f"{msg} turn off led")
        state = False
    elif msg == 2:
        mode = 0  # 控制权返还给开发板
        #wrong:缺少state = False
        #print("Control returned to the board.")
    print(f"msg:{msg} mode:{mode},state:{state}")
    return mode,state

# 测试该方法
#set_led("ON")
#set_led("OFF")
#set_led("CON")
if __name__ == "__main__":
    
    set_led(input("请输入指令："))