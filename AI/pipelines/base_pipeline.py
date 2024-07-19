
from utils.network_utils import load_checkpoint


class BasePipeline:
    def __init__(self, config):
        self.config = config
        self.exp_name = self.config.get("exp_name", None)
        if self.exp_name is None:
            self.exp_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

