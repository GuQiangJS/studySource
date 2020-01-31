---
title: macos下使用tunnelblick链接vpn时自动切换使用proxy的方法
date: 2020-01-31
updated: 2020-01-31
tags:
 - macos
 - openvpn
 - tunnelblick
 - pac
 - proxy
categories:
 - 系统设置
mathjax: true
description: <!—more—->
---

因为我是通过链接vpn后再通过局域网中的其他机器共享shadowsocks代理来上网的。
链接vpn后希望能走代理通道上网，而断开vpn则不能再走代理通道（否则无法上网，连百度都上不了）。
但是由于最近vpn链接不是非常稳定，经常会自动断开。
这样就需要不断的手动切换代理设置，一两个小时就设置一次实在是太痛苦😖了。
所以网上找了半天终于找到了相关办法，可以再tunnelblick链接和断开后自动通过脚本对代理设置进行设定。

> 我的mac是通过wifi上网的所以所有的设置只对wifi有效（默认名称为`Wi-Fi`)

具体方法如下：

1. 分别创建两份文件：

    1. `connected.sh`内容如下：
    ```bash
    #!/bin/bash
    sudo networksetup -setautoproxystate "Wi-Fi" on
    sudo networksetup -setautoproxyurl "Wi-Fi" http://192.168.1.255:1080/pac on
    ```
  
    2. `post-disconnect.sh`内容如下：
    ```bash
    #!/bin/bash
    sudo networksetup -setautoproxystate "Wi-Fi"  off
    ```
  
2. 为两份文件赋权限：`chmod u,g+x`
  ```bash
  chmod u,g+x /Users/GuQiang/Desktop/connected.sh /Users/GuQiang/Desktop/post-disconnect.sh
  ```
3. 将两份文件一并放在`/Users/GuQiang/Library/Application Support/Tunnelblick/Configurations/openvpn_setting.tblk/Contents/Resources`下即可。

> 设定方法原始来源：https://groups.google.com/forum/#!msg/tunnelblick-discuss/C7hu6370dtc/xOA706tcAAAJ
