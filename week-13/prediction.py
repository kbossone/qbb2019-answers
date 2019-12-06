#!/usr/bin/env python2

import sys
import hifive
import numpy

rna = open(sys.argv[1])
activity = open(sys.argv[2])

rnal = {}
activityl = {}

# to make filtered files
for i, line in enumerate(rna):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if int(col[1]) >= 5000000 and int(col[2])<=40000000:
        index = (int(col[1])-5000000)/5000
        rnal[index] = col[4]

for i, line in enumerate(activity):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if int(col[1]) >= 5000000 and int(col[2])<=40000000:
        index = (int(col[1])-5000000)/5000
        activityl[index] = col[4]
        
interaction_activity = {}

hic = hifive.HiC('PROJECT_FNAME', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)

for index in rnal:
    int_act = 0
    for index2 in activityl:
        int_act += float(activityl[index2]) * data[index][index2]
    interaction_activity[index] = int_act
# print(interaction_activity)

rna_expression_list = []
interaction_activity_list = []

for index in rnal:
    rna_expression_list.append(float(rnal[index]))
    interaction_activity_list.append(interaction_activity[index])

rna_array = numpy.array(rna_expression_list)
interaction_activity_array = numpy.array(interaction_activity_list)

R_value = numpy.corrcoef(rna_array, interaction_activity_array)[0, 1]
# print R_value

for key in rnal:
    print key, interaction_activity[key]