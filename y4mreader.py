""" y4mreader - class to read YUV4MPEG2 file format

Author:
 Andrey Maslennikov <andrew.maslennikov@gmail.com>
"""
class Y4MReader():
	def __init__(self):
		self.init_ok = False
		self.in_file = file
		self.width, self.height = 0, 0
		self.framerate    = 0.0
		self.aspect_ratio = 0.0
		self.color_space  = ''
		self.scan_type    = ''
		self.comment      = ''

	def _get_value(self):
		val = ''
		tmp = str(self.in_file.read(1))
		while tmp != ' ' and tmp != "\n":
			val += str(tmp)
			tmp = self.in_file.read(1)
		return str(val)

	def _set_default_values(self):
		if not self.color_space:
			self.color_space = '420'

	def _next(self, num):
		val = self.in_file.read(num)
		self.in_file.seek(-1 * num, 1)	# to NUM symbols back from current position
		return str(val)

	def init(self, filename):
		try:
			self.in_file = open(filename, 'rb')
		except IOError, e:
			init_ok = False
			print 'Cannot open file `' + filename + '\': ' + str(e)
			return 1

		# check format
		data = self.in_file.read(10)	# YUV4MPEG2 + " "
		if data != 'YUV4MPEG2 ':
			init_ok = False
			return 2

		self.init_ok = True

		while self._next(5) != 'FRAME':
			data = self.in_file.read(1)
			if data == 'W':
				self.width = int(self._get_value())
			elif data == 'H':
				self.height = int(self._get_value())
			elif data == 'F':	# framerate
				data = self._get_value()
				numerator, denominator = data.split(':')
				self.framerate = float(numerator) / float(denominator)
			elif data == 'I':	# scan type
				data = self._get_value()
				if data == 'p':
					self.scan_type = 'progressive'
				elif data == 't':
					self.scan_type = 'tff'
				elif data == 'b':
					self.scan_type = 'bff'
				else:
					self.scan_type = 'mixed'
			elif data == 'A':	# aspect ratio
				self.aspect_ratio = self._get_value()
			elif data == 'C':	# color space
				self.color_space = self._get_value()
				# only 4:2:0 for now
				if self.color_space != '420':
					self.init_ok = False
					return 2
			else:
				print 'Unknown parameter: `' + data + '\''
				break

		self._set_default_values()

		print 'width        =', self.width
		print 'height       =', self.height
		print 'framerate    =', self.framerate
		print 'scan_type    =', self.scan_type
		print 'aspect_ratio =', self.aspect_ratio
		print 'color_space  =', self.color_space

		return 0

	def get_next_frame(self):
		if not self.init_ok:
			return (3, '')

		data = self.in_file.read(6)
		if data != "FRAME\n":
			return (2, '')

		if (self.color_space == '420'):
			size = self.width * self.height * 3 / 2
		frame_data = self.in_file.read(size)

		return (0, frame_data)

	def get_width(self):
		if not self.init_ok:
			return 3
		return self.width

	def get_height(self):
		if not self.init_ok:
			return 3
		return self.height

	def get_framerate(self):
		if not self.init_ok:
			return 3
		return self.framerate

	def get_aspect_ratio(self):
		if not self.init_ok:
			return 3
		return self.aspect_ratio

	def get_scan_type(self):
		if not self.init_ok:
			return 3
		return self.scan_type

	def get_colour_space(self):
		if not self.init_ok:
			return 3
		return self.color_space

	def get_comment(self):
		if not self.init_ok:
			return 3
		return self.comment
