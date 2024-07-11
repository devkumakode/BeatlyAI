			res[ix] = np.array(tmp[ix]).reshape((window, 1))
	except ValueError as e:
		print(e)
