from y4mreader import Y4MReader

if __name__ == '__main__':
	reader = Y4MReader()
	err = reader.init('akiyo_qcif.y4m')
	if not err:
		err, nframes = 0, 0
		while not err:
			(err, frame) = reader.get_next_frame()
			nframes += 1

		print 'nframes:', nframes