
import pandas as pd
from datetime import datetime

class DataLoader:

    def __init__(self, df=None): 
        self.df = df

    @classmethod
    def from_file(cls, path_data):

        with open(path_data, 'r') as f: 
            data = f.readlines()[500:600]
            data = [d.strip().split(';') for d in data]

        df = pd.DataFrame(data).rename(columns=dict(enumerate(['timestamp_str', 'last_price', 'bid_price', 'ask_price', 'volume'])))
        return cls(df)
    

    def process_dataframe(self): 

        self.df['timestamp'] = self.df.timestamp_str.apply(self.format_time)
        self.df.drop('timestamp_str', axis=1, inplace=True)
        self.df.set_index('timestamp', inplace=True)
        return self.df

    @staticmethod
    def format_time(timestamp: str): 
        '''convert time stamp from Tick Replay Format (Sub Second 
        Granularity) to datetime'''
        date_format = '%Y%m%d %H%M%S %f0'
        date_obj = datetime.strptime(timestamp, date_format)
        return date_obj


    def aggregate_operations(): 
        # aggregate HiLo by 610 operations (use volume column)
        pass

    def plot(self, window_size, n_operation=610): 
        # plot the last price here. 
        pass

