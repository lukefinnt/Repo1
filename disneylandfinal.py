# 1) Real World Scenario Project should use a real world dataset and include a reference of their source in the report [1]

# CSV was downloaded from https://www.kaggle.com/arushchillar/disneyland-reviews

# 2) Importing data
# Your project should make use of one or more of the following, [1]
# • Relational Database or API or Web
# Scraping
# • Import a CSV file into a Pandas DataFrame. [1]

import pandas as pd
file = '/Users/luketuohey/Desktop/copyDisneylandReviews.csv'
df = pd.read_csv(file,encoding='latin-1')

import chardet
with open(file, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
result

df

print(df.head())

print(df.shape)

df.dtypes

# 3) Analyzing data

# • Your project should include sorting, indexing,
# grouping. [1]


# • Replace missing values or dropping duplicates.
# [1]


# • Slicing, loc or iloc. [1]


# • Looping, iterrows [1]

# • Merge dataframes [1]



# 4) Python
# • Use functions to create reusable code. [1]
# • Numpy. [1]
# • Dictionary or Lists. [1]



# 5) Visualize
# • Seaborn, Matplotlib [2]




# 6) Generate Valuable Insights
# • 5 insights from the visualization. [2]



# let's play with the data a bit to get an idea of what we are dealing with if there are duplicate values to drop



df.isnull().sum()


df.columns

df.isnull().sum()

df_row = df.dropna(axis=0)

df_row.shape

df_col = df.dropna(axis=1)

df_col.shape

zero_fill_data = df.fillna(0)

zero_fill_data.isnull().sum()

df_filled = df.fillna(method = "ffill",axis=0).fillna(0)

df_filled.isnull().sum()

disney = df.drop_duplicates(subset=['Review_ID'])

print(df.shape)

print(disney.shape)

# new dataframe with duplicate review IDs dropped is called 'disney'
# null values have been checked for

disney

print(disney.head)
#let's play a bit with the loc and iloc functions to make sure it's working

disney.loc[1:12,"Review_ID":"Review_Text"]

disney.iloc[0:12, 1:3]











# some insight ideas i might explore with my data in this project:
# 	Post popular park overall on average - park with the highest rating on average
#o	Least popular park overall - branch with the lowst rating on average
#o	Where do people from certain locations prefer
#o	If I am from Ireland which one will I prefer the most

# let's play around with the data a bit more to get a better understanding of it with a view
# to answering questions similar to the ones above as the insights reveal themselves to us

disney.describe()



disney.iloc[0]

disney.iloc[0,0]

disney.loc[0]

disney.loc[0,'Year_Month']

print (disney.values)

print (disney.columns)

# Sort df by Rating
disney_rating = disney.sort_values("Rating")

# Print the top few rows
print(disney_rating.head())

# Sort df by Rating
disney_rating = disney.sort_values("Rating",ascending=False)

# Print the top few rows
print(disney_rating.head())

# Sort df by branch, then descending rating
disney_rating_branch = disney.sort_values(["Rating", "Branch"], ascending=[False, True])


# Print the top few rows
print(disney_rating_branch.head())

disney

# Ok that's enough experimenting. Now lets try to answer:
# what is the average rating for each park (and can that be represented visually)
disney['Rating'].mean()


disney['Rating'].mean()

disney.median()

disney.describe()

disney['Rating'].count()

disney['Rating'].value_counts()

#lets see more about disneyland paris specifically

disney = df.drop_duplicates(subset=['Review_ID'])

paris = disney['Branch']== 'Disneyland_Paris'

disney.loc[paris]

disney.loc[paris]['Rating'].mean()

hk = disney['Branch']== 'Disneyland_HongKong'

disney.loc[hk]['Rating'].mean()

cf = disney['Branch']== 'Disneyland_California'

disney.loc[cf]['Rating'].mean()

#great success! I got the average overall ratings for each of the parks. Now how would I visualise that?

disney.loc[cf]['Rating'].value_counts()

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Paris','Hong Kong','California')
y_pos = np.arange(len(objects))
performance = [3.96,4.20,4.40]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Rating out of 5')
plt.title('Overall Average Review rating')

plt.show()

uk = disney['Reviewer_Location']== 'United Kingdom'


uk

disney.loc[uk]

#this is average rating UK reviewers give, but how do I sub divide that so i can see what english
#people give for each site?

disney.loc[uk]['Rating'].mean()

disney.loc[paris]['Rating'].mean()

#need to figure out group by, like how do I see the average reating for disney paris by UK visitors, by US visitors,
# etc then visualise


disney['Reviewer_Location'].value_counts()

reviewer_location_grp = disney.groupby(['Reviewer_Location'])

reviewer_location_grp

reviewer_location_grp.get_group('United Kingdom')

reviewer_location_grp['Rating'].agg(['median','mean']).loc['France']

branch_and_reviewer_location_grp = disney.groupby(['Reviewer_Location','Branch'])

branch_and_reviewer_location_grp['Rating'].mean

branch_and_reviewer_location_grp['Rating'].mean().loc['Ireland']

#this is the correct code for being able to see the average rating for each branch for each
#viewer location! with this I can already answer questions like, where do people from Ireland, united states,etc prefer


#what is the favourite branch of americans?
branch_and_reviewer_location_grp['Rating'].mean().loc['United States']


#what is the favourite branch of people from the UK?
branch_and_reviewer_location_grp['Rating'].mean().loc['United Kingdom']

#what is the favourite branch of people from the Hong Kong?
branch_and_reviewer_location_grp['Rating'].mean().loc['Hong Kong']

#i have all the code i am going to run for the the figures to deliver some insights. Now i just need to visualise them
# in some simple visuals
# will list here the data i will visualise, and then will visualise them


# what ratings do people from ireland give the different parks, and how does it differ from the overall averages we saw
# where cali was best, KH second , and paris last?

branch_and_reviewer_location_grp['Rating'].mean().loc['Ireland']

# with this we can see that the irish actually prefer disney land paris! and the rating is dead even for the other
# 2 branches

# lets visualise the numbers for Irish visitors of the parks

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Disneyland California', 'Disneyland HongKong', 'Disneyland Paris')
y_pos = np.arange(len(objects))
performance = [4.14,4.14,4.26]

plt.barh(y_pos, performance, align='center', alpha=0.9)
plt.yticks(y_pos, objects)
plt.xlabel('User experience score out of 5')
plt.title('Irish visitor preferred Disney Park')

plt.show()

#what about the americans? what park do they like the most and does it differ much from the overall average?

branch_and_reviewer_location_grp['Rating'].mean().loc['United States']


# how can we visuaise the preference of the americans in a pie chart to give an idea of the proportion of
# the preference for their own park verusus the others?


import matplotlib.pyplot as plt

labels = ['Disneyland California', 'Disneyland HongKong', 'Disneyland_Paris']
sizes = [40.6,38.4,31]
colors = ['yellowgreen', 'gold', 'lightskyblue']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()

#that's just a rough idea of the proportional sizes (just because pie charts are fun to make!) but its not the most
# appropriate way to visualise the data here.
# its better that we also take a look at the numbers in a clear bar chart to show which parks the americans like best

#Disneyland_California    4.393839
#Disneyland_HongKong      4.145952
#Disneyland_Paris         3.735338

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Disneyland California', 'Disneyland HongKong', 'Disneyland_Paris')
y_pos = np.arange(len(objects))
performance = [4.39,4.14,3.73]

plt.bar(y_pos, performance, align='center', alpha=0.7)
plt.xticks(y_pos, objects)
plt.ylabel('Rating out of 5')
plt.title('American visitor preferred Disney Park')

plt.show()

#so we can see that the americans and irish have different taste in disney parks for sure. Let's see that head
# to head now to really get the proper picture of the preference difference

import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 3
irish_visitors = (4.14,4.14,4.26)
american_visitors = (4.39,4.14,3.73)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, irish_visitors, bar_width,
alpha=opacity,
color='b',
label='Irish Visitors')

rects2 = plt.bar(index + bar_width, american_visitors, bar_width,
alpha=opacity,
color='g',
label='American Visitors')

plt.xlabel('Parks')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('Disneyland California', 'Disneyland HongKong', 'Disneyland Paris'))
plt.legend()

plt.tight_layout()
plt.show()

#and with that we have a good few insights into how people experience the different disney parks!
#overall average preference order was california, hong kong, then paris
#the americans loved their own park more than the average but like disney paris worse than the average score
#irish fans bucked the trend by preferring paris the most then scoring the cali andhk parks the same
#visitors from hong kong liked paris more than the americans but not as much as the irish, and preferred x as well
#overall where could we recommend you visit? with an overall average rating of x for all of the parks, you are quite
#likely to have a good time in any one you go to, but if you are american you might be advised
#to save yourself the trip to paris and enjoy disney in california a bit closer to home!
#and for the irish the same is true -- they should save money not going to america, and get a cheap ryanair flight to
#paris to enjoy disney paris, since on average the irish prefer that park anyway!
#thanks for reading!