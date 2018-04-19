#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import orm
import time


logger = logging.getLogger("mainLog")
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(formatter)

logger.addHandler(handler)
# logger1.addHandler(console)

logger.info('start....')



from models import User,Blog,Comment
import asyncio

async def test():
    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop,host='127.0.0.1', port=3306,user='root', password='1234',db='awesome')
    #没有设置默认值的一个都不能少
    # u = User(name='001', email='14422@qq.com', passwd='11z4550690', image='about:blank',id="004")
    tstamp=str(int(time.time())%152400)    
    u = User(name=tstamp, email=tstamp+'@qq.com', passwd='11z4550690', image='about:blank',id=tstamp)
    await u.save()


loop = asyncio.get_event_loop()
#把协程丢到事件循环中执行
loop.run_until_complete(test())
