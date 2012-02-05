from y4mreader import Y4MReader

if __name__ == '__main__':
	reader = Y4MReader()
	err = reader.init('akiyo_qcif.y4m')
	of = file('akiyo_qcif.yuv', 'wb')
	if not err:
		err, nframes = 0, 0
		while not err:
			(err, frame) = reader.get_next_frame()
			print 'Err:', err, '-- frame_size:', len(frame)
			if not err:
				of.write(frame)
				nframes += 1

		print 'nframes:', nframes