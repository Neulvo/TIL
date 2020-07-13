# -*- coding: utf-8 -*-
"""Cluster_practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ReaA1SYMGfamHwJPM2ZD8kpbnzcujfdj

referer : https://www.kaggle.com/mbnb8317/m5-cluster-zero-one-sales-pattern

# Jaccard similarity
- measures similarities between sets
- It is defined as the size of the intersection divided by the size of the union of two sets

![image.png](data:image/png;base64,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MQmQZQge5lkVIId53bbVWgGyjY7fSUACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEp1LBygAAApRJREFUJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQgAQlIQAISkIAEJCABCUhAAhKQgAQkIAEJSEACEpCABCQggWEE/heOEZ6sJZrW6AAAAABJRU5ErkJggg==)

The logic is

1. Level 1 clustering using kernel density estimation based on missing values  

- A wide range of missing values count for all ids => To compare zero / one sales pattern, grouping ids which have similar missing distribution into one cluster.

2. Substitute original sales value

- Substitute nan for 0, 0 for -1, values > 0 for 1.

3. Level 2 clustering

- Hierarchy Clustering level 1 clusters into more groups.
"""

import numpy as np
import pandas as pd

import os

import matplotlib.pyplot as plt
import seaborn as sns

from tqdm import tqdm
from scipy.cluster.hierarchy import linkage, fcluster

import warnings
warnings.filterwarnings('ignore')

#Data from : https://www.kaggle.com/kyakovlev/m5-simple-fe?select=grid_part_1.pkl

grid_df = pd.read_pickle('/content/drive/My Drive/data/practice/grid_part_1.pkl')

grid_df.head()

#Transform to original data set from

grid_df=grid_df[['id','d','sales']].pivot(index='id',columns='d').reset_index()
ids=pd.DataFrame(grid_df['id'])

grid_df.isnull()

grid_df.tail()

grid_df=grid_df['sales'].iloc[:,:1913]

# null -> null / value > 0 ->1 , if not -> -1
grid_df=pd.DataFrame(np.where(grid_df.isnull(),np.nan,np.where(grid_df>0,1,-1)))

grid_df.head()

grid_df.tail()

grid_df.isnull()

#set columns
grid_df.columns=[f'd_{i}' for i in range(1, 1914)]

grid_df.head()

grid_df.notnull()

grid_df.notnull().tail(20)

grid_df.notnull().sum(axis=1)

d1_peak=grid_df.notnull().sum(axis=1)
cluster=d1_peak.copy()

d1_peak.tail(20)

"""referer : Plot kde plot of the number of missing values over all ids   
-> It seems he did it opposite  
-> kde plot is about existing values
"""

plt.figure(figsize=(12,6))
sns.kdeplot(d1_peak)
plt.plot([925,925],[0,0.0030]); plt.plot([1300,1300],[0,0.0030]);plt.plot([1700,1700],[0,0.0030])
plt.text(x=700,y=0.002, s="Cluster 1"); plt.text(x=1020,y=0.002,s='Cluster 2')
plt.text(x=1420, y=0.002,s='Cluster 3'); plt.text(x=2000,y=0.002,s='Cluster 4')
plt.title('# of Nan distribution')
plt.show()

#Clustering

c1_mask=(d1_peak<=925)
c2_mask=(d1_peak>925)&(d1_peak<=1300)
c3_mask=(d1_peak>1300)&(d1_peak<=1700)
c4_mask=(d1_peak>1700)

cluster[c1_mask]=1
cluster[c2_mask]=2
cluster[c3_mask]=3
cluster[c4_mask]=4

grid_df['cluster']=cluster
grid_df=grid_df.fillna(0)

grid_df['cluster'].value_counts()

"""### from referer

As you can see on above graph, cluster 4 consists an half of all ids.

So, I tried to level 2 group only for cluster 4.

Before level 2 cluster, i will show you very simple example for how Jaccard similarity is calculated.

### Jaccard similarity calculation
"""

A=np.array([1,0,0,0,1,0])
B=np.array([1,1,0,0,0,0])

np.sum(A==B)/len(A)

"""## 1. Jaccard similarity clustering"""

cluster_df=grid_df[grid_df['cluster']==1]
cluster_array=cluster_df.values
cluster_array=np.where(cluster_array==0,np.nan,cluster_array)

cluster_array

length=cluster_array.shape[0]
for i in tqdm(range(0, int(length/10))):
  for j in range(i, length):
    np.sum(cluster_array[i,:-1]==cluster_array[j,:-1])

"""it takes time

## 2. the index similar to Jaccard

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>I</mi>
  <mi>n</mi>
  <mi>d</mi>
  <mi>e</mi>
  <mi>x</mi>
  <mo>=</mo>
  <mfrac>
    <mrow>
      <mi>s</mi>
      <mi>u</mi>
      <mi>m</mi>
      <mo stretchy="false">(</mo>
      <mi>A</mi>
      <mo>==</mo>
      <mi>B</mi>
      <mo stretchy="false">)</mo>
      <mtext>&#xA0;</mtext>
      <mo>&#x2212;<!-- − --></mo>
      <mtext>&#xA0;</mtext>
      <mi>s</mi>
      <mi>u</mi>
      <mi>m</mi>
      <mo stretchy="false">(</mo>
      <mi>A</mi>
      <mo>!</mo>
      <mo>=</mo>
      <mi>B</mi>
      <mo stretchy="false">)</mo>
    </mrow>
    <mrow>
      <mi>l</mi>
      <mi>e</mi>
      <mi>n</mi>
      <mo stretchy="false">(</mo>
      <mi>A</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </mfrac>
</math>
"""

def Clustering(cluster_lv1_name, cluster_lv2_num):
    
    cluster_df = grid_df[grid_df['cluster'] == cluster_lv1_name]
    
    if cluster_lv2_num == 1:
        print('Pass : Cluster', cluster_lv1_name)
        
    else:
        print('Making dist_matrix : Cluster', cluster_lv1_name)
        cluster_array = cluster_df.values
        dist_matrix = np.dot(cluster_array, cluster_array.T)

        ## this part, linkage, takes about 30 minutes.
        ## If you have another idea for reducing running time,
        ## Please advise me !

        # hierachical clustering by method ward
        Z = linkage(dist_matrix, method='ward')
        # below link is about fcluster
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html
        cluster_num = fcluster(Z, t=cluster_lv2_num, criterion='maxclust')
        cluster_df['cluster'] = cluster_df['cluster'].astype(str) + '_' + cluster_num.astype(str)

    return cluster_df



plan_clustering ={
    #cluster_lv1_name : how many cluster_lv2 to make
    1:1,
    2:1,
    3:1,
    4:4
}

# Commented out IPython magic to ensure Python compatibility.
# %time
df_list = list()
for lv1, lv2 in plan_clustering.items():
    df_name = f'cluster_{lv1}_df'

    cluster_df = Clustering(cluster_lv1_name = lv1, cluster_lv2_num = lv2)
    #Don't know why should use code below
    globals()[df_name] = cluster_df
    
    df_list += [cluster_df['cluster']]

"""takes alot_ code above"""

cls_total=pd.concat(df_list)

cluster_df=pd.concat([ids, cls_total],axis=1)

cluster_df

cluster_df['cluster'].value_counts()

