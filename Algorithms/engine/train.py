                print("EPOCH:{} Iter:{} of {} Loss:{:.4f} Acc:{:.4f}".format(step, i + 1, len(train_loader), loss.item(), correct / total))

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (step+1) % 2 == 0:
            torch.save(net, config.RESOURCES_DIR + '/ckpt/epoch_{}.ckpt'.format(step))

        train_test(train_loader, 'train', step, net, device, batch_size=batch_size)
        train_test(val_loader, 'val', step, net, device, batch_size=batch_size)
