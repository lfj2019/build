# -*- coding: utf-8 -*-
# 读Wave文件并且绘制波形
import wave
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 中文显示
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 打开WAV音频
# f = wave.open(r"E:\临时文件\声音检测-论文\English_Paper\CarMoving8000.wav",'rb')
# f = wave.open(r'C:\Users\Administrator\Desktop\voice\input_file1.wav', 'rb')
f = wave.open(r'C:\Users\Administrator\Desktop\voice\outfile11.wav', 'rb')
# 读取格式信息
# (声道数、量化位数、采样频率、采样点数、压缩类型、压缩类型的描述)
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
# nchannels通道数 = 2
# sampwidth量化位数 = 2
# framerate采样频率 = 8000
# nframes采样点数 = 1008536

# 读取nframes个数据，返回字符串格式
str_data = f.readframes(nframes)
f.close()

# 将字符串转换为数组，得到一维的short类型的数组
wave_data = np.fromstring(str_data, dtype=np.short)

# 赋值的归一化
wave_data = wave_data*1.0/(max(abs(wave_data)))

# 整合左声道和右声道的数据
wave_data = np.reshape(wave_data, [nframes, nchannels])
# wave_data.shape = (-1, 2)   # -1的意思就是没有指定,根据另一个维度的数量进行分割

# 最后通过采样点数和取样频率计算出每个取样的时间
time = np.arange(0, nframes) * (1.0 / framerate)

plt.figure()
# 左声道波形
plt.subplot(3, 1, 1)
plt.plot(time, wave_data[:, 0])
plt.xlabel("时间/S")
plt.ylabel("幅度")
# plt.title("Left channel")
plt.grid()  # 标尺
'''
plt.subplot(3,1,3)
# 右声道波形
plt.plot(time, wave_data[:, 1], c ="g")
plt.xlabel("time (seconds)")
plt.ylabel("Amplitude")
plt.title("Left channel")
plt.title("right channel")
plt.grid()
'''
plt.show()