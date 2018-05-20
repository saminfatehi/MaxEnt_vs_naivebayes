# -*- coding: utf-8 -*-

import subprocess

subprocess.call("bin/mallet import-file --input datafile.txt --output malletfile.mallet", shell=True)
subprocess.call("bin/mallet train-classifier --input malletfile.mallet --training-portion 0.9   --trainer MaxEnt --trainer NaiveBayes", shell=True)

