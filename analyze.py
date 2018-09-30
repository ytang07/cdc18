import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics as s
import math

# takes in the .csv file and returns a 2d list
# each entry of the list represents a 6 field data point 
def csv_to_data(csv_file):
    data = []
    with open(csv_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        for row in readCSV:
            data.append(row)
    data.pop(0)
    return data

# takes in a filename and returns the a list with each entry as an int
def sdata_to_int(filename):
    f1 = csv_to_data(filename)
    for row in range(len(f1)):
        for d in range(3):
            f1[row][d] = int(f1[row][d])
    return f1

# analyze takes a file that has already been processed by sdata_to_int
def analyze(file):
    # create an array of differences between team score and opponent score
    # create a list of shots (0s and 1s)
    diffs = []
    shots = []
    for row in range(len(file)):
        diffs.append(file[row][1] - file[row][2])
        shots.append(file[row][0])
    
    # create different lists for when teams are 5 or more points behind, within 5 points, or 5 or more points ahead
    behind = []
    about = []
    ahead = []
    
    # 
    for d in range(len(diffs)):
        if (diffs[d] < 5 and diffs[d] > -5):
            about.append(shots[d])
        elif(diffs[d] <= -5):
            behind.append(shots[d])
        elif(diffs[d] >= 5):
            ahead.append(shots[d])
    # retun a list of means,sd for behind, about, and ahead respectively
    return (s.mean(behind), math.sqrt(abs(s.mean(behind)*(1-s.mean(behind)))/len(behind)), s.mean(about), math.sqrt(abs(s.mean(about)*(1-s.mean(about)))/len(about)), s.mean(ahead), math.sqrt(abs(s.mean(ahead)*(1-s.mean(ahead)))/len(ahead)))

'''load data sets'''
#f1 = sdata_to_int('one_left2_scorediff.csv')
#f2 = sdata_to_int('four_left2_scorediff.csv')
#f3 = sdata_to_int('five_left2_scorediff.csv')
#f4 = sdata_to_int('one_right2_scorediff.csv')
#f5 = sdata_to_int('four_right2_scorediff.csv')
#f6 = sdata_to_int('five_right2_scorediff.csv')
#f7 = sdata_to_int('one_mid2_scorediff.csv')
#f8 = sdata_to_int('four_mid2_scorediff.csv')
#f9 = sdata_to_int('five_mid2_scorediff.csv')
t1 = sdata_to_int('one_left3_scorediff.csv')
t2 = sdata_to_int('four_left3_scorediff.csv')
t3 = sdata_to_int('five_left3_scorediff.csv')
t4 = sdata_to_int('one_right3_scorediff.csv')
t5 = sdata_to_int('four_right3_scorediff.csv')
t6 = sdata_to_int('five_right3_scorediff.csv')
t7 = sdata_to_int('one_mid3_scorediff.csv')
t8 = sdata_to_int('four_mid3_scorediff.csv')
t9 = sdata_to_int('five_mid3_scorediff.csv')

''' print the mean/sd pairs '''
#print(analyze(f1))
#print(analyze(f2))
#print(analyze(f3))
#print(analyze(f4))
#print(analyze(f5))
#print(analyze(f6))
#print(analyze(f7))
#print(analyze(f8))
#print(analyze(f9))
#print(analyze(t1))
#print(analyze(t4))
#print(analyze(t7))
#print(analyze(t2))
#print(analyze(t5))
#print(analyze(t8))
#print(analyze(t3))
#print(analyze(t6))
#print(analyze(t9))

# gets 99% confidence intervals from a 6 entry data array produced from analyze
def conf(data):
    bconf_l = data[0]-3*data[1]
    bconf_u = data[0]+3*data[1]
    tconf_l = data[2]-3*data[3]
    tconf_u = data[2]+3*data[3]
    aconf_l = data[4]-3*data[5]
    aconf_u = data[4]+3*data[5]
    return (bconf_l, bconf_u, tconf_l, tconf_u, aconf_l, aconf_u)

'''prints confidence intervals'''
#print("1 appearance")
#print(conf(analyze(f1)))
#print(conf(analyze(f4)))
#print(conf(analyze(f7)))
#print("2,3,4")
#print(conf(analyze(f2)))
#print(conf(analyze(f5)))
#print(conf(analyze(f9)))
#print("5 or more")
#print(conf(analyze(f3)))
#print(conf(analyze(f6)))
#print(conf(analyze(f9)))

''' 3 point data sets ''' 
print("1 appearance")
print(conf(analyze(t1)))
print(conf(analyze(t4)))
print(conf(analyze(t7)))
print("2,3,4")
print(conf(analyze(t2)))
print(conf(analyze(t5)))
print(conf(analyze(t8)))
print("5 or more")
print(conf(analyze(t3)))
print(conf(analyze(t6)))
print(conf(analyze(t9)))