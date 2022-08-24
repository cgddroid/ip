import db
import flask
from flask import jsonify
from flask import request
app=flask.Flask("__name__")
redis2=db.redis1()
@app.route('/')
def head():
    return '<h2>欢迎来到代理池！<h2>'
#获取一个可用ip
@app.route('/get')
def huoqu():
    data=redis2.huoqu()
    if data:
        return redis2.huoqu()
    else:
        return '<h2>无ip可用!<h2>'
##获取多个ip
@app.route('/duoge')
def duoge():
    data=redis2.quanbuip()
    data.reverse()
    num=request.args.get('num','')
    if num:
        num=int(num)
        return jsonify(data[:num])
    else:
        num=1
        return redis2.huoqu()
#获取总共的IP个数
@app.route('/count')
def count():
    data=redis2.geshu()
    return f'总共有{data}个ip'
if __name__ == '__main__':
    # app.run()
    pass
