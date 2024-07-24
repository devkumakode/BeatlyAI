import json
import os.path as osp
from glob import glob

import pandas as pd

# 1. N - Normal
# 2. V - PVC (Premature ventricular contraction)
# 3. \ - PAB (Paced beat)
# 4. R - RBB (Right bundle branch)
# 5. L - LBB (Left bundle branch)
# 6. A - APB (Atrial premature beat)
# 7. ! - AFW (Ventricular flutter wave)
# 8. E - VEB (Ventricular escape beat)

classes = ["N", "V", "\\", "R", "L", "A", "!", "E"]
lead = "MLII"
extension = "png"  # or `npy` for 1D
data_path = osp.abspath("../data/*/*/*/*/*.{}".format(extension))
