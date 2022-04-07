# selfhosted-dyndns

A selfhosted minimal python Flask backend for handling multiple domains to update the A-Record over the [powerdns](https://www.powerdns.com/) API. The API could be triggered from fritzbox to use pivpn/nextcloud or other tools.

## Install & Run

- Install Python 3.9 and pipenv
- Install Powerdns
- Create API Code in Powerdns
- Clone dir
- cd to dir
- `pipenv install`
- `cp core/.env-example core/.env`
- Edit .env file
- Define multiple subdomains in core/settings.py (RECORDS)
- Run `start_server.sh` script or add dyndns service to systemd
- `cp dyndns.service /etc/systemd/system/dyndns.service`
- `systemctl enable dyndns.service`
- `systemctl start dyndns.service`

## Fritzbox

Go to DynDNS settings, set to custom

url -> nameserverdomain.de/set-ip?USER=<username>&PW=<pass>&DOMAIN=<domain>&IP=<ipaddr>&IP6=<ip6addr>

domain name -> any value (not used in this version)

username -> set username as in .env

password -> set password as in .env

## Docker image
tbd

