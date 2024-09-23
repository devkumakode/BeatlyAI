            autosize=True,
        )

        fig.write_html(
            osp.join(self.res_dir, osp.basename(self.config["ecg_data"] + ".html")),
        )
