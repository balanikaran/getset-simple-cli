import requests
import click
import threading

@click.group()
def cli():
    """
    Command line tool for setting, getting and listening to key value pairs...
    """
    pass

@cli.command()
@click.argument('key')
@click.argument('value')
def set(key, value):
    """
    This subcommand is used to add a new key value pair
    """
    SET_URL = "http://localhost:3000/add/"
    response = requests.post(SET_URL, json={"key": key, "value": value})
    print("\n\n{}\n\n".format(response.text))

@cli.command()
@click.argument('key')
def get(key):
    """
    This command is used to get the value of a key
    """
    GET_URL = "http://localhost:3000/{}".format(key)
    response = requests.request('get', GET_URL)
    print("\n\nResult = {}\n\n".format(response.json()['value']))
    

@cli.command()
@click.argument('key')
def listen(key):
    """
    This command is used to listen changes on value of a key
    """
    GET_URL = "http://localhost:3000/{}".format(key)
    def getValue():
        threading.Timer(2.0, getValue).start()
        response = requests.request('get', GET_URL)
        print("Listening to {}, Current value = {}".format(key, response.json()['value']))
        
    getValue()