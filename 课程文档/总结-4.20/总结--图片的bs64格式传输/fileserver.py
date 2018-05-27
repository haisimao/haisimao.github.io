from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps


def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('10.7.152.69', 5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('memory.png', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 用一个字典(键值对)来保存要发送的各种数据
        # 待会可以将字典处理成JSON格式在网络上传递
        my_dict = dict({})
        my_dict['filename'] = 'memory.png'
        # JSON是纯文本不能携带二进制数据
        # 所以图片的二进制数据要处理成utf-8编码
        my_dict['filedata'] = data
        # 通过dumps函数将字典处理成JSON字符串
        json_str = dumps(my_dict)
        # 发送JSON字符串
        client.send(json_str.encode('utf-8'))
        client.close()


if __name__ == '__main__':
    main()
