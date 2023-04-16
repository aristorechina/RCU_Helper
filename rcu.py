# RCU Helper
# Made By Aristore
# https://github.com/aristorechina/

def GetLeftButton():
    """
    检测控制器的左侧按键是否被按下
    :return:1/0,按下时返回数值1,未按下时返回数值0
    """
    pass

def GetRightButton():
    """
    判断控制器的右侧按键是否被按下
    :return:1/0,按下时返回数值1,未按下时返回数值0
    """
    pass

def GetInMic():
    """
    读取控制器内置麦克风检测的声音大小值
    :return:0-4095,只表示音量大小无具体单位
    """
    pass

def GetInVotage():
    """
    读取控制器此时电源电压值
    :return:0-100,当数据为84时电压为8.4V
    """
    pass

def GetSysTime():
    """
    读取程序运行至今的时间
    :return:数值单位为毫秒,数值1000时为1秒
    """
    pass

def SetSysTime():
    """
    控制器运行程序后，内置时钟归零
    """
    pass

def SetInBeep(on_or_off):
    """
    开启或关闭蜂鸣器
    :param on_or_off:“关”“开”，蜂鸣器开启/蜂鸣器关闭,0/1
    """
    pass

def SetInSound(frequency,time):
    """
    设置蜂鸣器的音调以及播放时长
    :param frequency:“Hight Do”“Hight Re”.....“Low La”"Low Si",Hight代表高音Low代表低音
    :param time:“双拍”“一拍”“半拍”“1/4拍”“1/8拍”,播放音调持续时间
    """
    pass

def GetData(address):
    """
    读取控制器内置数据的数值
    :param address:1-156,对应内置地址名称
    :return:控制器内置地址数据值
    """
    pass

def SetData(address,data):
    """
    将控制器指定内置数据设为指定值
    :param address:1-156,对应内置地址名称
    :param data:1-4095,赋予内置地址数据值
    """
    pass

def SetMotor(port,speed):
    """
    使马达以指定速度运转
    :param port:M1-M4,马达连接端口
    :param speed:-100-100,马达速度数值越大速度越快,0停止,小于0则反转,大于0则正转
    """
    pass

def GetMotorCode(port):
    """
    读取马达编码器数值，起到记录马达转动角度的作用
    :param port:M1-M4,马达连接端口
    :return:马达转动的角度值,数值1表示转动1度,有正负区分
    """
    pass

def SetMotorCode(port):
    """
    将编码器记录的数值清零
    :param port:M1-M4,马达连接端口
    """
    pass

def SetMotorServo(port,speed,angle):
    """
    设置马达转动到指定角度
    :param port:M1-M4,马达连接端口
    :param speed:-100-100,马达速度
    :param angle:马达旋转的角度
    """
    pass

def SetWaitForAngle(port,speed,angle):
    """
    等待马达转动到指定角度，再执行下方程序
    :param port:M1-M4,马达连接端口
    :param speed:-100-100,马达速度
    :param angle:马达旋转的角度
    """
    pass

def SetMotorStraightAngle(port1,port2,speed,bmp):
    """
    使两个马达同步转动指定编码
    :param port1:M1-M4,马达连接端口
    :param port2:M1-M4,马达连接端口
    :param speed:-100-100,马达速度
    :param bmp:0-2147483647,马达旋转的编码值
    """
    pass

def SetCarTurn(port1,port2,speed,bmp):
    """
    使两个马达同步反向转动指定编码
    :param port1:M1-M4,马达连接端口
    :param port2:M1-M4,马达连接端口
    :param speed:-100-100,马达速度
    :param bmp:0-2147483647,马达旋转的编码值
    """
    pass

def SetMotorPower(percentage1,percentage2,percentage3,percentage4):
    """
    设置马达最大功率，用于调整马达差异，重启控制器后会复原
    :param percentage1:-100-100,M1马达功率百分比
    :param percentage2:-100-100,M2马达功率百分比
    :param percentage3:-100-100,M3马达功率百分比
    :param percentage4:-100-100,M4马达功率百分比
    """
    pass

def SetMotorStraight(port1,port2,speed):
    """
    使两个马达同步转动
    :param port1:M1-M4,马达连接端口
    :param port2:M1-M4,马达连接端口
    :param speed:-100-100,马达速度
    """
    pass

def SetMotorStraightTurn(port1,port2,speed,angle):
    """
    使两个马达同步转动指定角度
    :param port1:M1-M4,马达连接端口
    :param port2:M1-M4,马达连接端口
    :param speed:-100-100,马达速度
    :param angle:-100-100,马达旋转的角度
    """
    pass

def SetServo(port,angle):
    """
    使小型舵机转动指定角度
    :param port:P4-P6,小型舵机连接端口
    :param angle:0-180,小型舵机的转动角度
    """
    pass

def SetServoTime(port,angle,time):
    """
    使小型舵机在指定时间内转动指定角度
    :param port:P4-P6,小型舵机连接端口
    :param angle:0-180,小型舵机的转动角度
    :param time:转动时间,数值为毫秒单位,数值1000时为1秒
    """
    pass

def GetTouch(port):
    """
    判断触碰传感器是否被按下
    :param port:P1-P8,传感器端口
    :return:0/1,按下返回1,否则返回0
    """
    pass

def GetColorSensor(port,command):
    """
    读取颜色传感器检测物体的颜色值
    :param port:P1-P8,传感器端口
    :param command:读颜色传感器命令,1~3 读RGB三原色值,4 读颜色识别结果，识别结果与颜色关系:1-红色,2-绿色,3-蓝色,4-黄色,5-黑色,6-白色,5 读RGB888数据,,6~8 读原始RGB数据,9~11 RGB模拟光值,12-14 白平衡比例值,15 色调,16 饱和度,17 亮度,18 保留,19 最大输出值,20-60 设置命令,61-66 颜色扩展参考值,67 白色参考值,68 黑色参考值
    :return:1-6,对应红、绿、蓝、黄、黑、白色
    """
    pass

def GetUltrasound(port):
    """
    读取超声传感器与障碍物的距离值
    :param port:P1-P8,传感器端口
    :return:7-180,单位cm
    """
    pass

def GetLightSensor(port):
    """
    读取光电传感器检测物体的颜色深度值
    :param port:P1-P8,传感器端口
    :return:0-4095,数值随着被测物体颜色越深而减少
    """
    pass

def GetLightSensorData(port):
    """
    判断光电传感器检测的物体颜色深度是否小于阈值
    :param port:P1-P8,传感器端口
    :return:0/1,低于阈值返回1,否则返回0
    """
    pass

def SetLightSensorLed(port,on_or_off):
    """
    开启或关闭光电传感器的LED灯
    :param port:P1-P8,传感器端口
    :param on_or_off:“关”“开”，参数为“开”时开启灯，参数为“关”时关闭灯
    """
    pass

def Set3CLed(port,color):
    """
    设置彩灯模块的显示颜色
    :param port:P1-P8,传感器端口
    :param color:1-7,对应“红色”“绿色”“蓝色”“黄色”“紫色”“青色”“白色”,彩灯颜色
    """
    pass

def GetBluetoothData():
    """
    控制器通过蓝牙接收另一个控制器发送的数据
    :return:0-255
    """
    pass

def SetBluetoothData(data):
    """
    控制器通过蓝牙向另一个控制器发送数据
    :param data:0-255
    """
    pass

def SetWaitForTime(time):
    """
    等待指定时间后，执行其下方程序
    :param time:等待时间，单位为秒
    """
    pass

def GetRandom(a,b):
    """
    重复执行其包含的程序,生成a到b的任一随机数(整数)
    :param a:起始
    :param b:终止
    """
    pass

def GetTouchScreen():
    """
    判断屏幕是否被触摸
    :return:1/0,触摸时返回1,未触摸时返回0
    """
    pass

def GetTouchScreenX():
    """
    读取屏幕触摸点的X轴坐标值
    :return:1-240,屏幕从左往右,数值从小到大,无触摸时值为0
    """
    pass

def GetTouchScreenY():
    """
    读取屏幕触摸点的Y轴坐标值
    :return:1-320,屏幕从上往下,数值从小到大,无触摸时值为0
    """
    pass

def SetLCDClear(color):
    """
    清除显示屏全部的显示内容，背景颜色设置成黄色
    :param color:清屏后的背景颜色(RGB565)
    """
    pass

def SetDisplayString(size,data,color,bgcolor):
    """
    设置屏幕显示字体大小
    :param size:1-5,对应“默认字体”“中字体”“大字体”“特大字体”“超大字体”,字体大小
    :param data:内容(字符串，记得引号"")
    :param color:字体颜色
    :param bgcolor:背景颜色
    """
    pass

def SetDisplayVar(line_numbers,data,color,bgcolor):
    """
    在显示屏设定的行位置显示数字，显示方式为右对齐
    :param line_numbers:行号1-20
    :param data:能输入要显示的数字(整型)
    :param color:字体颜色
    :param bgcolor:背景颜色
    """
    pass

def SetDisplayString(line_numbers,data,color,bgcolor):
    """
    在显示屏设定的行位置显示字符，显示方式为左对齐
    :param line_numbers:行号1-20
    :param data:字符串文字(记得引号""),不区分中英文,限制输入20个
    :param color:字体颜色
    :param bgcolor:背景颜色
    """
    pass

def SetDisplayPicture(x,y,name,scaling):
    """
    在显示屏设定的坐标位置显示图片，起始位置为图片的左上角
    支持显示标准有损压缩JPEG图片和无损16位/24位/32位真彩BMP图片
    :param x:0-239,X坐标
    :param y:0-319,Y坐标
    :param name:图片文件名(字符串，例如"a1.jpg"),图片应预先存入到磁盘控制器内
    :param scaling:0-3,0是不缩放,1是缩放1/2,2是缩放1/4,3是缩放1/8
    """
    pass

def SetDisplayVarXY(x,y,data,color,bgcolor):
    """
    在显示屏设定的坐标位置显示数字，数字和背景颜色可设定
    :param x:0-239,X坐标
    :param y:0-319,Y坐标
    :param data:输入最长30个要显示的数字
    :param color:字体颜色
    :param bgcolor:背景颜色
    """
    pass

def SetLCDDot(x,y,color):
    """
    在显示屏设定的坐标位置显示一个坐标点
    :param x:0-239,X坐标
    :param y:0-319,Y坐标
    :param color:点的颜色
    """
    pass

def SetLCDLine(x,y,angle,length,color):
    """
    从显示屏设定的坐标位置开始，朝设定的角度方向绘制一条线段
    :param x:0-239,X坐标
    :param y:0-319,Y坐标
    :param angle:0-360,旋转角度
    :param length:长度，一个单位长度等于一个像素点
    :param color:线段颜色
    """
    pass

def SetLCDSolidCircle(x,y,r,color):
    """
    以显示屏设定的坐标位置为圆心，绘制一个实心圆形
    :param x:0-239,X坐标
    :param y:0-319,Y坐标
    :param r:一个单位半径长度等于一个像素点
    :param color:圆的颜色
    """
    pass

def SetLCDRectangle2(x,y,w,h,line_weight,color):
    """
    绘制一个空心矩形，左上角为显示屏设定的坐标位置
    :param x:0-239,X坐标
    :param y:0-319,Y坐标
    :param w:1-240,宽
    :param h:1-320,高
    :param line_weight:一个单位线宽等于一个像素点的宽
    :param color:线的颜色
    """
    pass

def SetLCDFilledRectangle2(x,y,w,h,color):
    """
    绘制一个实心矩形，左上角为显示屏设定的坐标位置
    :param x:0-239,X坐标
    :param y:0-319,Y坐标
    :param w:1-240,宽
    :param h:1-320,高
    :param color:矩形的颜色
    """
    pass

def SetMp3Play(folder,file):
    """
    播放MP3磁盘中01文件夹内名称为01的MP3
    支持 8/11.025/12/16/22.05/24/32/44.1/48KHZ 采样率的音频文件，支持 MP3、WAV 二种主流的音频格式
    :param folder:01-99,文件夹名称
    :param file:01-99,音频文件名称
    """
    pass

def SetMp3Suspend():
    """
    中断MP3的播放
    """
    pass

def SetMp3Play(folder,mp3num):
    """
    播放内置MP3文件
    内置MP3存放在音频磁盘中,可以直接操作文件更改和删除。但是删除后,这个编程模块就会失效。本质上这个编程模块只是播放指定文件夹中的MP3,删除后会无法播放。
    """
    pass

def SetWaitForAICamData(a,b):
    """
    等待AI模块切换至指定识别模式(AI硬件需连接在控制器串口,E6为P8,M6为P5)
    :param a:可选模式如下
    :param b:预留参数
    """
    pass

def GetAICamData():
    """
    读取AI视觉模块中对应14位返回数据信息
    """
    pass