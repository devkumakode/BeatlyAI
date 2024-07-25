
        loss_values_final.append(loss_values)
        accuracy_final.append(accuracy)

        save_as_pkl(config.RESOURCES_DIR + '/loss.pkl', loss_values_final)
        save_as_pkl(config.RESOURCES_DIR + '/accuracy.pkl', accuracy_final)

