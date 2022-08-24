import redis
import random
class redis1:
    def __init__(self,host='127.0.0.1',port='6379',db=0):
        #连接数据库
        self.db=redis.Redis(host=host, port=port, db=db, decode_responses=True)
    #判断代理是否在在数据库中
    def panduan(self,porxy):
        #判断数据库中是否有这个代理，如果是空的则返回None
        return self.db.zscore('ip',porxy) is None
    #往数据库里面添加一个元素
    def add(self,porxy,score=10):
        if self.panduan(porxy):
            print("添加", porxy)
            self.db.zadd('ip',mapping={porxy:score})
    #获取ip代理
    def huoqu(self):
        data=self.db.zrangebyscore('ip',100,100)
        if len(data):
            return random.choice(data)
        #如果没有一百分的则选择100以下的随便选一个的
        if len(self.db.zrangebyscore('ip',80,100)):
            return random.choice(self.db.zrangebyscore('ip',80,100))
        print("无ip可用")
    #对代理ip进行检验不合法进行减分
    def jianyan(self,porxy):
        self.db.zincrby('ip',-2,porxy)
        score=self.db.zscore('ip',porxy)
        #当检验分数小于或等于0时删除此代理ip
        if score<=0:
            self.db.zrem('ip',porxy)
    #对检验合格的代理ip直接给100分
    def max(self,porxy):
        self.db.zadd('ip',mapping={porxy:100})
    #获取代理ip为100分的全部ip
    def quanbumax(self):
        data=self.db.zrangebyscore('ip',100,100)
        if data:
            return data
        else:
            print("无100分代理ip可用")
    #获取全部代理ip个数
    def geshu(self):
        data=self.db.zcard('ip')
        return data
    #获取全部代理ip
    def quanbuip(self):
        data=self.db.zrangebyscore('ip',2,100)
        if data:
            return data
        else:
            print('数据为空!')
if __name__ == '__main__':
    redis2=redis1()
    # print(redis2.db)
    # a=['183.147.30.68:9000', '183.147.29.33:9000', '183.147.29.33:9000', '115.223.223.30:9000', '60.170.152.46:38888', '222.136.89.3:80', '218.75.38.154:9091']
    # for i in a:
    #     redis2.add(i)
    print(redis2.huoqu())
    # print(redis2.quanbuip())
    pass
