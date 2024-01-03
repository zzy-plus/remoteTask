from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

def getPidWithRE(target:str,pattern:str):
    # r'LISTEN      ([0-9]+)/'
    matches =  re.findall(pattern, target)
    print(matches[0])
    return matches[0]   #这里应当返回对应进程的pid


def findTaskInfo(ip_port:str):
    command = f'netstat -tulnp | grep {ip_port}'
    return subprocess.run(command, shell=True, capture_output=True, text=True)

def killTask(pid):
    command = f'kill {pid}'
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    # todo:根据执行结果返回True 或 False

def startTask(start_command):
    output = subprocess.run(start_command, shell=True, capture_output=True, text=True)
    # todo


def readFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        pass

def writeFile(filePath, data):
    with open(filePath, 'w', encoding='utf-8') as f:
        pass


@app.route('/read', methods=['GET'])
def fun_read():
    pass

@app.route('/write', methods=['GET'])
def fun_write():
    pass

@app.route('/start', methods=['GET'])
def fun_start():
    pass

@app.route('/stop', methods=['GET'])
def dun_stop():
    pass

@app.route('/restart', methods=['GET'])
def fun_restart():
    pass



if __name__ == '__main__':
    app.run('0.0.0.0', 1020, debug=True)
    pass
    # todo:从远程传入参数，控制任务的启停
