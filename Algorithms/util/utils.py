	y = y[start:end]
	cmap = ['k', 'r', 'g', 'b']
	start = end = 0
	for i in range(len(y) - 1):
		if y[i] != y[i + 1]:
			end = i
			plt.plot(np.arange(start, end + 1), x[start:end + 1], cmap[int(y[i])])
			start = i + 1
	plt.show()


def plot_rewards_with_std(reward, std_reward_plus, std_reward_minus, xlabel, ylabel):
	x = [i for i in range(len(reward))]
	y = reward

	avg_color = 'black'
	std_color = '#DDDDDD'

	plt.plot(x, y, color=avg_color, linewidth=1.5, label='mean')
	plt.fill_between(x, std_reward_plus, std_reward_minus, color=std_color, label='std')
