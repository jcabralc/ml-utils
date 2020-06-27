# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:42:30 2019

@author: Jessica Cabral
"""

############################################################################
#                          TOOLS SCRIPT                                   #
############################################################################


# Function to Detection Outlier on one-dimentional datasets.
def find_anomalies(random_data):
    from scipy import std, mean
    import random 
    random.seed(1)
    anomalies = []
    # Set upper and lower limit to 3 standard deviation
    random_data_std = std(random_data)
    random_data_mean = mean(random_data)
    anomaly_cut_off = random_data_std * 3
    
    lower_limit  = random_data_mean - anomaly_cut_off 
    upper_limit = random_data_mean + anomaly_cut_off
    print(lower_limit)
    # Generate outliers
    for outlier in random_data:
        if outlier > upper_limit or outlier < lower_limit:
            anomalies.append(outlier)
    return anomalies

# A tabela "Informações em nível de classe" lista os níveis de todas as variáveis passadas a funcao. 
# Similar a tabela "Class Level Information" do SAS
def Class_Level_Information(df, features):
    # cria dataframe vazio
    Class_Level_Information = DataFrame(columns=['Class', 'Levels', 'Values'])
    # coleta infos de cada feature
    for idx, feat in enumerate(features):
        Class_Level_Information.loc[idx, 'Class'] = feat
        Class_Level_Information.loc[idx, 'Levels'] = len(DataFrame(df[feat].value_counts()).index)
        Class_Level_Information.loc[idx, 'Values'] = DataFrame(df[feat].value_counts()).index.tolist()
    display(Class_Level_Information)