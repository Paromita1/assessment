
pip install xlrd


# ### Creating csv files
# #### Reading corresponding sheets from the given excel files and writing it into dataframes. All the dataframes, each containing a sheet information, are concatenated into a single dataframe. Using 'to_csv' function, the resultant dataframe is converted into corresponding csv file.

# In[1]:


import pandas as pd
df1 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1')
df2 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_1')
df3 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_2')
df4 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_3')
df5 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_4')
df6 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_5')
df7 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_6')
frames1 = [df1, df2, df3, df4, df5, df6, df7]
final_df = pd.concat(frames1)
final_df.to_csv('detail.csv')
print("CSV file :'detail.csv' created")


# In[2]:


import pandas as pd
df1 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1')
df2 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_1')
df3 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_2')
df4 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_3')
df5 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_4')
df6 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_5')
df7 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_6')
frames2 = [df1, df2, df3, df4, df5, df6, df7]
final_df = pd.concat(frames2)
final_df.to_csv('detailvol.csv')
print("CSV file :'detailvol.csv' created")


# In[3]:


import pandas as pd
df1 = pd.read_excel('data.xls', sheet_name ='DetailTemp_67_1_1')
df2 = pd.read_excel('data.xls', sheet_name ='DetailTemp_67_1_1_1')
df3 = pd.read_excel('data.xls', sheet_name ='DetailTemp_67_1_1_2')
df4 = pd.read_excel('data_1.xls', sheet_name ='DetailTemp_67_1_1_3')
df5 = pd.read_excel('data_1.xls', sheet_name ='DetailTemp_67_1_1_4')
df6 = pd.read_excel('data_1.xls', sheet_name ='DetailTemp_67_1_1_5')
df7 = pd.read_excel('data_1.xls', sheet_name ='DetailTemp_67_1_1_6')
frames3 = [df1, df2, df3, df4, df5, df6, df7]
final_df = pd.concat(frames3)
final_df.to_csv('detailtemp.csv')
print("CSV file :'detailtemp.csv' created")
