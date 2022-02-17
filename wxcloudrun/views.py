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
Date: 2022-02-15 16:54:10
LastEditors: liu.yan
LastEditTime: 2022-02-17 19:24:34
'''

from datetime import datetime
import json
import traceback
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.phone import token_get,login_info_get
from wxcloudrun.model import Counters,PhoneInfo
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
def get_params():
    if request.method == 'GET':
        try:
            params = request.args.to_dict()
        except Exception as err:
            app.logger.error(err)
            app.logger.error(traceback.format_exc())
            params = {}
    else:
        try:
            params = request.get_json() or {}
        except Exception as err:
            app.logger.error(err)
            app.logger.error(traceback.format_exc())
            params = {}
    return params

@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)

@app.route('/api/phone', methods=['GET'])
def get_num():
    """
    :return: 手机号码
    """
        # 获取请求体参数
    params = get_params()
   
    if 'name' not in params:
        return make_err_response('缺少name参数')
    # 按照不同的action的值，进行不同的操作
    name = params['name']
    counter = PhoneInfo.query.filter(PhoneInfo.phone_name == name).first()
    print(counter)
    return make_succ_response("") if counter is None else make_succ_response(counter.phone_num)
@app.route('/api/token', methods=['GET'])
def get_token():
    """
    :return: 手机号码
    """
        # 获取请求体参数

    # 按照不同的action的值，进行不同的操作
    token = json.loads(token_get().text)
    print(token)
    return make_succ_response("") if token is None else make_succ_response(token)
@app.route('/api/login', methods=['GET'])
def wx_login():
    """
    :return: 手机号码
    """
        # 获取请求体参数
    params = get_params()
   
    if 'js_code' not in params:
        return make_err_response('缺少js_code参数')
    # 按照不同的action的值，进行不同的操作
    res = json.loads(login_info_get(params["js_code"]))
    print(res)
    
    return make_succ_response("") if res is None else make_succ_response(res)