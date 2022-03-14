# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:42:29 2019

@author: grands1
"""
import pandas as pd
import numpy as np

# replace na with None
cm_mai_data = cm_mai_data.where((pd.notnull(cm_mai_data)), None)

cm_mai_data = cm_mai_data.replace({'TBD':pd.NaT})

a=list()
for i in cm_MAI['eqp_id']:
    a.append(type(i))

# return the number of occurences of all values in the series, first convert the series to Index and
# use value counts
b = pd.Index(a)
print(b.value_counts())

# return the dataframe with certain type in the series
# like say you need float from cm_MAI['api_industry'] in the dataframe
awsome = cm_MAI[cm_MAI['api_industry'].transform(type) == float]

# convert all nan to None in the dataframe
cm_mai_data = cm_mai_data.where((pd.notnull(cm_mai_data)), None)

# skippingrows when reading an excel file
cm_df = pd.read_excel(r'C:\Users\grands1\Downloads\CAI_October_2019_Metrics.xlsx',skiprows=4)

# from dictionary to dataframe
rej = pd.DataFrame.from_dict({'Serial Numbers':list(main_reject_dict.keys()),'Reason':list(main_reject_dict.values())})

# applying lower , upper to sereis no for loop
epower_fst_column['shpd_telematics'].str.lower()

# common elemnts between two lists
set(list(ep_df.columns))&set(list(ep_df_m.columns))

# non common elements between two lists ep_df_m is bigger than ep_df
set(list(ep_df_m.columns)).difference(set(list(ep_df.columns)))

# find in dataframe
final_df[final_df.isin(['OLY']).any(1)]

# value counts of a series
df['your_column'].value_counts(dropna=False)

# groupby
ac.groupby(['sn_pfx']).count()[['serial_number']].reset_index()

# column starting with
df.loc[:, df.columns.str.startswith('foo')]

# change datetime from '9999-12-31' fto a valid number
all_CSA_copy['CSAEndDate'] = all_CSA_copy['CSAEndDate'].astype('datetime64[ns]')
all_CSA_copy['CSAEndDate'] = all_CSA_copy['CSAEndDate'].dt.strftime('%Y-%m-%d')


# find repeated columns
{i: list(eca_data.columns).count(i) for i in list(eca_data.columns) if list(eca_data.columns).count(i) > 1 }


df = pd.read_excel(r'C:\Users\grands1\experiments.xlsx','Sheet4')

def map_values(row, values_dict):
    return values_dict[row]

values_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

df = pd.DataFrame({'INDICATOR': ['A', 'B', 'C', 'D'], 'VALUE': [10, 9, 8, 7]})

df['NEW_VALUE'] = df['INDICATOR'].apply(map_values, args = (values_dict,))

#df['NEW_VALUE'] = np.where(df['VALUE'] == 10, 10,20)

# replace with some condition.
df.loc[df['VALUE'] == 10, ['NEW_VALUE','INDICATOR']] = ['Z','ZA']
df.loc[df['VALUE'] == 7, 'NEW_VALUE'] = 'ZZ'

# apply a function on dataframe with many arguments as columns
def change(vec):
    pwc = vec[0]
    bsc_smdl_num = vec[1]
    if pwc=='C80':
        if re.match('CG137-[0-9]*', str(bsc_smdl_num)):
            return 'LEP'
        elif re.match('[\.]{1}[0-9]+)[aA-zZ]*', str(bsc_smdl_num)):
            return 'Retail'
    else:
        if re.match('^G3|^CG|^G1', str(bsc_smdl_num)):
            return 'CES'
        elif re.match('[0-9]{2}[A-Z]*|C175-[0-9]', str(bsc_smdl_num)):
            return 'LEP'
        elif re.match(',3}|^R[D|X]{1}|^ORD|G{0,1}3[', str(bsc_smdl_num)):
            return 'Retail'

final_df['gen_mgr'] = final_df[['sims_pwc','bsc_smdl_num']].apply(change,axis=1)

#Divide from a condition
og_not_rfv, og_rfv = [x for _, x in og_ui.groupby(og_ui['USER_INTERFACE'].str.strip().isin(rfv_list))]


a=dict()
for i in abc.columns:
    c=list()
    for j in abc[i]:
        c.append(type(j))
        b = pd.Index(c)
        a[i]=[b.value_counts()]



# subset a dicitonary
dd = dict((i,main_reject_dict[i]) for i in ex)

# count respective values from a dictionary
ax = {}
for i in dd.values():
    if not(i in ax):
        ax[i]=0
    ax[i]+=1

print(ax)

#snowflake
engine = create_engine(
        URL
        (
        account="cat.us-east-1",
        user="",
        password="",
        role="",
        warehouse="",
        database="",
        schema=""
    )
    )
connection = engine.connect()
sql = "select * from ZP_UPHOFDW_DB.EMD_DASH.TEST;"
pd.read_sql(sql, connection)
xd = engine.execute("SHOW DATABASES").fetchall()
xdl = [(i[1],i[2],i[3]) for i in xd]
connection.close()
engine.dispose()




#adding two dictionaries:
{**dict1,**dict2}

#adding multiple serial numbers to a dicitonary at once:
d=dict()
d.update(zip(key,value))

#adding multiple serial numbers with same value to a dicitonary at once:
d = {**d.fromkeys(list(same_electr_all_data['serial_number']),"Telematics device didn't change in 2019")}


# select last or latest value from the dataframe
trident_df = trident_csv.drop_duplicates(subset = ['SN'], keep='last')

# select the latest value from dataframe according to date
trident_full.sort_values('current_subscrp_strt_dt').drop_duplicates('serial_number',keep='last')








