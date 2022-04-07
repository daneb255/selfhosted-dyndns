import logging
import os

from flask import Flask, request
from core.settings import FLASK_SECRET_KEY, LOG_ROOT_DIR
from dyndns import set_dns

logging.basicConfig(
     filename=os.path.join(LOG_ROOT_DIR, 'dyndns.log'),
     format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
     datefmt='%Y-%m-%d,%H:%M:%S',
     level=logging.INFO
)

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY


@app.route("/set-ip", methods=['GET'])
def get_domain():
    try:
        user = request.args.get('USER')
        pw = request.args.get('PW')
        domain = request.args.get('DOMAIN')

        ip = request.args.get('IP')
        if not ip:
            ip = request.headers.getlist("X-Forwarded-For")[0]
            logging.info('No IP given, get IP from request: {}'.format(ip))

        ip6 = request.args.get('IP6')
        if not ip6:
            ip6 = ''

        logging.info('Get values {} {} {}'.format(ip, ip6, domain))
        if user and pw and domain and ip:
            logging.info('set dns with {} {} {}'.format(ip, ip6, domain))
            if set_dns(user, pw, domain, ip, ip6):
                return {'message': 'success'}, 200
            else:
                return {'message': 'error'}, 400
        else:
            return {'message': 'error'}, 400
    except Exception as e:
        print(e)
        return {'message': 'error'}, 400


@app.route("/")
def default():
    return {'message': 'hello!'}, 200
