import SCBDB
import time
import shelve
from kommun_mapper import kommunDict
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import kommun_mapper
import matplotlib.pyplot as plt

kommuner = kommun_mapper.kommunDict()

print(len(kommuner))
X =[]
d = shelve.open('kommundata')
d['1080'] = SCBDB.SCBData(1080).featureList
i = 0
for kommun in kommuner:

    if kommun == '1080' or kommun == '1214' or kommun == '1233' or kommun == '1260' or kommun == '1440' or kommun == '2034' or  kommun == '2061' or kommun == '2313' or kommun == '2403' or kommun == '2421' or kommun == '1214':
        continue

    X.append(d[kommun])

X = np.matrix(X)
print(X)



db = DBSCAN().fit(X)

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

unique_labels = set(labels)

print(unique_labels)