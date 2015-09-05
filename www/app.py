#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# app.py

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
# 使用aiohttp框架
from aiohttp import web

# http的"/"响应index
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

# 初始化http响应程序
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    #建立"/"响应为index
    app.router.add_route('GET', '/', index)
    #建立协程响应服务器，地址为本机，端口号为9000
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    #记录info级日志信息
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

#建立协程响应循环
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()