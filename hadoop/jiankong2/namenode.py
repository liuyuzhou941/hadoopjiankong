import urllib.request
import socket
import json




sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.settimeout(1)
try:
    sk.connect(('192.168.200.73',50070))
    print('Server port 50070 OK!')
    with urllib.request.urlopen(
            'http://192.168.200.73:50070/jmx?qry=Hadoop:service=NameNode,name=JvmMetrics') as response:
        html = response.read()
       # print(type(html))
        #json1 = str(html, encoding="utf-8")
        # print(type(a))
        # print (a[0:3])
        #转换成字符串
        json1=str(html, encoding="utf-8")
        #print(type(json1))
        str = json1

        params = json.loads(str)
        #逐步的去掉外围括号等！最后变成字典
        #print (type(params))
        #print(params)
        #print (params["beans"])
        list1= params["beans"]
        #print(type(list1[0]))
        #print(list1[0])
        dict1=list1[0]
        #监控选项
        #监控名称
        '''
        print(dict1["name"])
        #模型类型
        print(dict1["modelerType"])
        #附加标签
        print(dict1["tag.Context"])
      
        print(dict1["tag.ProcessName"])
        print(dict1["tag.SessionId"])
        print(dict1["tag.Hostname"])
        '''
        """
        #jvm非堆内存已使用大小
        print(dict1["MemNonHeapUsedM"])
        #jvm非堆内存已提交大小
        print(dict1["MemNonHeapCommittedM"])
        ###########
        print(dict1["MemNonHeapMaxM"])
        #jvm使用堆内存大小
        print(dict1["MemHeapUsedM"])
        #jvm提交堆内存大小
        print(dict1["MemHeapCommittedM"])
        ###########
        print(dict1["MemHeapMaxM"])
        ###########
        print(dict1["MemMaxM"])
        ###########
        print(dict1["GcCountCopy"])
        ###########
        print(dict1["GcTimeMillisCopy"])
        ###########
        print(dict1["GcCountMarkSweepCompact"])
        ###########
        print(dict1["GcTimeMillisMarkSweepCompact"])
        #gc总次数
        print(dict1["GcCount"])
        # gc总耗时(ms)
        print(dict1["GcTimeMillis"])
        ###########
        print(dict1["GcNumWarnThresholdExceeded"])
        ###########
        print(dict1["GcNumInfoThresholdExceeded"])
        ###########
        print(dict1["GcTotalExtraSleepTime"])
        #尚未启动的线程数目
        print(dict1["ThreadsNew"])
        # 正在执行状态的线程数目
        print(dict1["ThreadsRunnable"])
        # 正在阻塞等待监视器锁的线程数目
        print(dict1["ThreadsBlocked"])
        # 无限期地等待另一个线程来执行某一特定操作的线程数目
        print(dict1["ThreadsWaiting"])
        # 等待另一个线程执行取决于指定等待时间的操作的线程数目
        print(dict1["ThreadsTimedWaiting"])
        # 已退出线程数目
        print(dict1["ThreadsTerminated"])
        # jvm出现fatal次数
        print(dict1["LogFatal"])
        """
        # jvm Error次数
        """
        print(dict1["LogError"])
        # jvm出现warn的次数
        print(dict1["LogWarn"])
        # jvm 出现Info的次数
        print(dict1["LogInfo"])
        """
        # jvm出现warn的次数
        #print(type(dict1["LogWarn"]))
        jvmB=dict1["LogWarn"]
        if jvmB>0:
            with open('mailContext.txt', 'w') as fw:  # with方式不需要再进行close
                fw.write('jvm出现warn的次数>1')
                fw.close()
                import mailJJ


        else:
            print (jvm_warn监控正常)
            exit()







        #print(json1["name"])
        # MemNonHeapUsedM1="MemNonHeapUsedM"
        # MemNonHeapUsedM2=json1.index(MemNonHeapUsedM1)
        # print( json1.find(MemNonHeapUsedM1))
        # print(json1[120:150])

        response.close()
        # print(bytes.decode(html))  # 默认 encoding="utf-8"
        # print(html.decode())  # 默认 encoding="utf-8"
        # print (html)
        # print(type(html))
        # a=list(html)
    # print(type(a))
    # print(a[0:1110])
except Exception:
    print("'Server port 50700 not connect!")
sk.close()
#with urllib.request.urlopen('http://192.168.200.73:50070/jmx') as response:



