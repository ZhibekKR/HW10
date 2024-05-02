import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

get_unique_values = data['whoAmI'].unique() #get unique values
new_data_frame = pd.DataFrame(0, index=data.index, columns=get_unique_values) #create a dataframe with zeros

#fill the new dataframe
for column in get_unique_values:
    new_data_frame[column] = (data['whoAmI'] == column).astype(int)

new_data_frame.head()
