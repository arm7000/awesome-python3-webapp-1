#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '

from coroweb import get  
import asyncio  
 
@get('/')  
async def index(request):  
    return '<h1>Awesome</h1>'  
 
@get('/hello')  
async def hello(request):  
    return '<h1>hello!</h1>'  