
def get_labels(datasets):
    nr_classes = len(datasets)
    labels = []
    for i in range(nr_classes):
         for _ in range(len(datasets[i])):
             class_label = [0] * nr_classes
             class_label[i] = 1
             labels.append(class_label)
