import pika
import pprint


def _on_message(ch, method, properties, body):
    ret = {}
    ret['routing_key'] = method.routing_key
    ret['headers'] = properties.headers
    ret['body'] = body
    print '---------------'
    print pprint.pprint(ret)
    print '---------------'


paras = pika.ConnectionParameters(credentials=pika.PlainCredentials(
    username='guest',
    password='ntse')
)
conn = pika.BlockingConnection(paras)
chan = conn.channel()
queue = chan.queue_declare('dump', exclusive=False, auto_delete=True).\
            method.queue

chan.queue_bind(exchange='amq.rabbitmq.trace', queue=queue, routing_key='#')
chan.queue_bind(exchange='amq.rabbitmq.log', queue=queue, routing_key='#')
chan.basic_consume(_on_message, queue=queue, no_ack=True)
chan.start_consuming()
