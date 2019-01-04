import os
from urllib.request import urlretrieve
import pandas as pd

FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data
        
    Parameters
    ----------
    filename : str (optional)
    url : str (optional)
    force_download : bool (optional)

    Returns
    -------
    data : pandas.DataFrame
    """
    
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
        
    data = pd.read_csv(filename, index_col='Date', parse_dates=True)
    data.columns = ['East', 'West']
    data['Total'] = data['East'] + data['West']
    return data

