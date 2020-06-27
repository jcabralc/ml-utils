'''
ANOVA
Show information about the dataset and most relevante features

Parameters:
    df: Dataset to Analyse
    features: List of Features to Analyse
    dep_feature: Dependence Feature
    frac = Fraction of Data in Dataset to Analyse. Default is 1.0 (100%, all the data)
    random_state = Default is 1
    anova_form = Formula to fit the Linear Model
    ss_type = Squares Type (1, 2 or 3). Int or List of ints
    
The Sum of Squares Type I (SS1) allows to verify if the inclusion of additional variables in the model represents a significant marginal contribution;
The Sum of Squares Type III (SS3) allows to verify, considering all the other explanatory variables of the model, the marginal contribution of a variable is significant;
'''
def ANOVA_diagnostics(df, features, dep_feature, anova_form, ss_type, frac=1.0, random_state=1):
    from pandas import DataFrame
    # colect sample os data based on frac parameter
    frac_df = df.sample(frac=frac,  random_state= random_state)
    # Create Class Level Information Table
    print('------ Class Level Information Table ------ \n')
    Class_Level_Information = DataFrame(columns=['Class', 'Levels', 'Values'])
    # Colect info for each feature
    for idx, feat in enumerate(features):
        Class_Level_Information.loc[idx, 'Class'] = feat
        Class_Level_Information.loc[idx, 'Levels'] = len(DataFrame(frac_df[feat].value_counts()).index)
        Class_Level_Information.loc[idx, 'Values'] = DataFrame(frac_df[feat].value_counts()).index.tolist()
    display(Class_Level_Information)
    # Show Observations Read/Used
    display(DataFrame({'Number of Observations Read': df.shape[0], 
                       'Number of Observations Used': [frac_df.shape[0]]}).T)
    # info from the Dependent Variable
    print('\n------ Dependent Variable: {} ------ '.format(dep_feature))
    # ANOVA
    moore_lm = ols(anova_form, data=frac_df).fit()
    print('\n------ Model Statistics ------ ')
    display(moore_lm.summary())
    if (type(ss_type) == list):
        for typ in ss_type:
            print('\n ------ ANOVA Type {} SS ------ '.format(typ))
            anova_table = sm.stats.anova_lm(moore_lm, typ=typ)
            display(anova_table)
            print('------  Most significant variables based on SS ------ ')
            display(anova_table.sort_values(by='sum_sq', ascending=False)[:5])
            
    
    print('\n------ Diagnostic Plots ------ ')
    diagnostic_plots(frac_df[features], frac_df[dep_feature], model_fit=moore_lm)
    
    