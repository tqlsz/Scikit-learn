import numpy as np
import urllib

# url with dataset

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

raw_data = urllib.urlopen(url)

# load the csv file as a numpy matrix

dataset = np.loadtxt(raw_data, delimiter=",")
print type(dataset)

# separate the data from the target attributes

X = dataset[:, 0:7]
print X
print '----------------------------------'
Y = dataset[:,8]
print Y

