from sshtunnel import SSHTunnelForwarder
import logging


def start_server(remote_user, remote_host, remote_port, local_host, local_port, private_key, gateway, config_file):
    """
    Starting server for the tunnel from local to the given environment
    """
    server = SSHTunnelForwarder(
        ssh_address_or_host=gateway,
        ssh_config_file=config_file,
        ssh_username=remote_user,
        ssh_private_key=private_key,
        remote_bind_address=(remote_host, int(remote_port)),
        local_bind_address=(local_host, int(local_port)),
    )

    server.start()
    logging.info("tunnel open now")
    return server


def stop_server(server):
    """
    Shutting tunnel down
    :param server:
    :return:
    """
    server.stop()
    logging.info("tunnel closed")
