
#!/usr/bin/python3
from redis_conn import RedisClient
from mosix_conf import MosixConf
import time
import socket

def _get_external_IP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	print("ip is", ip)
	s.close()
	return ip

def main():
	hostname = RedisClient.PREFIX + _get_external_IP()
	line = '{} 1 p'.format(hostname)
	keepalive = 30
	r = RedisClient(host = 'redis.zae11b.ng.0001.use2.cache.amazonaws.com', keepalive=keepalive)
	mc = MosixConf(conf_path = '/etc/mosix')
	while True:
		r.send_keep_alive(line)
		hosts = (r.get_hosts_map())
		print('got those hosts:', hosts)
		hosts = set(hosts)
		current_hosts = set(mc.get_map())
		if (hosts != current_hosts):
			print("setting new map")
			mc.set_map(hosts)
		time.sleep(keepalive/3)



if __name__ == "__main__":
    main()
