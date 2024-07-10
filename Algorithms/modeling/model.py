
		features = self.features(x)
		features_res = features.reshape((batch, 398, 1))

		memory, _ = self.memory(features_res)
		deconv = self.deconv(memory.reshape((batch, 64, 398)))
		deconv = deconv.reshape((batch, seq_len, 32))
		output = self.classifier(deconv)
		out = self.output(output.view(batch * seq_len, -1))

		return out
