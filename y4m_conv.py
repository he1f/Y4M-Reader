class Y4MReader():
	def __init__(self):
		self.init_ok = False
		self.in_file = file
		self.width, self.height = 0, 0
		self.framerate = 0
		self.aspect_ratio = 0
		self.color_space = ''
		self.scan_type = ''
		self.comment = ''

	def _get_value(self):
		val = ''
		tmp = self.in_file.read(1)
		while tmp != ' ':
			val += str(tmp)
			tmp = self.in_file.read(1)
		print 'val =', val

	def init(self, filename):
		try:
			self.in_file = open(filename)
		except IOError, e:
			init_ok = False
			print 'Cannot open file `' + filename + '\': ' + str(e)
			return 1

		# check format
		data = self.in_file.read(10)	#	YUV4MPEG2 + " "
		if data != 'YUV4MPEG2 ':
			init_ok = False
			return 2

		# reading W, H is that order...
		# W first...
		data = self.in_file.read(1)
		if data == 'W':
			self.width = self._get_value()
		else:
			init_ok = False
			return 2

		# ... than H
		data = self.in_file.read(1)
		if data == 'H':
			self.height = self._get_value()
		else:
			init_ok = False
			return 2

		print 'width  =', self.width
		print 'height =', self.height
		init_ok = True

		return 0

	def get_next_frame(self):
		return 0

	def get_width(self):
		if init_ok == False:
			return 0
		return self.width

	def get_height(self):
		if init_ok == False:
			return 0
		return self.height

	def get_framerate(self):
		if init_ok == False:
			return 0
		return self.framerate

	def get_aspect_ratio(self):
		if init_ok == False:
			return 0
		return self.aspect_ratio

	def get_scan_type(self):
		if init_ok == False:
			return 0
		return self.scan_type

	def get_colour_space(self):
		if init_ok == False:
			return 0
		return self.color_space

	def get_comment(self):
		if init_ok == False:
			return 0
		return self.comment

	def get_frame(self, index):
		return 0

if __name__ == '__main__':
	reader = Y4MReader()
	err = reader.init('akiyo_qcif.y4m')