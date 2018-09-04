#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender = '1390331234@qq.com'  # 发件人邮箱账号
my_pass = 'sqhmnpusuyoofjif'  # 发件人邮箱密码
my_user = 'liuyuzhou@zhongruigroup.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    f = open('mailContext.txt', 'r')  # 以读方式打开文件
    result = list()
    for line in f.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
            continue  # 是的话，跳过不处理
        result.append(line)  # 保存
    result.sort() # 排序结果

    f.close()

    try:
        msg = MIMEText(line, 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
    exit()
else:
    print("邮件发送失败")
    exit()