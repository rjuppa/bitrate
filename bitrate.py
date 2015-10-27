import click
import requests.packages
import json
from decimal import Decimal

requests.packages.urllib3.disable_warnings()


def get_price():
    jdata = requests.get('https://www.bitstamp.net/api/ticker/', timeout=30)
    str = json.loads(jdata.text)['last']
    price = Decimal(str)
    return price


@click.command()
def cli():
    color = 'white'
    click.echo("According to BitStamp.net the price for 1BTC is:")
    click.echo(click.style('%s USD' % get_price(), fg=color))


