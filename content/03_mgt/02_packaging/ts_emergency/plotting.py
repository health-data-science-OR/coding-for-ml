import matplotlib.pyplot as plt

DEFAULT_LABEL_FS = 12
DEFAULT_AXIS_FS = 12
DEFAULT_FIGSIZE = (12,8)

def plot_single_ed(wide_df, hosp_id, figsize=(12,3), 
                   fontsize=DEFAULT_LABEL_FS, line_width=2):
    '''
    Plot a single ED's data
    Assumes data are passed in wide format.
    
    Params:
    -------
    wide_df: pandas.Dataframe
        ED time series data in wide format
        
    hosp_id: str
        name of hospital column to plot e.g. 'hosp_1'
        
    figsize: tuple(int, int), optional (default=(12,3))
        `matplotlib` figure size 
        
    fontsize: int, optional (default=DEFAULT_LABEL_FS)
        Size of label font
        
    line_width: int
        Width of the line plot
        
    Returns:
    -------
    matplotlib fig, ax
            
    '''
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot()
    ax.set_xlabel("Date", fontsize=fontsize)
    ax.set_ylabel("Attendances", fontsize=fontsize)

    _ = ax.plot(wide_df[hosp_id], lw=line_width)
    # include x, y grid 
    _ = ax.grid(ls='--')

    # set size of x, y ticks
    _ = ax.tick_params(axis='both', labelsize=fontsize)

    # return the figure
    return fig, ax


def plot_eds(wide_df, figsize=DEFAULT_FIGSIZE, label_font_size=DEFAULT_LABEL_FS, 
             axis_font_size=DEFAULT_AXIS_FS):
    '''
    Plot all ED's attendances in a 1x4 grid layout.
    
    Params:
    ------
    wide_df: pandas.Dataframe
        ED time series data in wide format

    figsize: tuple(int, int), optional (default=(12,3))
        `matplotlib` figure size 
        
    label_font_size: int, optional (default=DEFAULT_LABEL_FS)
        Size of label font
        
    axis_font_size: int, optional (default=DEFAULT_AXIS_FS)
        Size of axis tick font
    
    Returns:
    --------
    matplotlib fig
    '''
             
    fig, axs = plt.subplots(nrows=4, ncols=1, tight_layout=True, figsize=(12,8),
                            sharex=True)

    # note that axs is a 2D array
    for hosp_idx in range(0, 4):
        _ = axs[hosp_idx].plot(wide_df[f'hosp_{hosp_idx+1}'])
        _ = axs[hosp_idx].set_title(f'Hospital {hosp_idx+1}', 
                                    fontsize=label_font_size)
        _ = axs[hosp_idx].grid(ls='--')

    # axis labels matplotlib >=3.4 
    AXIS_LABEL_SIZE = 12
    _ = fig.supylabel('ED Attendances', fontsize=axis_font_size)
    _ = fig.supxlabel('Date', fontsize=axis_font_size)
             
    return fig