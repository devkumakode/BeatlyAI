            target = target.to(device)

            output = net(ecgs)
            output = output.to(device)
