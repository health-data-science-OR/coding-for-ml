'''
Functions to load built in datasets for ts_emergency.
Datasets are downloaded from an external github repo.

The key loading function is load_ed_ts
'''

import pandas as pd
import numpy as np

LONG_URL = 'https://raw.githubusercontent.com/health-data-science-OR/' \
            + 'hpdm139-datasets/main/syn_ts_ed_long.csv'

WIDE_URL = 'https://raw.githubusercontent.com/health-data-science-OR/' \
            + 'hpdm139-datasets/main/syn_ts_ed_wide.csv'

def load_ed_ts(data_format='wide', as_pandas=True):
    '''
    Load the built-in ED dataset
    
    Params:
    ------
    data_format: str
        'Wide' or 'long' format.  Wide format provides hospital columns.
        Long format provides a categorical hospital column and single attends
        column.
        
    as_pandas: bool, optional (default = True)
        Return as `pandas.Dataframe`.  If False then `numpy.ndarray`
        
    Returns:
    -------
    pandas.Dataframe or if `as_pandas=False` then returns `numpy.ndarray`
    
    '''
    valid_formats = ['wide', 'w', 'long', 'l']
    
    if data_format.lower() not in valid_formats:
        raise ArgumentError(f'data format should be one of {valid_formats}')

    if data_format == 'wide' or data_format == 'w':
        df = _ed_data_to_wide(LONG_URL)
    else:
        df = _ed_data_to_long(WIDE_URL)
    
    if as_pandas:
        return df
    else:
        return df.to_numpy()
        
        
 
def _ed_data_to_wide(file_path):
    '''
    Return the ED data in wide format.
    
    1. Pivot table
    2. Transpose and drop the ('attends', hosp_i) multi-index
    3. Rename columns [0, 1, 2, 4] tp ['hosp_1', 'hosp_2', 'hosp_3', 'hosp_4']
    4. Index to DateTimeIndex
    5. Drop the additional uneeded series 'date' (as stored in index as well)
    6. Convert attendence numbers from int64 to int16
    
    Params:
    ------
    file_path: str
        Path to wide format file
        
    Returns:
    -------
    pandas.DataFrame
    '''
    # column name transfers
    translated_names = {0:'hosp_1', 
                        1:'hosp_2',
                        2:'hosp_3',
                        3:'hosp_4'}

    data_types = {'hosp_1':np.int16, 
                  'hosp_2':np.int16,
                  'hosp_3':np.int16,
                  'hosp_4':np.int16}

    df = (pd.read_csv(file_path)
            .pivot_table(values=['attends'], index=['date'], columns=['hosp'])
            .T.reset_index(drop=True)
            .T.rename(columns=translated_names)
            .assign(date=lambda x: pd.to_datetime(x.index))
            .set_index('date')
            .astype(data_types)
         )

    return df



def _ed_data_to_long(file_path):
    '''
    Return the ED data in long format. Uses pd.wide_to_long()
    Assume wide format file is used.
    
    1. pd.wide_to_long()
    2. reset_index() to remove multi-index
    3. rename col 'hosp_'  to 'attends'
    4. date to datetime
    5. Convert attendence numbers from int64 to int16 amd hosp_id to int8.
    (could also be a categorical field.)
    
    Params:
    ------
    file_path: str
        Path to wide format file
        
    Returns:
    -------
    pandas.DataFrame
    '''

    translated_names = {'hosp_':'attends'}
    data_types = {'hosp': np.int8, 'attends':np.int16}

    long_df = ( 
                pd.wide_to_long(pd.read_csv(file_path), stubnames='hosp_', 
                                i=['date'], j='hosp')
                .reset_index()
                .rename(columns=translated_names)
                .assign(date=lambda x: pd.to_datetime(x['date']))
                .astype(data_types)
                )

    return long_df
