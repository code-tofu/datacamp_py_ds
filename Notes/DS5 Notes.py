# import numpy, pandas and 
# Q: should i discriminate between numpy and pandas?
import numpy as np
import pandas as pd

#read file as a dataframe and display data info
office_df = pd.read_csv("datasets/office_episodes.csv")
pd.DataFrame.head(office_df) #office_df.head()

#NameError: name 'df' is not defined - note: methods act on the objects(i.e. office_df["column"])
top_view = office_df["viewership_mil"].max() #compared to max
top_episode = office_df["viewership_mil"].idxmax() #compared to list.index() )
top_star = office_df["guest_stars"][top_episode]
print(top_episode,top_view,top_star ) 

#try to print with labels
# The top episode is Episode
# It has million views
# It guest stars 
#filter rating/guest episodes and add colour
#import matplotlib modules
import matplotlib.pyplot as plt
#initalize a matplotlib.pyplot fig object
plt.rcParams['figure.figsize'] = [11, 7]
fig = plt.figure() 

#plotting:
# Hanging indents should add a level.
plt.scatter(
    x = office_df["episode_number"] ,
    y = office_df["viewership_mil"], #viewship already in million
#    s = ,
#    c = ,
)

# formatting:
plt.xlabel("Episode Number")
# plt.xticks
plt.ylabel("Viewership (Millions)")
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.text(80,22.5, "Episode 77 Guest Stars: Cloris Leachman, \n Jack Black, Jessica Alba")
plt.show()


# __Projects 1170__
# Use the following dataset: datasets/office_episodes.csv, which was downloaded from Kaggle.This dataset contains information on a variety of characteristics of each episode. In detail, these are:

# datasets/office_episodes.csv
# episode_number: Canonical episode number.
# season: Season in which the episode appeared.
# episode_title: Title of the episode.
# description: Description of the episode.
# ratings: Average IMDB rating.
# votes: Number of votes.
# viewership_mil: Number of US viewers in millions.
# duration: Duration in number of minutes.
# release_date: Airdate.
# guest_stars: Guest stars in the episode (if any).
# director: Director of the episode.
# writers: Writers of the episode.
# has_guests: True/False column for whether the episode contained guest stars.
# scaled_ratings: The ratings scaled from 0 (worst-reviewed) to 1 (best-reviewed).

# Create a matplotlib scatter plot of the data that contains the following attributes:
# Each episode's episode number plotted along the x-axis - __(Done)__
# Each episode's viewership (in millions) plotted along the y-axis - __(Done)__
# A color scheme reflecting the scaled ratings (not the regular ratings) of each episode, such that:
#   Ratings < 0.25 are colored "red"
#   Ratings >= 0.25 and < 0.50 are colored "orange"
#   Ratings >= 0.50 and < 0.75 are colored "lightgreen"
#   Ratings >= 0.75 are colored "darkgreen"
# A sizing system, such that episodes with guest appearances have a marker size of 250 and episodes without are sized 25
# A title, reading "Popularity, Quality, and Guest Appearances on the Office" - __(Done)__
# An x-axis label reading "Episode Number" - __(Done)__
# A y-axis label reading "Viewership (Millions)" - __(Done)__
# Provide the name of one of the guest stars (hint, there were multiple!) who was in the most watched Office episode. Save it as a string in the variable top_star (e.g. top_star = "Will Ferrell"). - __(Done)__

# Note:
# initalize a matplotlib.pyplot fig object, which you can do using the code fig = plt.figure() (provided you have imported matplotlib.pyplot as plt) - (Done)- __(Done)__ding the type, data, labels, etc) in the same cell as the one you initialize your figure (fig) - __(Done)__
# set the figure size parameters using this code (provided again you have imported matplotlib.pyplot as plt): plt.rcParams['figure.figsize'] = [11, 7] - __(Done)__
# Bonus Step: try to differentiate guest appearances not just with size, but also with a star (use a different marker.)! 
