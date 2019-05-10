import pandas as pd
import sys
import numpy
import matplotlib.pyplot as plt
import unittest


def count_kmers(sequence, k=2):
    """ Define a function to count kmers of size k, where k is specified as an argument, and print the result """
    temp_count={}
    for i in range(len(sequence)-k+1):
                a=sequence[i:i+k]
                if a in temp_count:
                    temp_count[a] +=1
                else:
                    temp_count[a] = 1
    tx = f'The number of observed kmers of size {k} in the given sequence is {len(temp_count)}'
    return(tx)


def count_kmer_2(sequence, k=2):
    """ Define a function to count kmers of size k, where k is specified as an argument, to be used for building the dataframe """
    temp_count={}
    for i in range(len(sequence)-k+1):
                a=sequence[i:i+k]
                if a in temp_count:
                    temp_count[a] +=1
                else:
                    temp_count[a] = 1
    return(len(temp_count))


def build_frame(sequence):
    """ Define a function to create a data frame containing all possible k and the associated
number of observed and expected kmers """
    pos_k=[]
    obs_km=[]
    pos_km=[]
    for k in range(len(sequence)):
        pos_k.append(k+1)
        obs_km.append(count_kmer_2(sequence, k+1))
        pos_km.append(min(len(sequence)-k, 4**(k+1)))
        
    kmer_data_frame = pd.DataFrame(
    {'k':pos_k,'Observed_kmers':obs_km,'Possible_kmers':pos_km})
        
    return(kmer_data_frame)


def plot_kmers(sequence):
    """ Define a function to produce a graph from the data frame of the proportion of each kmer
observed """
    d=build_frame(sequence)
    plt.plot(d.Observed_kmers/d.Possible_kmers)
    plt.xlabel('Possible kmers')
    plt.ylabel('Proportion of kmers observed')


def compute_complexity(sequence):
    """ Define a function to calculate linguistic complexity """
    d=build_frame(sequence)
    ratio = (sum(d.Observed_kmers)/sum(d.Possible_kmers))
    complexity=f'The linguistic complexity of the given sequence is {ratio}'
    return(complexity)


def main_function ():
    sequence_file=str(sys.argv[1:])[2:-2] # sequence_file=str('sequence_file.txt') 
    with open(sequence_file,"r") as file1:
        sequence = file1.read()
        file1.close()
    if sequence:
        if sequence[-1]=='\n':
            sequence = sequence[:-1]
    return(count_kmers(sequence)), (build_frame(sequence)), (plot_kmers(sequence)), (compute_complexity(sequence))

main_function()
