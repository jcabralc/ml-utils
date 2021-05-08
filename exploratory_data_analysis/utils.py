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

def pareto_plot(df, x=None, y=None, title=None, show_pct_y=False, pct_format='{0:.0%}'):
    """ Generates a Pareto Chart 

    Parameters:
    ------------
    df: 
        pandas dataframe with data you want to plot
    x: 
        x feature
    y: 
        y feature
    title: 
        plot title
    show_pct_y: 
        If you want to show a second y axis with percentage values
    pct_format:
        The format to show the percentage value in the plot
    """
    xlabel = x
    ylabel = y
    tmp = df.sort_values(x)
    x = tmp[x].values
    y = tmp[y].values
    weights = y / y.sum()
    cumsum = weights.cumsum()
    
    fig, ax1 = plt.subplots()
    ax1.bar(x, y)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)

    ax2 = ax1.twinx()
    ax2.plot(x, cumsum, '-ro', alpha=0.5)
    ax2.set_ylabel('', color='r')
    ax2.tick_params('y', colors='r')
    
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['{:,.2%}'.format(x) for x in vals])

    # hide y-labels on right side
    if not show_pct_y:
        ax2.set_yticks([])
    
    formatted_weights = [pct_format.format(x) for x in cumsum]
    for i, txt in enumerate(formatted_weights):
        ax2.annotate(txt, (x[i], cumsum[i]), fontweight='heavy')    
    
    if title:
        plt.title(title)
    
    plt.show()
