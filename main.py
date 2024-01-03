from flask import Flask, request

def getPidWithRE(target:str,pattern:str):
    pass
    # todo:使用正则匹配获取pid，返回一个数组

def findTaskInfo(searchStr):
    pass
    # todo:使用netstat | grep 命令找到与searchStr匹配的结果，返回字符串

def killTask():
    pass
    # todo:用pid结束任务

def startTask():
    pass
    # todo:启动任务



if __name__ == '__main__':
    pass
    # todo:从远程传入参数，控制任务的启停
