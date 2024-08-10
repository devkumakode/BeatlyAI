	###############################################################################

	split_df = prepare_split_df(config.ECG_DATA_DIR + '/split.csv')

	print(split_df.head(5))

	if INSPECT:
		distinct_databases = set(split_df['Database'].values.tolist())
		for distinct_database in distinct_databases:
			print(str(distinct_database).upper())

			current_db_df = split_df[split_df['Database'] == distinct_database]
			inspect_db(current_db_df)
			print()
			print()

	x_train, y_train = fun(
			split_df,
			split_df.apply(
