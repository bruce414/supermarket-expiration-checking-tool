import pandas as pd
from datetime import datetime
import heapq

# import the csv file, read it, then assign it to data_file
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSYLlVRwTaHQdijPwol0uVaLef035498ZRmUBCVGUpOC6Dcm7ecflygv3XJQJj1w6Z4NBwPUNrl18B0/pub?gid=0&single=true&output=csv"
data_file = pd.read_csv(csv_url)

print(data_file)

# get the current date
current_datetime = datetime.today()
print(current_datetime)


data_volume = data_file.shape[0]
print(data_volume)
        

    



