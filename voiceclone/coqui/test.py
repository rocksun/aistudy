import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
# Text to speech to a file
text="""
假演讲者“摧毁”程序员大会
真假女演讲嘉宾引争议，大会被取消，科技圈中的女性状态如何？

译自 Meet ‘Anna Boyko’: How a Fake Speaker Blew up DevTernity，作者 Richard Gall 是英格兰东北部的作家兼研究人员。他目前是爱丁堡大学的研究生，正在学习数字社会学，也是“当我们谈论......”(What We Talk About When...)的联合主持人。

一个会议因包含不存在的女性发言人而受批评，并最终被取消。

感谢 Gergely Orosz(Pragmatic Engineer 通讯的作者)的调查工作，原计划于 12 月初举行的 DevTernity 线上会议现在卷入一场争议，并吸引到软件工程领域的许多有影响力人士关注。
"""
tts.tts_to_file(text=text, speaker_wav="./shuhui.wav", language="zh-cn", file_path="output2.wav")