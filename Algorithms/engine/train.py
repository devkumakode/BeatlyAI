            loss = criterion(output, target)

            _, predicted = torch.max(output.data, 1)

            predicted = predicted.to(device)

            total += target.size(0)
            correct += (predicted == target).sum().item()

            loss_item = loss.item()

            running_loss += loss_item
            loss_values.append(running_loss)

            accuracy.append(correct / total)

            if (i+1) % 20 == 0:
