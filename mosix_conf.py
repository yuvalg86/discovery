#!/usr/bin/python3
import os

class MosixConf():
	def __init__(self, conf_path = os.path.realpath('./test/mosix')):
		self._path_config = conf_path
		self._map_path = os.path.join(conf_path,'mosix.map')
		self.content = None

	def get_map(self):
		if self.content is not None:
			return self.content
		with open(self._map_path,"r") as f:
			self.content = [x.strip() for x in f.readlines() if x.strip() is not None]
		return self.content

	def add_host_to_map(self, host):
		new_line = '{} 1 p'.format(host)
		with open(self._map_path, "a") as f:
			f.write(new_line)
		print('added line ', new_line)

	def set_map(self, newmap):
		with open(self._map_path, "w") as f:
			for item in newmap:
				print(item)
				f.write(item+'\n')
		self.content = newmap


def main():
	# Unit-test
	a = MosixConf('./etc/mosix')
	a.get_map()
	a.add_host_to_map('blagla')

if __name__ == "__main__":
    main()