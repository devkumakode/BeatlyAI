                    "state_dict": self.model.state_dict(),
                    "optimizer": self.optimizer.state_dict(),
                    "epoch": epoch,
                    "total_iter": self.total_iter,
                },
                osp.join(self.pth_dir, "{:0>8}.pth".format(epoch)),
            )
