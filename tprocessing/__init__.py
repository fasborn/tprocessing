import pandas as pd
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np
import itertools

import gc
#gc.collect()

way = r"C:\Users\kgoiaev001\Documents\Other\Температура\Температура\Tttr\Tttr"
way_catalogue = r"C:\Users\kgoiaev001\Documents\Other\Температура\Температура\Tttr\Каталог.xlsx"

onlyfiles = [f for f in listdir(way) if isfile(join(way, f))]


#dictionary = dict(zip(keys, values))

{'a': 1, 'b': 2, 'c': 3}
"""
df = pd.DataFrame()
i = 0
list_ = []
for item in onlyfiles:
    i+=1
    temp = pd.read_fwf(way+"/"+item)
    list_.append(temp)
    #df = pd.concat([df, temp])
    print(item, i)
"""


#---------------------------------------------------------------------------------------------------
#Reading names of all files from a storage
lis = pd.DataFrame(onlyfiles, columns = ["ch"])
#["ch"].str.replace(".dat", "")#[0].str.split(".")
lis["Identifier"] = lis["ch"].str.replace(".dat", "")
lis["Identifier"] = lis["Identifier"].astype(int)

#Reading catalog from a storage
catalogue = pd.read_excel(way_catalogue, skiprows=1)
catalogue = catalogue[catalogue.columns[2:9]]

#Creating dictionary from a dataframe
cities = dict()
cities = dict(zip(catalogue["Индекс ВМО"].to_list(), catalogue["Наименование станции"].to_list()))

#Creating reversed dictionary
catal_map = catalogue[["Наименование станции", "Индекс ВМО"]].set_index(keys = "Наименование станции").to_dict()
catal_map = catal_map['Индекс ВМО']

#Map from identifier to the filename
lis_dict = lis[["Identifier", "ch"]].set_index(keys = "Identifier").to_dict()["ch"]


#List of columns in the files
list_of_columns = ["Индекс ВМО станции",
                  "Год",
                  "Месяц",
                  "День",
                  "TFLAG",
                  "TMIN",
                  "QTMIN",
                  "TMEAN",
                  "QTMEAN",
                  "TMAX",
                  "QTMAX",
                  "R - суточная сумма осадков",
                  "CR",
                  "QR"]




#Data positions in the files
widths  = [(0,5), 
           (6, 10), 
           (11, 14), 
           (14, 16), 
           (17, 18), 
           (19, 24), 
           (25, 26), 
           (27, 32), 
           (33, 34), 
           (35, 40), 
           (41, 42),
           (43, 48),
           (49, 50),
           (51, 52)]

#Function to read file into dataframe
def read_df(city, columns = list_of_columns):
    temp = catal_map[city]
    temp = lis_dict[temp]
    df = pd.read_fwf(way+"/"+temp, header = None, colspecs=widths)
    df.columns =  columns
    return df


def new_read_df (city, columns = list_of_columns):
    for item in list(catal_map.keys()):
        if city in item:
            print('We have found city "'+ item + '"')
            temp = catal_map[item]
            temp = lis_dict[temp]
            df = pd.read_fwf(way+"/"+temp, header = None, colspecs=widths)
            df.columns =  columns
            return df
    return "No such city presented"