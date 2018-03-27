#!/usr/bin/python3
import redis
import os
import time
import socket
from datetime import datetime




# Create a UDP socket
class RedisClient():
	PREFIX = 'mosix_server_'

	def __init__(self, host = 'localhost', port = 6379, keepalive = 3):
		self.r = redis.StrictRedis(host=host, port=port)
		self.keepalive = keepalive

	def send_keep_alive(self, line_in_mosix_conf):
		sent = False
		while not sent:
			print('sending KA:', line_in_mosix_conf, self.keepalive , datetime.now())
			sent = self.r.setex(line_in_mosix_conf, self.keepalive , datetime.now())

	def get_hosts_map(self):
		hosts = self.r.keys(self.PREFIX+'*')
		hosts_map = [x.decode('utf-8')[len(self.PREFIX):] for x in hosts if x.decode('utf-8').startswith(self.PREFIX)]
		return hosts_map

def main():
	# Unit-test
	a = RedisClient()
	a.send_keep_alive("hello world")
	a.get_hosts_map()
	time.sleep(5)
	a.get_hosts()


if __name__ == "__main__":
    main()