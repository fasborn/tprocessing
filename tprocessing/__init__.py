import pandas as pd
from os import listdir
from os.path import isfile, join

import gc
#gc.collect()

class tdat:
    def __init__(self, way, catalogue):
        self.onlyfiles = [f for f in listdir(way) if isfile(join(way, f))]
        self.catal = catalogue
        
        #Reading names of all files from a storage
        self.lis = pd.DataFrame(self.onlyfiles, columns = ["file"])
        self.lis["Identifier"] = self.lis["file"].str.replace(".dat", "")
        self.lis["Identifier"] = self.lis["Identifier"].astype(int)

        #Creating dictionary from a dataframe
        self.catal_map = dict(zip(self.catal["Наименование станции"].to_list(), self.catal["Индекс ВМО"].to_list()))

        #Map from identifier to the filename
        self.lis_dict = dict(zip(self.lis["Identifier"].to_list(), self.lis["file"].to_list()))
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
    def read_df(self, city, columns = list_of_columns):
        temp = self.catal_map[city]
        temp = self.lis_dict[temp]
        df = pd.read_fwf(self.way+"/"+temp, header = None, colspecs=self.widths)
        df.columns =  columns
        return df


    def new_read_df (self, city, columns = list_of_columns):
        for item in list(self.catal_map.keys()):
            if city in item:
                print('We have found city "'+ item + '"')
                temp = self.catal_map[item]
                temp = self.lis_dict[temp]
                df = pd.read_fwf(self.way+"/"+temp, header = None, colspecs=self.widths)
                df.columns =  columns
                return df
        return "No such city presented"