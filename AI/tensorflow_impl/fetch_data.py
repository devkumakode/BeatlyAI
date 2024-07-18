#!/usr/bin/env python

import os, sys, errno
import csv
import random
import subprocess
import argparse

par = argparse.ArgumentParser(description="Download and process Physionet Datasets")

par.add_argument("-dl", nargs="+",
                 dest="dataset_list",
                 default=[],
