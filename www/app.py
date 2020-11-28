#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'shinozhu'

import logging; logging.basicConfig(level=logging.INFO)

import asyncio,time
from datetime import datetime
from aiohttp import web

async def index(request):
    return web.Response(body='<h1>Awesome APP</h1>', content_type='text/html')

def init():
    app = web.Application()
    app.router.add_get("/", index)
    logging.info('Server started at http://127.0.0.1...')
    web.run_app(app, host='127.0.0.1', port=8080)

init()