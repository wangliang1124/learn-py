最近我家女神提了一个需求，要我把她在亲宝宝上上传的闺女的照片和视频全下载下来，因为她把手机上的都删了，万一哪天这个平台over了，就没有备份了，所以我利用周末的时间在家学习Python，准备搞一个爬虫爬取一下。

爬虫的原理本身不复杂，基本上就几个步骤：
*   1.分析要爬取的网站或APP
*   2.使用 requests 库发出 http 或 https请求
*   3.使用 BeautifulSoup 提取需要的内容，类似JS的DOM操作
*   4.写入本地文件

首先打开charles抓包工具，手机设置代理，打开亲宝宝APP，发现几乎所有请求都是https请求。于是Charles给出了SSLHandshake:Received Fatal Alert:certificate_unknown的提示。

应该是CA证书的问题，于是我在手机上下载了charles证书并安装，却发现问题依旧。继续google，原来android7之后安全策略调整了，即使有信任的证书也不行，除非是系统级别的证书。网上给出了解决办法，无奈我的手机是miui 10.2稳定版，无法root，除非刷成开发部。

卒。

然后我发现亲宝宝提供了pc版的，貌似可以备份。