---
layout: page
title: 友链
slug: link
date: 2022/06/18 22:29
status: publish
author: ZEROJAN
comment: true
categories: 
  - 友链
tags: 
  - link

---
<div id="links">
  <ul>
    <li><a href="https://www.imalan.cn" title="只坚持一种正义。我的正义">AlanDecode
    <img src="https://www.imalan.cn/favicon-32x32.png?v=yyLyaqbyRG" alt="">
    </a></li>
    <li><a href="https://lcxddn.github.io/" title="welcome to my world!">GasL
    <img src="https://lcxddn.github.io/images/apple-touch-icon-next.png" alt="">
    </a></li>
  </ul>
</div>

<style>
  #links ul {
    list-style: none;
    padding: 0px;
    text-align: center;
    border: none;
    background: none;
  }

  #links ul li {
      display: inline-block;
      width: 150px;
      height: 150px;
      margin: 1rem 1rem;
      background-color: rgba(0, 0, 0, 0.04);
      box-shadow: rgba(0, 0, 0, 0.18) 0px 25px 5px;
      border-radius: 5%;
      font-weight: 600;
      text-align: center;
      transition: all 0.5s;
      line-height: 2rem;
      position: relative;
      top: 0px;
  }

  #links ul li:hover {
      box-shadow: rgba(0, 0, 0, 0.3) 0px 20px 10px;
      transition: all 0.5s;
      background-color: #FF5722;
      top: -15px;
  }

  #links ul li:hover a {
      color: white;
      transition: all 0.1s;
  }

  #links ul li:hover .site-friend-link-count {}

  #links ul li a {
      text-decoration: none;
      color: rgba(0, 0, 0, 0.8);
      background: none;
      transition: all 0.5s;
      font-size: 1.2rem
  }

  #links ul li .site-friend-link-count {
      color: white;
      overflow: hidden;
      text-overflow: ellipsis;
      word-spacing: normal;
      word-break: break-word;
      word-wrap: break-word;
      z-index: 1000;
      position: absolute;
      background-color: #FF5722;
      width: 15px;
      height: 15px;
      border-radius: 100%;
      top: -5px;
      right: -7px;
      line-height: 15px;
  }

  #links ul li a img {
      width: 100%;
      height: 100%;
      background-color: white;
      padding: 0px;
  }

  #links ul li a img:hover {
      box-shadow: none;
  }
</style>