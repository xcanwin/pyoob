# XNetcat
## 简介
- 基于Python的Netcat服务器, 用于接收OOB与SSRF请求, 兼容TCP与UDP.

## 作用
- 监听端口, 输出接收到的数据.
- 兼容TCP与UDP.
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
