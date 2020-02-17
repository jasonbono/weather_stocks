import pandas as pd



def split_types(_df):
    """
    input: a dataframe with the features n_good and n_bad
    
    output: two dataframes, which represent subsets of the original
    Rows are selected only if they represent a day where the weather changed
    from good to bad (df_bad) or bad to good (df_good)
    """

    df_good = _df.copy()
    mask = _df["n_good"] == 1
    df_good = _df[mask]
    
    df_bad = _df.copy()
    mask = _df["n_bad"] == 1
    df_bad = _df[mask]
    return df_good,df_bad



def normal_stock_move(_df,spread_type='emean'):
    """
    input: a dataframe with daily relative stock movments (PercentChange)

    output: the mean and optionaly the spread for the price movements of each year
    """
    mean = _df['PercentChange'].mean()
    if (spread_type == 'rms'):
        spread = _df['PercentChange'].var()**(1/2)

    elif (spread_type == 'emean'):
        spread = _df['PercentChange'].sem()
    else:
        return mean
    return mean,spread



def remove_stock_outliers(_df,nsigma=3):
    """
    input: a dataframe with daily relative stock movments (PercentChange)
    
    output: a dataframe with a cut on the stock moments that lie outside of the natural distribution (nominally 3 sigma)
    """
    df = _df.copy()
    mean = df['PercentChange'].mean()
    rms = df['PercentChange'].var()**(1/2)
    #apply a mask to keep only values within n sigmas of the mean
    vals = df['PercentChange']
    mask = (vals < mean + nsigma*rms) & (vals > mean - nsigma*rms)
    df = df[mask]
    return df
    



