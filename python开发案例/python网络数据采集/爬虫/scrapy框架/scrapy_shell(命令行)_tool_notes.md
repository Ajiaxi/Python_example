## 配置设置
Scrapy将scrapy.cfg在标准位置的ini样式文件中查找配置参数：
```
1. /etc/scrapy.cfg或c:\scrapy\scrapy.cfg（系统范围），
2. ~/.config/scrapy.cfg（$XDG_CONFIG_HOME）和~/.scrapy.cfg（$HOME）用于全局（用户范围）设置，以及
3. scrapy.cfg 在一个scrapy项目中。
```
这些文件的设置按列出的首选顺序进行合并：用户定义的值的优先级高于系统默认值，而在定义时，项目范围的设置将覆盖所有其他设置。

Scrapy也可以理解，并且可以通过一些环境变量进行配置。目前这些是：
```
SCRAPY_SETTINGS_MODULE
SCRAPY_PROJECT
SCRAPY_PYTHON_SHELL
```

## Scrapy项目的默认结构
```angular2html
scrapy.cfg
myproject/
    __init__.py
    items.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...
```
scrapy.cfg文件所在的目录称为项目根目录。该文件包含定义项目设置的python模块的名称。这是一个例子：
```angular2html
[ settings ] 
default  =  myproject.settings
```
## 使用scrapy工具
```angular2html
Scrapy X.Y - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  crawl         Run a spider
  fetch         Fetch a URL using the Scrapy downloader
[...]
```
## 创建项目
```angular2html
scrapy  startproject  myproject  [ project_dir ]
```
这将在project_dir目录下创建一个Scrapy项目。如果project_dir没有指定，project_dir将会相同myproject

接下来，你进入新的项目目录：
```
cd  project_dir
```
## 控制项目
例如，要创建一个新的蜘蛛：
```angular2html
scrapy genspider mydomain mydomain.com
```
### genspider
```
句法： scrapy genspider [-t template] <name> <domain>
需要项目：否
```
在当前文件夹或当前项目的spiders文件夹中创建一个新的蜘蛛，如果从项目中调用。该<name>参数设置为蜘蛛name，同时<domain>用于生成allowed_domains和start_urls蜘蛛的属性

Usage example:
```
$ scrapy genspider -l
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed

$ scrapy genspider example example.com
Created spider 'example' using template 'basic'

$ scrapy genspider -t crawl scrapyorg scrapy.org
Created spider 'scrapyorg' using template 'crawl'
```
还要记住，一些命令在从项目内部运行时可能会有稍微不同的行为。例如，user_agent如果要获取的URL与某个特定的蜘蛛相关联，则fetch命令将使用蜘蛛重载行为（例如该属性来覆盖用户代理）。这是有意的，因为该fetch命令旨在用于检查蜘蛛正在下载页面
### check
```
句法： scrapy check [-l] <spider>
需要项目：是的
```
执行合同检查。

用法示例：
```
$ scrapy check -l
first_spider
  * parse
  * parse_item
second_spider
  * parse
  * parse_item

$ scrapy check
[FAILED] first_spider:parse_item
>>> 'RetailPricex' field is missing

[FAILED] first_spider:parse
>>> Returned 92 requests, expected 0..4
```
### list
```
句法： scrapy list
需要项目：是的
```
列出当前项目中的所有可用蜘蛛。输出是每行一个蜘蛛。

用法示例：
```angular2html
$ scrapy list
spider1
spider2
```

### edit
```
句法： scrapy edit <spider>
需要项目：是的
```
使用EDITOR环境变量中定义的编辑器或（如果未设置）EDITOR设置编辑给定的蜘蛛。

该命令仅作为最常见情况的便捷快捷方式提供，开发人员当然可以自由选择任何工具或IDE来编写和调试蜘蛛。

用法示例：
```angular2html
$ scrapy edit spider1
```

### fetch
```
句法： scrapy fetch <url>
需要项目：否
```
使用Scrapy下载器下载给定的URL，并将内容写入标准输出。

这个命令的有趣之处在于它会获取蜘蛛将如何下载它的页面。例如，如果蜘蛛具有USER_AGENT 覆盖用户代理的属性，那么它将使用该属性。

所以这个命令可以用来“看”蜘蛛如何获取某个页面。

如果在项目之外使用，则不会应用特定的每蜘蛛行为，并且只会使用默认的Scrapy下载器设置。

支持的选项：
```
--spider=SPIDER：绕过蜘蛛自动检测并强制使用特定的蜘蛛
--headers：打印响应的HTTP标头而不是响应的正文
--no-redirect：不要按照HTTP 3xx重定向（默认是跟随它们）
```
用法示例：
```
$ scrapy fetch --nolog http://www.example.com/some/page.html
[ ... html content here ... ]

$ scrapy fetch --nolog --headers http://www.example.com/
{'Accept-Ranges': ['bytes'],
 'Age': ['1263   '],
 'Connection': ['close     '],
 'Content-Length': ['596'],
 'Content-Type': ['text/html; charset=UTF-8'],
 'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],
 'Etag': ['"573c1-254-48c9c87349680"'],
 'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],
 'Server': ['Apache/2.2.3 (CentOS)']}
```
### view
```
句法： scrapy view <url>
需要项目：否
```
在浏览器中打开给定的URL，因为您的Scrapy蜘蛛会“看到”它。有时蜘蛛会看到与普通用户不同的页面，所以这可以用来检查蜘蛛“看到”什么，并确认它是你期望的。

支持的选项：
```
--spider=SPIDER：绕过蜘蛛自动检测并强制使用特定的蜘蛛
--no-redirect：不要按照HTTP 3xx重定向（默认是跟随它们）
```
用法示例：
```angular2html
$ scrapy view http://www.example.com/some/page.html
[ ... browser starts ... ]
```
### shell   [官方文档](http://scrapy-chs.readthedocs.io/zh_CN/latest/topics/shell.html)
```
句法： scrapy shell [url]
需要项目：否
```
启动给定URL（如果给定）的Scrapy shell，如果没有给出URL，则为空。同时支持UNIX风格的本地文件路径，无论是相对 ./或../前缀或绝对文件路径。请参阅Scrapy shell了解更多信息。

支持的选项：
```
--spider=SPIDER：绕过蜘蛛自动检测并强制使用特定的蜘蛛
-c code：评估shell中的代码，打印结果并退出
--no-redirect：不要按照HTTP 3xx重定向（默认是跟随它们）; 这只会影响您作为命令行参数传递的URL; 一旦你在shell中，fetch(url)默认情况下仍然会遵循HTTP重定向。
```
用法示例：
```angular2html
$ scrapy shell http://www.example.com/some/page.html
[ ... scrapy shell starts ... ]

$ scrapy shell --nolog http://www.example.com/ -c '(response.status, response.url)'
(200, 'http://www.example.com/')

# shell follows HTTP redirects by default
$ scrapy shell --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
(200, 'http://example.com/')

# you can disable this with --no-redirect
# (only for the URL passed as command line argument)
$ scrapy shell --no-redirect --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
(302, 'http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F')
```
### parse
```
句法： scrapy parse <url> [options]
需要项目：是的
```
获取给定的URL并用处理它的蜘蛛解析它，使用通过--callback选项传递的方法，或者parse如果没有给出。

支持的选项：
```
--spider=SPIDER：绕过蜘蛛自动检测并强制使用特定的蜘蛛
--a NAME=VALUE：设置蜘蛛参数（可能重复）
--callback或者-c：spider方法用作解析响应的回调
--pipelines：通过管道处理物品
--rules或者-r：使用CrawlSpider 规则来发现用于解析响应的回调（即spider方法）
--noitems：不要显示被刮的物品
--nolinks：不显示提取的链接
--nocolour：避免使用pygments对输出进行着色
--depth或者-d：递归地遵循请求的深度级别（默认值：1）
--verbose或-v：显示每个深度级别的信息
```
用法示例：
```
$ scrapy parse http://www.example.com/ -c parse_item
[ ... scrapy log lines crawling example.com spider ... ]

>>> STATUS DEPTH LEVEL 1 <<<
# Scraped Items  ------------------------------------------------------------
[{'name': u'Example item',
 'category': u'Furniture',
 'length': u'12 cm'}]

# Requests  -----------------------------------------------------------------
[]
```
### settings
```
句法： scrapy settings [options]
需要项目：否
```
获取Scrapy设置的值。

如果在项目中使用它将显示项目设置值，否则将显示该设置的默认Scrapy值。

使用示例
```angular2html
$ scrapy settings --get BOT_NAME
scrapybot
$ scrapy settings --get DOWNLOAD_DELAY
0
```
### runspider
```
句法： scrapy runspider <spider_file.py>
需要项目：否
```
运行一个独立于Python文件的蜘蛛，无需创建一个项目。

使用示例
```angular2html
$ scrapy runspider myspider.py
[ ... spider starts crawling ... ]
```
### 通过setup.py入口点注册命令
注意:这是一个实验功能，谨慎使用
您还可以通过scrapy.commands在库setup.py 文件的入口点添加一个部分来从外部库添加Scrapy命令 。

以下示例添加my_command命令
```angular2html
from setuptools import setup, find_packages

setup(name='scrapy-mymodule',
  entry_points={
    'scrapy.commands': [
      'my_command=my_scrapy_module.commands:MyCommand',
    ],
  },
 )
```

