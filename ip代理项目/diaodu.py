import getip
import db
import jianche
import concurrent.futures
import multiprocessing
redis2=db.redis1()
import time
import api
class diaodu:
    #使代理ip每隔五分钟爬取一次
    def paqui(self):
        while True:
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exu:
                duixiang1 = exu.submit(getip.yundaill)
                duixiang2 = exu.submit(getip.zimadaill)
                duixiang3 = exu.submit(getip.qitaip)
                duixiang4 = exu.submit(getip.bajiuip)
                duixiang5 = exu.submit(getip.kuaiip)
            data_0 = list(duixiang1.result())
            data_1 = list(duixiang2.result())
            data_2 = list(duixiang3.result())
            data_3 = list(duixiang4.result())
            data_4 = list(duixiang5.result())
            data = data_0 + data_1 + data_2 + data_3 + data_4
            for i in data:
                redis2.add(i)
            time.sleep(60*5)
    #每隔5分钟对ip检验一次
    def jianyan(self):
        while True:
            jianche.threa()
            time.sleep(60*5)
    #调度api服务模块
    def api(self):
        api.app.run()
    #用多进程同时执行可用达到同步
    def main(self):
        paqu_process=multiprocessing.Process(target=self.paqui)
        paqu_process.start()
        if redis2.geshu()>0:
            jiance_process=multiprocessing.Process(target=self.jianyan)
            jiance_process.start()
        api_process=multiprocessing.Process(target=self.api)
        api_process.start()
if __name__ == '__main__':
    diaodu_0=diaodu()
    diaodu_0.main()
