SAVE_TO_FILE = False


def extract_name (text, start_marker, end_marker):
	start = text.index(start_marker) + len(start_marker)
	end = text.index(end_marker, start)

	return text[start:end]


def load_json (filename):
	with open(filename) as f:
		data = json.load(f)
		f.close()
