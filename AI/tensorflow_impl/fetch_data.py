                 choices=["nsrdb", "apnea-ecg", "mitdb", "afdb", "svdb"],
                 help="The list of datasets to download")

args = par.parse_args()
dataset_list = args.dataset_list


def fetch_data():
    """
    nsrdb normal sinus rhythm
    apnea
    mitdb arrhythmia
    afdb atrial fibrillation
    svdb supraventricular arrhythmia 
    """

    physionet = {
        "nsrdb": ["16265", "16272", "16273", "16420", "16483", "16539", "16773",
