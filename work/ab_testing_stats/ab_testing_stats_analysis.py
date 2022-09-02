
# coding: utf-8

# In[202]:


import pandas as pd

# Read the input json file into pandas dataframe
df=pd.read_json("searches.json", lines = True)



# ## Exploring the Data

# In[203]:


# Print sample
print(df.head())

# Print the dataframe dimensions
print('dataframe dimensions: {}'.format(df.shape))


# ## Cleaning The Data

# In[204]:


# remove records of users(from both design_types) which have not not logged in even once.
# we will ignore any such records. Good thing is that we do not have any such records. 
# In case we get any such records in future we are keeping the below step as in case of bad records 
# it may lead to divide by zero error while calculating search count per login value

# Also ignore the entires where is_instructor is True as these are possibly the test runs and 
# should not be considered for the experiment
df_clean=df.drop(df[(df['login_count'] == 0) | (df['is_instructor'] == True)].index)

# Reset the index to start from 0 and end at max size
df_clean = df_clean.reset_index(drop=True)


# Print sample
print(df_clean.head())

# Print the dataframe dimensions
print('dataframe dimensions: {}'.format(df_clean.shape))


# ## Preparing the Data

# In[205]:


# Add column design_type which has information about the type of design (A or B) shown to given user
df_clean['design_type']=df_clean.apply(lambda x: 'A' if x['uid'] % 2 == 0 else 'B', axis=1)


# search_count_per_login field will be used for identifying most often search usage in a desgin
#df_clean.loc[:,'search_count_per_login']=df_clean.loc[:,'search_count']/df_clean.loc[:,'login_count']
df_clean['search_count_per_login']=df_clean['search_count']/df_clean['login_count']

# Print sample
print(df_clean.head())


# # Question: Did more users use the search feature in the new design (B)?
# 
# ### To answer this question we find the percentage of users in each design_types who have used the search 
# ### and verify if for group design_types: B the percentage of users using the search is higher than that of 
# ### group design_types: A.

# In[206]:


# Total number of users of each design
n_users_designA=df_clean[df_clean['design_type'] == 'A'].shape[0]
n_users_designB=df_clean[df_clean['design_type'] == 'B'].shape[0]

print('Users count of design A : {}'.format(n_users_designA))
print('Users count of design B : {}'.format(n_users_designB))


# Number of users in each design who have used the search feature
n_users_usingSearch_designA=df_clean[(df_clean['design_type'] == 'A') & (df_clean['search_count'] > 0)].shape[0]
n_users_usingSearch_designB=df_clean[(df_clean['design_type'] == 'B') & (df_clean['search_count'] > 0)].shape[0]

print('Users count of design A which have used the search feature: {}'.format(n_users_usingSearch_designA))
print('Users count of design B which have used the search feature: {}'.format(n_users_usingSearch_designB))


# Percentage of users in each design type who have used the search feature
userPercentage_usingSearch_designA=round(((n_users_usingSearch_designA/n_users_designA)*100),2)
userPercentage_usingSearch_designB=round(((n_users_usingSearch_designB/n_users_designB)*100),2)

print('Users percentage in design A which have used the search feature: {}'.format(userPercentage_usingSearch_designA))
print('Users percentage in design B which have used the search feature: {}'.format(userPercentage_usingSearch_designB))


# # Answer: Did more users use the search feature in the new design (B)? FALSE

# In[207]:


print('Did more users use the search feature in the new design (B): {}'.format(userPercentage_usingSearch_designB                                                                             > userPercentage_usingSearch_designA))



# # Question: Did users search more often in the new design (B)?
# 
# ### To answer this question we find the mean of the field "search_count_per_login" for users 
# ### in each group and the group which has higher mean is the one in which the search feature 
# ### is used more frequently.

# In[208]:


# Get mean of search_count_per_login in each group
mean_search_count_per_login_designA=round(df_clean[df_clean['design_type'] == 'A']['search_count_per_login'].mean(),2)
mean_search_count_per_login_designB=round(df_clean[df_clean['design_type'] == 'B']['search_count_per_login'].mean(),2)

# Print mean values
print('mean usage of search feature in design A: {}'.format(mean_search_count_per_login_designA))
print('mean usage of search feature in design B: {}'.format(mean_search_count_per_login_designB))


# # Question: Did users search more often in the new design (B)? FALSE
# 

# In[209]:


print('Did users search more often in the new design (B) : {}'.format(mean_search_count_per_login_designB                                                                             > mean_search_count_per_login_designA))

