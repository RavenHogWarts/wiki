# -*- coding: utf-8 -*-
"""Sample Configuration
"""

# For Maverick
site_prefix = "/wiki/"
index_page_size = 10
archives_page_size = 30
fetch_remote_imgs = True
category_by_folder = True
locale = "Asia/Shanghai"
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/RavenHogWarts/Theme-For-Maverick.git",
    "branch": "Kepler"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "RavenHogWarts/wiki@gh-pages"
}

# For site
site_name = "ZEROJAN WIKI"
site_logo = "${static_prefix}logo.png"
site_build_date = "2022-06-18T17:20+08:00"
author = "ZEROJAN"
email = "fengyj120@163.com"
author_homepage = "https://ravenhogwarts.github.io"
description = "算是半个有趣的人"
key_words = ['Maverick', 'ZEROJAN', 'Kepler', 'WiKi']
language = 'zh-CN'
external_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/RavenHogWarts",
        "icon": "gi gi-github"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "友人帐",
        "url": "${site_prefix}link/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/RavenHogWarts",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "bdG6jPOLFe19NOSerM9vEJqp-gzGzoHsz",
    "appKey": "AT7QLaEOWmqaI8pcwb8324As",
    "visitor": True,
    "recordIP": True
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="shortcut icon" href="https://cdn.jsdelivr.net/gh/RavenHogWarts/wiki@gh-pages/favicon.ico">
'''

footer_addon = ''

body_addon = ''
