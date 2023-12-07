# 使用 coqui ai 实现语音 Clone

## 配置 Windows WSL

通过 WSL 配置一个 ubuntu 22 。然后执行：

```shell
apt update && sudo apt upgrade

apt install python3-pip # install pip
```

## 设置代理

模型下载速度太慢的话，最好预先设置代理。

```
root@rocksun:~/.local/share/tts# ip route show
default via 172.27.112.1 dev eth0 
172.27.112.0/20 dev eth0 proto kernel scope link src 172.27.112.191 
```

```
export HTTP_PROXY="http://172.27.112.1:4780"
export HTTPS_PROXY="http://172.27.112.1:4780"
export NO_PROXY="localhost,127.0.0.1"
```

## 命令行

```bash
tts --text "我是一名中国的程序员" \
    --model_name "tts_models/zh-CN/baker/tacotron2-DDC-GST" \
    --out_path ./output.wav
```

## 参考

- A Turorial for the: Tutorial For Nervous Beginners (Win10): https://github.com/coqui-ai/TTS/discussions/1332
- Synthesizing Speech: https://tts.readthedocs.io/en/latest/inference.html
