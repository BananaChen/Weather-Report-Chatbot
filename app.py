from bottle import route, run, request, abort, static_file
from fsm import TocMachine
import os

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']
#VERIFY_TOKEN = "1234567890987654321"
machine = TocMachine(
    states=[
        'user',
        'hello',
        'region',
        'city',
        'temperature',
        'rainProb',
        'byebye'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'hello',
            'conditions': 'is_going_to_hello'
        },
        {
            'trigger': 'advance',
            'source': 'hello',
            'dest': 'region',
            'conditions': 'is_going_to_region'
        },
        {
            'trigger': 'advance',
            'source': 'region',
            'dest': 'city',
            'conditions': 'is_going_to_city'
        },
        {
            'trigger': 'advance',
            'source': 'city',
            'dest': 'temperature',
            'conditions': 'is_going_to_temperature'
        },
        {
            'trigger': 'advance',
            'source': 'city',
            'dest': 'rainProb',
            'conditions': 'is_going_to_rainProb'
        },
        #from temp
        {
            'trigger': 'advance',
            'source': 'temperature',
            'dest': 'rainProb',
            'conditions': 'is_going_to_rainProb'
        },
        {
            'trigger': 'advance',
            'source': 'temperature',
            'dest': 'hello',
            'conditions': 'is_going_to_hello'
        },
        {
            'trigger': 'advance',
            'source': 'temperature',
            'dest': 'byebye',
            'conditions': 'is_going_to_byebye'
        },
        #from rain prob
        {
            'trigger': 'advance',
            'source': 'rainProb',
            'dest': 'temperature',
            'conditions': 'is_going_to_temperature'
        },
        {
            'trigger': 'advance',
            'source': 'rainProb',
            'dest': 'hello',
            'conditions': 'is_going_to_hello'
        },
        {
            'trigger': 'advance',
            'source': 'rainProb',
            'dest': 'byebye',
            'conditions': 'is_going_to_byebye'
        },
        #go back
        {
            'trigger': 'go_back',
            'source': [
                'byebye',
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    #machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    #run(host="localhost", port=5000, debug=True, reloader=True)
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
