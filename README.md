# smartDNS-Config
The repo is configuration file for smartDNS, it will help you "scientifically" use DNS server. Daily update!

## smartDNS-Config 是什么？

自今年起，在中国，未经批准，建立公用 DNS 是违法行为，由于某些原因，我们少了很多良心的DNS解析服务，现存的 DNS 解析服务 很多都是解析不太准(有污染)情况。

当你科学地使用科学工具完成科学上网的配置，你就会遇到 DNS 问题：

1. 当你使用国内 DNS 你就无法正常解析一些页面
2. 当你使用国外 DNS 则在解析 zhihu，Neteasemusic 等网站的访问效果不理解(解析到这类服务的国外的服务器上，体验差）

所以可以自建一个本地智能 DNS 服务来使得科学上网更舒坦。

本项目提供了基于 [shawn1m/overture](https://github.com/shawn1m/overture) 来提供 DNS 服务，[felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)和 [gaoyifan/china-operator-ip](https://github.com/gaoyifan/china-operator-ip) 所提供的服务来配置相关 match 文件，来使得科学上网的过程更加科学化，符合全国人民的期望和历史的进程。

## 如何使用？

请前往 [shawn1m/overture](https://github.com/shawn1m/overture) 下载符合你系统的 overture 软件，并在该目录下git clone 本项目替换默认配置文件，再运行overture即可。
注意替换本地 DNS 服务器为 overture bindIP 地址。

## 未来

我 正在基于 overture 进行开发([smartDNS](https://github.com/import-yuefeng/smartDNS))，使其获得更多科学特性，不仅仅限于现在的overture 主从模式DNS，而是解决具有 N 个网络出口时，DNS 如何智能选择访问最顺畅的出口，并且能够自动学习产生 Fast-table，用于记录 domain <-> DNS server 的映射，来不断基于用户本地网络情况来优化访问不同网站的DNS解析情况。

敬请期待。

