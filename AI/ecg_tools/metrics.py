        cm = confusion_matrix(self.labels, self.predictions)
        return cm

    def confusion_matrix_image(self):
        figure = ConfusionMatrixDisplay(self.confusion_matrix()).plot().figure_

        def get_img_from_fig(fig, dpi=180):
            buf = io.BytesIO()
            fig.savefig(buf, format="png", dpi=dpi)
            buf.seek(0)
            img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
            buf.close()
            img = cv2.imdecode(img_arr, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            return img

        numpy_figure = get_img_from_fig(figure)
