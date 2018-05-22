# -*- coding: utf-8 -*-

import subprocess

subprocess.call("bin/mallet import-file --input datafile.txt --output malletfile.mallet", shell=True)
subprocess.call("bin/mallet train-classifier --input malletfile.mallet --cross-validation 10   --trainer MaxEnt --trainer NaiveBayes", shell=True)

