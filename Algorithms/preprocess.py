	split_df = pd.read_csv(split_scv_path)
	split_df[['Database', 'filename']] = split_df.name.str.split('/', expand=True)
	split_df['filename'] = split_df.apply(lambda x: extract_name(x['filename'], '', '.json'), axis=1)

	return split_df


if __name__ == "__main__":

	###############################################################################
	# temporary
