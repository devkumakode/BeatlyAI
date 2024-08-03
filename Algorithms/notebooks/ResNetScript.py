
        #if batch % 100 == 0:
         #   loss, current = loss.item(), (batch + 1) * len(X)
          #  print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
        
        loss, current = loss.item(), (batch + 1) * len(X)
        print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def test(dataloader, model, loss_fn):
