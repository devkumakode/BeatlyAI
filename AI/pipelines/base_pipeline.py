                            "borderwidth": 1,
                            "borderpad": 4,
                            "bgcolor": "#ffffff",
                            "opacity": 1,
                        },
                    )

        fig = go.Figure(
            data=go.Scatter(
                x=list(range(len(self.pipeline_loader.dataset.signal))),
                y=self.pipeline_loader.dataset.signal,
            ),
        )
        fig.update_layout(
            title="ECG",
            xaxis_title="Time",
            yaxis_title="ECG Output Value",
            title_x=0.5,
            annotations=annotations,
