import pika, json

params = pika.URLParameters('amqps://keakrtib:XkIR-8xquzQieSr4oVVJx65eQOb4sHC_@beaver.rmq.cloudamqp.com/keakrtib')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)