"""
# ECG wave segmentation

The goal is to segment different types of waves from the ECG signal. There are 4 types of waves: P-wave,
QRS-complex, T-wave, extrasystole (parts of the signal are not part of any wave). You should focus on detecting
boundaries where each wave starts and ends. You are provided with an annotated dataset of ECG signals
from 3 databases (cardiplus, incartdb, mitdb) in the data directory. There is also split.csv file containing
the paths to all the files. Each file contains one ECG signal,
also called a lead, in a JSON format. The structure of the JSON format is as follows:
```
{'data': {
        '<lead_name>': {
            'ecg': [[]],
            'label': [[]],
            'fs': int} },
 'legend': {0: 'none', 1: "p_wave", 2: "qrs", 3: "t_wave", 4: "extrasystole"}
```
The format is designed for multiple leads and multiple signals per lead, however, in this case, each file contains
exactly one lead with one signal. For each lead there is `ecg` with the ecg signal, `labels` with list
of integers [0-4] of the same length as the ecg signal (category of each point of the signal),
