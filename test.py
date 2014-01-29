import pika
import json
import pprint


def parse_message(body):
    """
    RPC message like below:
        oslo.message: string. Example: '{}'
        oslo.version: string. Example: '2.0'
    """
    if not isinstance(body, dict):
        raise ValueError("Message must be a valid dict.")

    try:
        msg_version = body['oslo.version']
        msg_body = json.loads(body['oslo.message'])

        method = msg_body['method']
    except Exception:
        import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    return method


def _on_message(ch, _method, _properties, body):
    print '---------------'
    body_obj = json.loads(body)
    print parse_message(body_obj)
    print '---------------'


paras = pika.ConnectionParameters(
    host='127.0.0.1',
    credentials=pika.PlainCredentials(
        username='guest',
        password='bb488ba44452dee7ce6a')
)
conn = pika.BlockingConnection(paras)
chan = conn.channel()
queue = chan.queue_declare('dump', exclusive=False, auto_delete=True).\
            method.queue

chan.queue_bind(exchange='nova', queue=queue, routing_key='#')
chan.basic_consume(_on_message, queue=queue, no_ack=True)
chan.start_consuming()
