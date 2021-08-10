'''
tsa - time series analysis module

plotting functions for time series analysis
'''

# standard imports
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# cross package imports
from ts_emergency.plotting.view import plot_single_ed

def plot_detrended(wide_df, hosp_id, ax=None):
    '''
    Plot the first difference of the ED time series
    '''
    
    # create differenced dataframe
    diff_df = wide_df.diff(periods=1)
    
    fig, ax = plot_single_ed(diff_df, hosp_id, ax)
    ax.set_title('Detrended')
    
    return fig, ax
    

def diagnostic_plot(wide_df, hosp_id, figsize=(9, 6), maxlags=56, 
                    include_zero=False):
    '''
    Basic plot of diagnostics for ED time series.
    
    1. Detrended series
    2. ACF
    3. PACF
    
    Params:
    ------
    wide_df: pandas.Dataframe
        ED data in wide format
        
    hosp_id: str
        column name for hospital
        
    figsize: (int, int), optional (default=(9,6))
        size of figure
        
    maxlags: int, optional (default=56)
        The number of lags to include int the ACF and PACF
        
    include_zero: bool, optional (default=False)
        Include ACF and PACF of observation with itself in plot (=1.0)
    
    Returns:
    -------
    fig, np.ndarray
    ''' 
    fig = plt.figure(figsize=figsize, tight_layout=True)

    # add gridspec
    gs = fig.add_gridspec(3, 2)

    # detrended axis spans two columns
    ax1 = fig.add_subplot(gs[0, :])
    # acf axis spans 2 rows in column idx 0
    ax2 = fig.add_subplot(gs[1:,0])
    # pacf axis spans 2 rows in column idx 1
    ax3 = fig.add_subplot(gs[1:, 1])
    
    # plot detrended on axis 1
    _ = plot_detrended(wide_df, hosp_id, ax=ax1)

    # plot acf on axis 2
    _ = plot_acf(wide_df[hosp_id], lags=maxlags, ax=ax2, zero=include_zero)
    # plot pacf on axi
    _ = plot_pacf(wide_df[hosp_id], lags=maxlags, ax=ax3, zero=include_zero)
    
    axs = np.array([ax1, ax2, ax3])
    return fig, axs

    