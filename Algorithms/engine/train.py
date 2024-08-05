                batch_size = ecgs.shape[0]

            output = net(ecgs)
            output = output.to(device)

            _, predicted = torch.max(output.data, 1)
            label_true = labels.contiguous().view(-1).long()

            total += label_true.size(0)
            right += (predicted == label_true).sum().item()

        print("epoch:{},{} ACC: {:.4f}".format(step, str1, right / total))


def get_charateristic(y):
    Ppos = Qpos = Rpos =Spos = Tpos = 0
    for i, val in enumerate(y):
        if val == 1 and y[i-1] == 0:
