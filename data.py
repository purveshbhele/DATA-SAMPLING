import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

"""mean=statistics.mean(data)
std_dev=statistics.stdev(data)

print("Mean is",str(mean))
print("Std_dev is",str(std_dev))

fig=ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()"""


def randomSetOfMean(counter):
        dataset=[]
        for i in range(0,counter):
                random_index=random.randint(0,len(data)-1)
                value=data[random_index]
                dataset.append(value)
        mean=statistics.mean(dataset)
        return mean


def show_fig(mean_list):
        df=mean_list
        fig=ff.create_distplot([df],["Reading_Time"],show_hist=False)
        fig.show()


def setUp():
        mean_list=[]
        for i in range(0,1000):
                setOfMeans=randomSetOfMean(100)
                mean_list.append(setOfMeans)
        show_fig(mean_list)
        std_dev=statistics.stdev(mean_list)
        print("Std_Dev of sampling distribution is",str(std_dev))

setUp()
