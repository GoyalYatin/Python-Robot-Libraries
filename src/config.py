"""
Constant global variables_and_configs/configs
"""

# For Tunneling

remoteUser = "ygoyal"         # user name
remoteHost = "10.0.12.83"     # ip for the server where webservice is hosted
remotePort = "8080"
localHost = "127.0.0.1"
localPort = "8080"
privateKey = "D:\\cygwin64\\home\\ygoyal\\.ssh\\id_rsa"     # absolute location of private key
gateway = "ntigwq"            # gateway address for the environment
configFile = "D:\\cygwin64\\home\\ygoyal\\.ssh\\config"     # absolute location of config file


# For Cassandra

host = '127.0.0.1'
port = 9160
keyspace = 'nexti_ay'
user = 'nexti_app'
password = 'spark'
cql_version = '3.4.0'


# For MongoDB

ip_port_initial_db = '127.0.0.1:27017/sampledb'
mongoUserName = ""
mongoPasswd = ""


# For Kafka

bootstrap_servers = 'localhost:9092'
auto_offset_reset = 'latest'
consumer_timeout_ms = 1000
zookeeper_host = '10.0.12.12'
zookeeper_port = 2181
kafka_broker_host = '10.0.12.14'
kafka_broker_port = 9092
kafka_offset = 'largest'
