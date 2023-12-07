from TTS.api import TTS

# model_name = "tts_models/zh-CN/baker/tacotron2-DDC-GST"
# model_name = "tts_models/multilingual/multi-dataset/your_tts"
model_name = "tts_models/multilingual/multi-dataset/bark"

tts = TTS(model_name)
tts = TTS(model_name, progress_bar=False)
# Run TTS
# tts.tts_to_file(text="This is from chinese!", speaker_wav="rocksun.wav", language="en", file_path='output.wav')
tts.tts_to_file(text="测试一下中文语音", speaker_wav="rocksun.wav", language="zh", file_path='output-zh.wav')