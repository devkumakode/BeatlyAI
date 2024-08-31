
                predictions = self.model(inputs)

                classes = predictions.topk(k=1)[1].view(-1).cpu().numpy()

                gt_class = np.concatenate((gt_class, batch["class"].numpy()))
                pd_class = np.concatenate((pd_class, classes))

        class_accuracy = sum(pd_class == gt_class) / pd_class.shape[0]
        print("Validation CLASS accuracy - {:4f}".format(class_accuracy))

        pd_class = pd_class.astype(int)
