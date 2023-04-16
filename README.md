> 此为个人整理的工具，以便编写在中鸣机器人下的python脚本，需要搭配`VSCode`之类的IDE使用。
>
> 将`rcu.py`与主程序放在同一文件夹下，使用`import rcu`即可。程序传入机器人时不可传入`rcu.py`，这仅仅是辅助工具。
>
> 详情参见中鸣官方文档[Zmrobo3软件帮助手册](https://www.yuque.com/zmrobo/robocode/)
>
> 作者：[Aristore](https://github.com/aristorechina)

# **控制器**

## 1.控制器任务（）

（1）功能：程序起始模块，程序运行时会执行其下方模块
（2）参数：任务1-任务8，表示任务序号

**范例：短鸣蜂鸣器**
内置蜂鸣器响1秒后关闭

```python
import rcu

def task1():
    rcu.SetInBeep(1)
    rcu.SetWaitForTime(1)
    rcu.SetInBeep(0)

task1()
```

## 2.按下左键？

（1）功能：检测控制器的左侧按键是否被按下
（2）返回值：1/0，按下时返回数值1，未按下时返回数值0

**范例：左键检测**
当左键被按下时，屏幕显示left字母1秒

```python
import rcu

def task1():
    while True:
        if rcu.GetLeftButton():
            rcu.SetDisplayString(1,"left",0xFFE0,0x0000)
            rcu.SetWaitForTime(1)
            rcu.SetLCDClear(0x0000)

task1()
```

## 3.按下右键？

（1）功能：判断控制器的右侧按键是否被按下
（2）返回值：1/0，按下时返回数值1，未按下时返回数值0

**范例：右键检测**
当右键被按下时，屏幕显示right字母1秒

```python
import rcu

def task1():
    while True:
        if rcu.GetRightButton():
            rcu.SetDisplayString(1,"right",0xFFE0,0x0000)
            rcu.SetWaitForTime(1)
            rcu.SetLCDClear(0x0000)

task1()
```

## 4.麦克风音量

（1）功能：读取控制器内置麦克风检测的声音大小值
（2）返回值：0-4095，只表示音量大小无具体单位

**范例：声控转弯机器人**
当检测到音量数值大于2000时，维持转弯状态1秒，否则往前移动

```python
import rcu

def task1():
    while True:
        if (rcu.GetInMic()>2000):
            rcu.SetMotor(1,50)
            rcu.SetMotor(2,0)
            rcu.SetWaitForTime(1)
        else:
            rcu.SetMotor(1,50)
            rcu.SetMotor(2,50)

task1()
```

## 5.电池电压

（1）功能：读取控制器此时电源电压值
（2）返回值：0-100，当数据为84时电压为8.4V

**范例：电量提醒器**
当检测到电池电压数值大于70时，显示“现电量充足”，否则显示“请及时充电”

```python
import rcu

def task1():
    while True:
        if (rcu.GetInVotage()>70):
            rcu.SetDisplayString(1,"现电量充足",0xFFE0,0x0000)
        else:
            rcu.SetDisplayString(1,"请及时充电",0xFFE0,0x0000)

task1()
```

## 6.控制器时间

（1）功能：读取程序运行至今的时间
（2）返回值：数值单位为毫秒，数值1000时为1秒

**范例：计时器**
实时显示控制器时间

```python
import rcu

def task1():
  while True:
    rcu.SetDisplayVar(1,rcu.GetSysTime(),0xFFE0,0x0000)

task1()
```

## 7.控制器时间归零

（1）功能：控制器运行程序后，内置时钟归零

**范例：重复计时器**
实时显示控制器时间，当按下左键时重新计时

```python
import rcu

def task1():
  while True:
    rcu.SetDisplayVar(1,rcu.GetSysTime(),0xFFE0,0x0000)
    if (rcu.GetLeftButton()):
      rcu.SetSysTime()

task1()
```

## 8.蜂鸣器（关）

（1）功能：开启或关闭蜂鸣器
（2）参数：“关”“开”，蜂鸣器开启/蜂鸣器关闭

**范例：蜂鸣节拍器**
蜂鸣器重复开启半秒后，关闭半秒实现节拍提示

```python
import rcu

def task1():
    while True:
        rcu.SetInBeep(1)
        rcu.SetWaitForTime(0.5)
        rcu.SetInBeep(0)
        rcu.SetWaitForTime(0.5)

task1()
```

## 9.设置声音频率（）Hz 时间（）s

（1）功能：设置蜂鸣器的音调以及播放时长
（2）参数：“Hight Do”“Hight Re”.....“Low La”"Low Si"，Hight代表高音Low代表低音
（3）参数：“双拍”“一拍”“半拍”“1/4拍”“1/8拍”，播放音调持续时间

**范例：高中低音效提醒器**
循环播放高中低的Do音，做到提醒效果

```python
import rcu

def task1():
    while True:
        rcu.SetInSound(1047,(0.25)*1000)
        rcu.SetWaitForTime(0.5)
        rcu.SetInSound(523,(0.25)*1000)
        rcu.SetWaitForTime(0.5)
        rcu.SetInSound(262,(0.25)*1000)
        rcu.SetWaitForTime(0.5)

task1()
```

## 10.地址（）数据值

（1）功能：读取控制器内置数据的数值
（2）参数：1-156，对应内置地址名称
（3）返回值：控制器内置地址数据值

**范例：内置数据控制马达转动**
调用地址1的内置数据控制马达转动

```python
import rcu

def task1():
    while True:
        rcu.SetMotor(1,rcu.GetData(1))

task1()
```

## 11.地址（）数据值设为（）

（1）功能：将控制器指定内置数据设为指定值
（2）参数：1-156，对应内置地址名称
（3）参数：1-4095，赋予内置地址数据值

**范例：设置地址初始数值**
设定地址1的数据值为50，控制M1和M2马达以50的速度转动

```python
import rcu

def task1():
    rcu.SetData(1,50);
    while True:
        rcu.SetMotor(1,rcu.GetData(1))

task1()
```

------

# 马达

## 1.马达（）以速度（）转动

（1）功能：使马达以指定速度运转
（2）参数：M1-M4，马达连接端口
（3）参数：-100-100，马达速度数值越大速度越快，0停止，小于0则反转，大于0则正转

**范例：原地旋转机器人**
机器人以50速度原地旋转

```python
import rcu

def task1():
    while True:
        rcu.SetMotor(1,50)
        rcu.SetMotor(2,0)

task1()
```

## 2.马达（）编码器数值

（1）功能：读取马达编码器数值，起到记录马达转动角度的作用
（2）参数：M1-M4，马达连接端口
（3）返回值：马达转动的角度值，数值1表示转动1度，有正负区分

**范例：转一圈后停止转动**
马达以50速度转动，编码器数值大于360后，马达停止转动

```python
import rcu

def task1():
    rcu.SetMotor(1,50)
    while not (rcu.GetMotorCode(1)>360):
        pass
    rcu.SetMotor(1,0)

task1()
```

## 3.马达（）编码器归零

（1）功能：将编码器记录的数值清零
（2）参数：M1-M4，马达连接端口

**范例：来回转动**
用马达转动的角度值，控制马达正传或反转，在马达转动超过一圈后，编码器记录清零，马达进行反方向转动，实现来回移动

```python
import rcu

def task1():
    rcu.SetMotor(1,50)
    while True:
        if (rcu.GetMotorCode(1)>360):
            rcu.SetMotorCode(1);
            rcu.SetMotor(1,-50)
        if (rcu.GetMotorCode(1)<-360):
            rcu.SetMotorCode(1);
            rcu.SetMotor(1,50)

task1()
```

## 4.设置伺服马达（）以速度（）旋转（）

（1）功能：设置马达转动到指定角度
（2）参数：M1-M4，马达连接端口
（3）参数：-100-100，马达速度
（4）参数：马达旋转的角度

**范例：设置马达按指定速度转动到特定角度**
马达M1以速度100转动一圈

```python
import rcu

def task1():
    rcu.SetMotorServo(1,100,360)

task1()
```

## 5.等待伺服马达（）以速度（）旋转（）

（1）功能：等待马达转动到指定角度，再执行下方程序
（2）参数：M1-M4，马达连接端口
（3）参数：-100-100，马达速度
（4）参数：马达旋转的角度

**范例：来回转动**
马达循环执行反转完90度后，再正转90度

```python
import rcu

def task1():
    while True:
        rcu.SetWaitForAngle(1,-100,90)
        rcu.SetWaitForAngle(1,100,90)

task1()
```

## 6.马达（）（）以速度（）编码（）前进

（1）功能：使两个马达同步转动指定编码
（2）参数：M1-M4，马达连接端口
（3）参数：M1-M4，马达连接端口
（4）参数：-100-100，马达速度
（5）参数：0-2147483647，马达旋转的编码值

**范例：机器人往前移动**
马达M1和M2同时以50的速度转动2圈，实现往前移动
```
 需要注意：同步马达模块是有缓慢启动（保证双马达启动稳定）的过程，如果不断重复执行模块会让两个马达一直处在缓慢启动过程而无法启动。
```

```python
import rcu

def task1():
    rcu.SetMotorStraightAngle(1,2,50,720)

task1()
```

## 7.马达（）（）以速度（）编码（）转弯

（1）功能：使两个马达同步反向转动指定编码
（2）参数：M1-M4，马达连接端口
（3）参数：M1-M4，马达连接端口
（4）参数：-100-100，马达速度
（5）参数：0-2147483647，马达旋转的编码值

**范例：原地掉头**
马达M1正转360度，马达M2反转360度，实现掉头

```python
import rcu

def task1():
    rcu.SetCarTurn(1,2,50,360)

task1()
```

## 8.马达功率M1（）M2（）M3（）M4（）

（1）功能：设置马达最大功率，用于调整马达差异，重启控制器后会复原。
（2）参数：-100-100，M1马达功率百分比
（2）参数：-100-100，M2马达功率百分比
（2）参数：-100-100，M3马达功率百分比
（2）参数：-100-100，M4马达功率百分比

**范例：改变马达最大功率**
设置M1M2马达以一百速度前进，当按下左键时最大功率改变，实现差速转弯。

```
设置功率相当于设置速度的最大值，马达功率最大值为50时，100速度实际上只有100*50%=50速度。
```

```python
import rcu

def task1():
    rcu.SetMotorPower(50,100,-50,-100);

task1()
```

## 9.设置双马达走直线（）（）速度（）

（1）功能：使两个马达同步转动
（2）参数：M1-M4，马达连接端口
（3）参数：M1-M4，马达连接端口
（4）参数：-100-100，马达速度

**范例：往前直走**
马达M1和M2均往同一方向同一速度转动

```python
import rcu

def task1():
    rcu.SetMotorStraight(1,2,50);

task1()
```

## 10.设置双马达走同步转弯（）（）速度（）角度（）

（1）功能：使两个马达同步转动指定角度
（2）参数：M1-M4，马达连接端口
（3）参数：M1-M4，马达连接端口
（4）参数：-100-100，马达速度
（5）参数：马达旋转的角度

**范例：移动转弯**
马达M1和M2以整体速度为50，圆心角60度，不停转向移动

```python
import rcu

def task1():
    rcu.SetMotorStraightTurn(1,2,50,60);

task1()
```

## 11.小型舵机（）转动角度（）

（1）功能：使小型舵机转动指定角度
（2）参数：P4-P6，小型舵机连接端口
（3）参数：0-180，小型舵机的转动角度

```python
rcu.SetServo(1,90)
```

## 12.小型舵机调速（）转动角度（）持续（）毫秒

（1）功能：使小型舵机在指定时间内转动指定角度
（2）参数：P4-P6，小型舵机连接端口
（3）参数：0-180，小型舵机的转动角度
（4）参数：转动时间，数值为毫秒单位，数值1000时为1秒

```python
rcu.SetServoTime(1,90,1000)
```

------

# 传感器

## 1、触碰传感器（）被按下？

（1）功能：判断触碰传感器是否被按下
（2）参数：P1-P8，传感器端口
（3）返回值：0/1，按下返回1，否则返回0

**范例：触碰转动**
触碰传感器被按下时，马达M1转动，否则不转动

```python
import rcu

def task1():
    while True:
        if rcu.GetTouch(1):
            rcu.SetMotor(1,50)
        else:
            rcu.SetMotor(1,0)

task1()
```

## 2、颜色传感器（）数值

（1）功能：读取颜色传感器检测物体的颜色值
（2）参数：P1-P8，传感器端口
（3）返回值：1-6，对应红、绿、蓝、黄、黑、白色

**范例：测色移动**
颜色传感器检测到红色，马达M1转动，其余颜色不转动

```python
import rcu

def task1():
    while True:
        if (rcu.GetColorSensor(1, 4)==1):
            rcu.SetMotor(1,50)
        else:
            rcu.SetMotor(1,0)

task1()
```

## 3、超声波传感器（）数值

（1）功能：读取超声传感器与障碍物的距离值
（2）参数：P1-P8，传感器端口
（3）返回值：7-180， 单位cm

**范例：测距移动**
当超声波传感器检测到自身与障碍物的距离小于20时，马达M1反方向转动，否则正方向转动

```python
import rcu

def task1():
    while True:
        if (rcu.GetUltrasound(1)<20):
            rcu.SetMotor(1,-50)
        else:
            rcu.SetMotor(1,50)

task1()
```

## 4、光电传感器（）数值

（1）功能：读取光电传感器检测物体的颜色深度值
（2）参数：P1-P8，传感器端口
（3）返回值：0-4095， 数值随着被测物体颜色越深而减少  

**范例：深浅检测**
当光电传感器测出的返回值小于1000，显示“这是深色”，否则显示“这是浅色”

```python
import rcu

def task1():
    while True:
        if (rcu.GetLightSensor(1)<1000):
            rcu.SetDisplayString(1,"这是深色",0xFFE0,0x0000)
        else:
            rcu.SetDisplayString(1,"这是浅色",0xFFE0,0x0000)

task1()
```

## 5、光电传感器（）数字数值

（1）功能：判断光电传感器检测的物体颜色深度是否小于阈值
（2）参数：P1-P8，传感器端口
（3）返回值：0/1，低于阈值返回1，否则返回0

**范例：深浅检测**
当光电传感器数字数值的返回值为1时，显示“这是深色”，否则显示“这是浅色”

```python
import rcu

def task1():
    while True:
        if rcu.GetLightSensorData(1):
            rcu.SetDisplayString(1,"这是深色",0xFFE0,0x0000)
        else:
            rcu.SetDisplayString(1,"这是浅色",0xFFE0,0x0000)

task1()
```

## 6、光电传感器（）灯（）

（1）功能：开启或关闭光电传感器的LED灯
（2）参数：P1-P8，传感器端口
（3）参数：“关”“开”，参数为“开”时开启灯，参数为“关”时关闭灯

**范例：闪灯提示器**
检测到超过阈值的颜色后，闪灯三次提示，没超过阈值时，LED灯常亮

```python
import rcu

def task1():
    while True:
        if rcu.GetLightSensorData(1):
            for count in range(3):
                rcu.SetLightSensorLed(1,0)
                rcu.SetWaitForTime(0.1)
                rcu.SetLightSensorLed(1,1)
                rcu.SetWaitForTime(0.1)
        else:
            rcu.SetLightSensorLed(1,1)

task1()
```

## 7、彩灯模块（）设置为（）

（1）功能：设置彩灯模块的显示颜色
（2）参数：P1-P8，传感器端口
（3）参数：“红色”“绿色”“蓝色”“黄色”“紫色”“青色”“白色”，彩灯颜色

**范例：三色跑马灯**
红黄蓝三原色交替出现，实现跑马灯效果

```python
import rcu

def task1():
    while True:
        for count in range(3):
            rcu.Set3CLed(1,1)
            rcu.SetWaitForTime(1)
            rcu.Set3CLed(1,4)
            rcu.SetWaitForTime(1)
            rcu.Set3CLed(1,3)
            rcu.SetWaitForTime(1)

task1()
```

------

# **显示**

## 1、屏幕被触摸？

（1）功能：判断屏幕是否被触摸
（2）返回值：1/0，触摸时返回1，未触摸时返回0

**范例：触摸检测**
当屏幕被触摸，显示“touch”，否则无显示

```python
import rcu

def task1():
    while True:
        if  rcu.GetTouchScreen():
            rcu.SetDisplayString(1,"touch",0xFFE0,0x0000)
        else:
            rcu.SetLCDClear(0x0000);

task1()
```

## 2、屏幕被触摸的X轴

（1）功能：读取屏幕触摸点的X轴坐标值
（2）返回值：1-240，屏幕从左往右，数值从小到大，无触摸时值为0

**范例：显示触碰位置的X坐标**
屏幕被触碰时，显示触碰位置的X坐标

```python
import rcu

def task1():
    while True:
        if  rcu.GetTouchScreen():
            rcu.SetDisplayString(1,str(rcu.GetTouchScreenX()),0xFFE0,0x0000)
        else:
            rcu.SetLCDClear(0x0000);

task1()
```

## 3、屏幕被触摸的Y轴

（1）功能：读取屏幕触摸点的Y轴坐标值
（2）返回值：1-320，屏幕从上往下，数值从小到大，无触摸时值为0

**范例：触屏移动**
触屏记录坐标Y轴数值，松开后，马达M1和M2以该数值前进

```python
import rcu

def task1():
    while True:
        if  rcu.GetTouchScreen():
            rcu.SetData(50,rcu.GetTouchScreenY());
            while not not(rcu.GetTouchScreen()):
                pass
            rcu.SetMotorStraightAngle(1,2,50,rcu.GetData(50))

task1()
```

## 4、LCD清屏黄色

（1）功能：清除显示屏全部的显示内容，背景颜色设置成黄色
（2）参数：“红色”“绿色”“蓝色”“黄色”“紫色”“青色”“白色”“黑色”，清屏后的背景颜色

**范例：清除显示**
屏幕被触摸时，显示坐标信息，否则不显示任何内容

```python
import rcu

def task1():
    while True:
        if  rcu.GetTouchScreen():
            rcu.SetDisplayString(1,str(rcu.GetTouchScreenX()),0xFFE0,0x0000)
            rcu.SetDisplayString(2,str(rcu.GetTouchScreenY()),0xFFE0,0x0000)
        else:
            rcu.SetLCDClear(0x0000);

task1()
```

## 5、设置字体大小（默认字体）

（1）功能：设置屏幕显示字体大小
（2）参数：“默认字体”“中字体”“大字体”“特大字体”“超大字体”，字体大小

**范例：显示预览**
显示默认、中、大三种规格的字体

```python
import rcu

def task1():
    rcu.SetFontSize(0);
    rcu.SetDisplayString(1,"默认",0xFFE0,0x0000)
    rcu.SetFontSize(1);
    rcu.SetDisplayString(2,"中",0xFFE0,0x0000)
    rcu.SetFontSize(2);
    rcu.SetDisplayString(3,"大",0xFFE0,0x0000)

task1()
```

## 6、在屏幕第（）行显示数字（）

（1）功能：在显示屏设定的行位置显示数字，显示方式为右对齐
（2）参数：1-20
（3）参数：0-1030，能输入要显示的数字

**范例：显示数字**
在屏幕显示“123456”数字

```python
import rcu

def task1():
    rcu.SetDisplayVar(1,123456,0xFFE0,0x0000);

task1()
```

## 7、在屏幕第（）行显示字符（）

（1）功能：在显示屏设定的行位置显示字符，显示方式为左对齐
（2）参数：1-20
（3）参数：字符串文字，不区分中英文，限制输入20个

**范例：显示字符**
分别显示中文和英文字符

```python
import rcu

def task1():
    rcu.SetDisplayString(1,"中鸣科技中鸣科技中鸣科技中鸣科技中鸣科技",0xFFE0,0x0000)
    rcu.SetDisplayString(2,"zmrobozmrobozmrobozm",0xFFE0,0x0000)

task1()
```

## 8、绘制图片X（）Y（）文件名（）缩放比例（）

（1）功能：在显示屏设定的坐标位置显示图片，起始位置为图片的左上角
（2）参数：0-239，X坐标
（3）参数：0-319，Y坐标
（4）参数：图片文件名，图片应预先存入到磁盘控制器内。
（5）参数：0-3，0是不缩放，1是缩放1/2，2是缩放1/4，3是缩放1/8
支持显示标准有损压缩JPEG图片和无损16位/24位/32位真彩BMP图片

**范例：显示图片**
在右顶角以不缩放的形式显示文件名为“a1.jpg”的图片

```python
import rcu

def task1():
    rcu.SetDisplayPicture(0,0,"a1.jpg",0);

task1()
```

## 9、在屏幕X（）Y（）显示数字（）颜色（）背景（）

（1）功能：在显示屏设定的坐标位置显示数字，数字和背景颜色可设定
（2）参数：0-239，X坐标
（3）参数：0-319，Y坐标
（4）参数：输入最长30个要显示的数字
（5）参数：字体颜色
（6）参数：背景颜色

```plain
rcu.SetDisplayVarXY(1,1,10,0xFFE0,0x0000)
```

## 10、绘制点X（）Y（）颜色黄色

（1）功能：在显示屏设定的坐标位置显示一个坐标点
（2）参数：0-239，X坐标
（3）参数：0-319，Y坐标
（4）参数：点的颜色

**范例：点阵表情**
用坐标点显示一个“∵”表情

```python
import rcu

def task1():
    rcu.SetLCDDot(10,10,0xFFE0);
    rcu.SetLCDDot(20,10,0xFFE0);
    rcu.SetLCDDot(15,15,0xFFE0);

task1()
```

## 11、绘制直线X（）Y（）角度（）长度（）颜色黄色

（1）功能：从显示屏设定的坐标位置开始，朝设定的角度方向绘制一条线段
（2）参数：0-239，X坐标
（3）参数：0-319，Y坐标
（4）参数：0-360，旋转角度
（5）参数：长度，一个单位长度等于一个像素点
（6）参数：线段颜色

**范例：点阵笑脸**
用坐标点和线段组合出笑脸

```python
import rcu

def task1():
    rcu.SetLCDDot(10,10,0xFFE0);
    rcu.SetLCDDot(30,10,0xFFE0);
    rcu.SetLCDLine(20,20,135,5,0xFFE0);
    rcu.SetLCDLine(20,20,45,8,0xFFE0);

task1()
```

## 12、绘制圆X（）Y（）半径（）颜色黄色

（1）功能：以显示屏设定的坐标位置为圆心，绘制一个实心圆形
（2）参数：0-239，X坐标
（3）参数：0-319，Y坐标
（4）参数：一个单位半径长度等于一个像素点
（5）参数：圆的颜色

**范例：画圆**
在屏幕的中央(120,160)画半径长度为15的黄色实心圆

```python
import rcu

def task1():
    rcu.SetLCDSolidCircle(120,160,15,0xFFE0);

task1()
```

## 13、绘制矩形X（）Y（）宽（）高（）线宽（）颜色黄色

（1）功能：绘制一个空心矩形，左上角为显示屏设定的坐标位置
（2）参数：0-239，X坐标
（3）参数：0-319，Y坐标
（4）参数：1-240，宽
（5）参数：1-320，高
（6）参数：一个单位线宽等于一个像素点的宽
（7）参数：线的颜色

**范例：画空心矩形**
画6个不同颜色的空心矩形

```python
import rcu

def task1():
    rcu.SetLCDRectangle2(30,50,60,60,1,0xF800);
    rcu.SetLCDRectangle2(90,50,60,60,1,0x07E0);
    rcu.SetLCDRectangle2(150,50,60,60,1,0x001F);
    rcu.SetLCDRectangle2(30,110,60,60,1,0xFFE0);
    rcu.SetLCDRectangle2(90,110,60,60,1,0xF81F);
    rcu.SetLCDRectangle2(150,110,60,60,1,0x07FF);

task1()
```

## 14、绘制实心矩形X（）Y（）宽（）高（）颜色黄色

（1）功能：绘制一个实心矩形，左上角为显示屏设定的坐标位置
（2）参数：0-239，X坐标
（3）参数：0-319，Y坐标
（4）参数：1-240，宽
（5）参数：1-320，高
（6）参数：矩形的颜色

**范例：画实心矩形**
画4个不同颜色的实心矩形

```python
import rcu

def task1():
    rcu.SetLCDFilledRectangle2(0,0,50,50,0xFFE0);
    rcu.SetLCDFilledRectangle2(25,25,50,50,0x07FF);
    rcu.SetLCDFilledRectangle2(50,50,50,50,0xFFFF);
    rcu.SetLCDFilledRectangle2(75,75,50,50,0x001F);

task1()
```

------

# **播放**

## 1、播放MP3文件夹名（）MP3名（）

（1）功能：播放MP3磁盘中01文件夹内名称为01的MP3
（2）参数：01-99，文件夹名称
（3）参数：01-99，音频文件名称

**范例：播放MP3**
执行程序，播放01文件夹内名为01的MP3音频文件
```
支持 8/11.025/12/16/22.05/24/32/44.1/48KHZ 采样率的音频文件，支持 MP3、WAV 二种主流的音频格式 
```

```python
import rcu

def task1():
    rcu.SetMp3Play(1,1);

task1()
```

## 2、暂停播放MP3

（1）功能：中断MP3的播放

**范例：播放后停止**
播放MP3，3秒后停止

```python
import rcu

def task1():
    rcu.SetMp3Play(1,1);
    rcu.SetWaitForTime(3)
    rcu.SetMp3Suspend();

task1()
```

## 3、播放声音（）

（1）功能：播放内置MP3文件

**范例：播放内置音频**
播放控制器内置音频：猫
```
内置MP3存放在音频磁盘中，可以直接操作文件更改和删除。但是删除后，这个编程模块就会失效。本质上这个编程模块只是播放指定文件夹中的MP3，删除后会无法播放。
```

```python
import rcu

def task1():
    rcu.SetMp3Play(1, 3)

task1()
```

------

# **无线**

## 1、接收RCU蓝牙数据

功能：控制器通过蓝牙接收另一个控制器发送的数据
返回值：0-255

```plain
rcu.GetBluetoothData()
```

## 2、RCU蓝牙发送数据

功能：控制器通过蓝牙向另一个控制器发送数据
参数值：0-255

```plain
rcu.SetBluetoothData(50)
```

------

# **控制**

## 1、等待（）秒

（1）功能：等待指定时间后，执行其下方程序
（2）参数：等待时间，单位为秒

**范例：一秒后清除显示**
运行程序显示数字1，一秒后清除

```python
import rcu

def task1():
    rcu.SetDisplayVar(1,1,0xFFE0,0x0000);
    rcu.SetWaitForTime(1)
    rcu.SetLCDClear(0x0000);

task1()
```

## 2、重复执行

（1）功能：重复执行其包含的程序

**范例：重复显示随机数**
重复执行：每过一秒在第1行显示1到10的任一随机数

```python
import rcu

def task1():
    while True:
        rcu.SetDisplayVar(1,rcu.GetRandom(1,10),0xFFE0,0x0000);
        rcu.SetWaitForTime(1)
        rcu.SetLCDClear(0x0000);

task1()
```

## 3、重复执行（）次

（1）功能：重复执行其包含的程序指定次数，默认值为10次
（2）参数：循环次数，数值须为正整数

**范例：显示数值**
每过一秒就显示变量i的数字并增加1，重复这个过程10次

```python
import rcu
i=0

def task1():
    global i
    i=0
    for count in range(10):
        i+=1
        rcu.SetWaitForTime(1)
        rcu.SetDisplayVar(1,i,0xFFE0,0x0000);

task1()
```

## 4、如果（）那么（）

（1）功能：如果指定条件成立，就执行其包含的程序

**范例：执行条件内程序**
条件成立，屏幕显示数字“10”

```python
import rcu

def task1():
    if (2>1):
        rcu.SetDisplayVar(1,10,0xFFE0,0x0000);

task1()
```

## 5、如果（）那么（）否则

（1）功能：如果指定条件成立，就执行其包含的程序1，否则执行程序2

**范例：不满足条件，执行否则内程序**
条件不成立，屏幕显示数字“20”

```python
import rcu

def task1():
    if (1>2):
        rcu.SetDisplayVar(1,10,0xFFE0,0x0000);
    else:
        rcu.SetDisplayVar(1,20,0xFFE0,0x0000);

task1()
```

## 6、等待（）成立

（1）功能：等待指定条件成立，执行其后程序

**范例：等待条件**
等待屏幕被触摸，显示字符“Hello”

```python
import rcu

def task1():
    while not rcu.GetTouchScreen():
        pass
    rcu.SetDisplayString(1,"Hello",0xFFE0,0x0000)

task1()
```

## 7、重复执行直到（）

（1）功能：重复执行其包含的程序，直到指定条件成立，而后停止程序。

**范例：重复执行，直到满足条件**
重复显示数字“1”，直到满足触摸条件，显示数字“2”

```python
import rcu

def task1():
    while not rcu.GetTouchScreen():
        rcu.SetDisplayVar(1,1,0xFFE0,0x0000);
    rcu.SetDisplayVar(1,2,0xFFE0,0x0000);

task1()
```

------

# **运算**

## 1、（）+（）

（1）功能：执行加法运算
（2）返回值：运算后的数值

**范例：显示加法运算结果**
显示“5+5”的运算结果

```python
import rcu

def task1():
    rcu.SetDisplayVar(1,(5 + 5),0xFFE0,0x0000);

task1()
```

## 2、（）-（）

（1）功能：执行减法运算
（2）返回值：运算后的数值

**范例：显示减法运算结果**
显示“10-5”的运算结果

```python
import rcu

def task1():
    rcu.SetDisplayVar(1,(10 - 5),0xFFE0,0x0000);

task1()
```

## 3、（）*（）

（1）功能：执行乘法运算
（2）返回值：运算后的数值

**范例：显示乘法运算结果**
显示“5×5”的运算结果

```python
import rcu

def task1():
    rcu.SetDisplayVar(1,(5 * 5),0xFFE0,0x0000);

task1()
```

## 4、（）/（）

（1）功能：执行除法运算
（2）返回值：运算后的数值

**范例：显示除法运算结果**
显示“5÷5”的运算结果

```python
import rcu

def task1():
    rcu.SetDisplayVar(1,(5 / 5),0xFFE0,0x0000);

task1()
```

## 5、在（）和（）之间取随机数

（1）功能：在指定区间内取随机数
（2）返回值：指定区间内的随机数

**范例：显示随机数**
随机显示一个范围在1-10之间的数

```python
import rcu

def task1():
    rcu.SetDisplayVar(1,rcu.GetRandom(1,10),0xFFE0,0x0000);

task1()
```

## 6、（）>（）

（1）功能：如果指定参数的值大于指定值，报告条件成立
（2）返回值：0和1；0为不成立，1为成立

**范例：比较大小显示数值**
若条件成立，显示数字“1”，否则显示数字“0”

```python
import rcu

def task1():
    if (2>1):
        rcu.SetDisplayVar(1,1,0xFFE0,0x0000);
    else:
        rcu.SetDisplayVar(1,0,0xFFE0,0x0000);

task1()
```

## 7、（）<（）

（1）功能：如果指定参数的值小于指定值，报告条件成立
（2）返回值：0和1；0为不成立，1为成立

**范例：比较大小显示数值**
若条件成立，显示数字“1”，否则显示数字“0”

```python
import rcu

def task1():
    if (2<1):
        rcu.SetDisplayVar(1,1,0xFFE0,0x0000);
    else:
        rcu.SetDisplayVar(1,0,0xFFE0,0x0000);

task1()
```

## 8、（）=（）

（1）功能：如果指定参数的值等于指定值，报告条件成立

**范例：相等检测**
若两个随机数相等，那么显示“随机数一致”，否则显示“随机数不一致”

```python
import rcu

def task1():
    if (rcu.GetRandom(1,3)==rcu.GetRandom(1,3)):
        rcu.SetDisplayString(1,"随机数一致",0xFFE0,0x0000)
    else:
        rcu.SetDisplayString(1,"随机数不一致",0xFFE0,0x0000)

task1()
```

## 9、（）与（）

（1）功能：指定两个条件同时成立，报告条件成立

**范例：与逻辑的使用**
条件均满足，显示“两个条件均成立”，否则显示“最少一个条件不成立”

```python
import rcu

def task1():
    if ((rcu.GetRandom(1,3)<0) and (rcu.GetRandom(1,3)>0)):
        rcu.SetDisplayString(1,"两个条件均成立",0xFFE0,0x0000)
    else:
        rcu.SetDisplayString(1,"最少一个条件不成立",0xFFE0,0x0000)

task1()
```

## 10、（）或（）

（1）功能：指定两个条件其中一个成立，报告条件成立

**范例：或逻辑的使用**
满足条件一条或以上时，显示“最少一个条件成立”，否则显示“两个条件均不成立”

```python
import rcu

def task1():
    if ((rcu.GetRandom(1,3)>2) or (rcu.GetRandom(1,3)<2)):
        rcu.SetDisplayString(1,"最少一个条件成立",0xFFE0,0x0000)
    else:
        rcu.SetDisplayString(1,"两个条件均不成立",0xFFE0,0x0000)

task1()
```

## 11、（）不成立

（1）功能：指定条件不成立，报告条件成立

**范例：反向返回条件状态**
条件不成立时，显示“没触摸”，否则显示“触摸中”

```python
import rcu

def task1():
    while True:
        if not(rcu.GetTouchScreen()):
            rcu.SetDisplayString(1,"没触摸",0xFFE0,0x0000)
        else:
            rcu.SetDisplayString(1,"触摸中",0xFFE0,0x0000)

task1()
```

## 12、连接（）和（）

功能：报告两个字符串合并结果。
返回值：字符

## 13、（）的第（）个字符

功能：报告指定字符串的指定位置字符。

## 14、（）的字符数

功能：报告指定字符串的字符数。

## 15、（）包含（）？

功能：如果指定字符串包含另一指定字符串，报告条件成立。
返回值：0和1；0为不成立，1为成立。

## 16、（）除以（）的余数

功能：报告指定两数相除的余数。
返回值：运算后的数值。

```plain
%
```

## 17、四舍五入（）

功能：报告指定数字四舍五入的值。

```plain
round()
```

## 18、绝对值（）

功能：报告指定数字的指定数学运算结果。
参数值：fabs、floor、ceil、sqrt、sin、cos、tan、asin、aco、atan、ln、log、e、10
返回值：运算后的数值。

```plain
math.fabs()
```

------

# [AI模块](https://www.yuque.com/zmrobo/robocode/oiko54)