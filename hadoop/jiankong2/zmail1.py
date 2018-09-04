import zmail
import namenode
#读取txt文件内容
def main():
  print("we are in %s"%__name__)
f = open('mailContext.txt', 'r')  # 以读方式打开文件
result = list()
for line in f.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
        continue  # 是的话，跳过不处理
        result.append(line)  # 保存
    result.sort() # 排序结果
    f.close()
# 你的邮件内容
nihao=str(line)

mail_content = {
    'subject': '监控邮件!',  # 随便填写
    'content': nihao,  # 随便填写
    'attachments': 'mailContext.txt',  # 最好使用绝对路径，若你电脑没有这个文件会造成错误
}
#print(mail_content)
# 使用你的邮件账户名和密码登录服务器

print("jieshu")
server = zmail.server('1390331234@qq.com','sqhmnpusuyoofjif')
# 发送邮件

server.send_mail(['liuyuzhou@zhongruigroup.com','378512965@qq.com'],mail_content)


if __name__ == '__main__':
  main()