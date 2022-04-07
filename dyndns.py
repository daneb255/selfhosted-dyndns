import json
import requests
import logging
from core.settings import DYNDNS_FILE, DYNDNS_PASSWORD, DYNDNS_USER, RECORDS, PDNS_API_URL, PDNS_API_KEY


def set_dns(user, pw, domain, ip, ip6):
    if user == DYNDNS_USER and pw == DYNDNS_PASSWORD:
        dyndns_text = open(DYNDNS_FILE, "w+")
        dyndns_text.write('{}\n'.format(ip))
        dyndns_text.write('{}\n'.format(ip6))
        dyndns_text.write('{}\n'.format(domain))
        dyndns_text.close()
        try:
            uri = '{}/{}'.format(PDNS_API_URL, domain)
            headers = {'X-API-Key': '{}'.format(PDNS_API_KEY)}
            success = True
            for record in RECORDS:
                logging.info('Set record: {} ip: {} ip6: {} for domain: {}'.format(record, ip, ip6, domain))
                payload = {
                    "rrsets": [
                        {
                            "name": "{}".format(record),
                            "type": "A",
                            "ttl": 60,
                            "changetype": "REPLACE",
                            "records": [
                                {
                                    "content": "{}".format(ip),
                                    "disabled": False
                                }
                            ]
                        },
                        {
                            "name": "{}".format(record),
                            "type": "AAAA",
                            "ttl": 60,
                            "changetype": "REPLACE",
                            "records": [
                                {
                                    "content": "{}".format(ip6),
                                    "disabled": False
                                }
                            ]
                        }
                    ]
                }
                r = requests.patch(uri, data=json.dumps(payload), headers=headers)
                logging.info('Request status code: {}'.format(r.status_code))
                if r.status_code == 200 or r.status_code == 204:
                    logging.info('Entry created successfully!')
                    r.close()
                else:
                    logging.info('Entry not created!')
                    r.close()
                    success = False

            if success:
                return True
            else:
                return False
        except Exception as e:
            logging.error(e)
            return False
