import requests
import ssh_tunnel as tunnel
import config as cons
import json_lib as json_lib
import logging


def request_wbs(url):
    """
    sending request for the input url and returning the response
    """
    server = tunnel.start_server(cons.remoteUser, cons.remoteHost, cons.remotePort, cons.localHost,
                                 cons.localPort, cons.privateKey, cons.gateway, cons.configFile)
    response = requests.get(url).content
    tunnel.stop_server(server)
    logging.info("Requested response " + response)
    return response


def request_wbs_sorted_json(url):
    """
    sending request for the input url and returning the response in json sorted
    """
    server = tunnel.start_server(cons.remoteUser, cons.remoteHost, cons.remotePort, cons.localHost,
                                 cons.localPort, cons.privateKey, cons.gateway, cons.configFile)
    response = requests.get(url).content
    tunnel.stop_server(server)
    sorted_response = json_lib.to_json_sorted(response)
    logging.info("Requested response " + sorted_response)
    return sorted_response
