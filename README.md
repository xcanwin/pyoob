## 简介

- 基于Python的轻量级Netcat服务器
- 用于接收HTTP、OOB、SSRF等多种请求
- 同时监听TCP与UDP两种协议
- 持续获取结果
- 日志记录

## 灵感来源

- 由于经常fuzzing Out-of-Band攻击和SSRF攻击，需要用NCAT，但是得输入繁杂的命令，又得频繁地ctrl+c来终止服务端，还得频繁的暂停burp的http请求或者java程序来终止客户端，又不确定是TCP协议还是UDP协议得尝试-u参数，最后想记录历史情况还得输入更繁杂的命令，记录的历史还没有客户端来源。
- 根据自己以上种种痛点写了这个小工具，提高挖洞效率，顺便开源出来。

## 作用

- 监听端口, 输出接收到的数据.
- 同时支持TCP与UDP.
- 功能类似于ncat的TCP服务端 ncat -l -k -v -o netcat.log --append-output -p 4444
- 同时类似于ncat的UDP服务端 ncat -l -k -v -o netcat.log --append-output -p 4444 -u
- 时刻监听同一端口, 可不限制地接收客户端新建的请求.
- 收到请求后立即断开, 避免占用靶机的程序线程和网络连接.
- 记录历史请求, 保存请求原文.

## 优点

- 代码开源, 安全可控.
- 不依赖第三方库.
- 跨平台.
- 解决了内网环境无法下载ncat的问题.
- 解决了ncat命令过于冗余的问题.
- 解决了ncat监听模式下需要频繁ctrl+c才能终止OOB连接的问题.
- 兼容Python2和Python3.
- 解决了小白不清楚OOB请求类型的痛点, 我说一个数...... TCP与UDP并存.

## 用法

```
python xnetcat.py
python xnetcat.py -P 4444
python xnetcat.py -H 0.0.0.0 -P 4444
python xnetcat.py -H 0.0.0.0 -P 4444 -L xnetcat.log
```
