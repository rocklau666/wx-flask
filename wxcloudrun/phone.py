'''
 ┌─────────────────────────────────────────────────────────────┐
 │┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐│
 ││Esc│!1 │@2 │#3 │$4 │%5 │^6 │&7 │*8 │(9 │)0 │_- │+= │|\ │`~ ││
 │├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┤│
 ││ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{[ │}] │ BS  ││
 │├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤│
 ││ Ctrl │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  ││
 │├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────┬───┤│
 ││ Shift  │ Z │ X │ C │ V │ B │ N │ M │< ,│> .│? /│Shift │Fn ││
 │└─────┬──┴┬──┴──┬┴───┴───┴───┴───┴───┴──┬┴───┴┬──┴┬─────┴───┘│
 │      │Fn │ Alt │         Space         │ Alt │Win│   HHKB   │
 │      └───┴─────┴───────────────────────┴─────┴───┘          │
 └─────────────────────────────────────────────────────────────┘

Description: 这是xxxxx文件
Author: liu.yan
Date: 2022-02-16 15:16:30
LastEditors: liu.yan
LastEditTime: 2022-02-17 19:32:33
'''

import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import PhoneInfo
import json
# 初始化日志
logger = logging.getLogger('log')
import requests

APPID="wx254cb79ac986f686"
APPSECRET="be69fe7f254b33d1a1336f95fb5dea97"

def token_get():
    response = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+APPID+"&secret="+APPSECRET,verify=False)
    return response
def login_info_get(JSCODE):
    logger.info(JSCODE)
    res=requests.post("https://api.weixin.qq.com/sns/jscode2session?appid="+APPID+"&secret="+APPSECRET+"&js_code="+JSCODE+"&grant_type=authorization_code",verify=False)
    print(res.text)
  
    r=res.text
    logger.info(r)

    return(r)
# def query_counterbyid(id):
#     """
#     根据ID查询Counter实体
#     :param id: Counter的ID
#     :return: Counter实体
#     """
#     try:
#         return Counters.query.filter(Counters.id == id).first()
#     except OperationalError as e:
#         logger.info("query_counterbyid errorMsg= {} ".format(e))
#         return None


# def delete_counterbyid(id):
#     """
#     根据ID删除Counter实体
#     :param id: Counter的ID
#     """
#     try:
#         counter = Counters.query.get(id)
#         if counter is None:
#             return
#         db.session.delete(counter)
#         db.session.commit()
#     except OperationalError as e:
#         logger.info("delete_counterbyid errorMsg= {} ".format(e))


# def insert_counter(counter):
#     """
#     插入一个Counter实体
#     :param counter: Counters实体
#     """
#     try:
#         db.session.add(counter)
#         db.session.commit()
#     except OperationalError as e:
#         logger.info("insert_counter errorMsg= {} ".format(e))


# def update_counterbyid(counter):
#     """
#     根据ID更新counter的值
#     :param counter实体
#     """
#     try:
#         counter = query_counterbyid(counter.id)
#         if counter is None:
#             return
#         db.session.flush()
#         db.session.commit()
#     except OperationalError as e:
#         logger.info("update_counterbyid errorMsg= {} ".format(e))

