import pika
import json

#---------------------- 生产者者 --------------------------------------------------------
credentials = pika.PlainCredentials('shampoo', '123456')  # mq用户名和密码
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(pika.ConnectionParameters(host = '10.1.62.170',port = 5672,virtual_host = '/',credentials = credentials))
channel = connection.channel()
# 声明消息队列，消息将在这个队列传递，如不存在，则创建
result = channel.queue_declare(queue = 'python-test')

for i in range(10):
    message=json.dumps({'OrderId':"1000%s"%i})
    # 向队列插入数值 routing_key是队列名
    channel.basic_publish(exchange = '',routing_key = 'python-test',body = message)
    print(message)
connection.close()


#---------------------- 消费者 --------------------------------------------------------
credentials = pika.PlainCredentials('shampoo', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host = '10.1.62.170',port = 5672,virtual_host = '/',credentials = credentials))
channel = connection.channel()
# 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
channel.queue_declare(queue = 'python-test', durable = False)
# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(body.decode())

# 告诉rabbitmq，用callback来接收消息
channel.basic_consume('python-test',callback)
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()