#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/3/17 下午5:35
#   Desc    :   news模块
from model import models
from app import BaseHandler


class NewsHandler(BaseHandler):
    """ news模块
    """
    def get(self):
        news_list = models.News.find_all()
        self.render('news.html', news_list=news_list)
