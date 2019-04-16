import requests
import click
import threading
import socketio

sio = socketio.Client()

PORT = "3000"
ADDRESS = "http://localhost:{}".format(PORT)

@sio.on('test_successful')
def onTestSuccessful():
    print("Sockets are connected...")

@sio.on('set_done')
def onSetDone(message):
    print("{}".format(message))
    sio.disconnect()


@sio.on('get_done')
def onGetDone(result):
    print("\n\nResult = {}\n\n".format(result))
    sio.disconnect()


@sio.on('get_listening_value')
def onValueUpdated(data):
    print("Listening to {}, Current value = {}".format(
        data['key'], data['value']))


@sio.on('listen_again')
def onListenAgain(data):
    sio.emit('listen', {"key": data})


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
    sio.connect(ADDRESS)
    sio.emit('set', {"key": key, "value": value})


@cli.command()
@click.argument('key')
def get(key):
    """
    This command is used to get the value of a key
    """
    sio.connect(ADDRESS)
    sio.emit('get', {"key": key})
    sio.wait()


@cli.command()
@click.argument('key')
def listen(key):
    """
    This command is used to listen changes on value of a key
    """
    sio.connect(ADDRESS)
    sio.emit('listen', {"key": key})
    sio.wait()


@cli.command()
def testSocket():
    """
    This command is used to test the socket connection
    """
    sio.connect(ADDRESS)
    sio.emit("testing_socket_connection", "We are connected")
    sio.disconnect()
