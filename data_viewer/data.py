import json
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import os
from PIL import Image

raw = '''{"members":{"1":{"local_score":0,"global_score":0,"id":"0","name":"0","stars":0,"last_star_ts":0}}}'''

'''
# AoC Leaderboard Times
Get the JSON text from your leaderboard and paste it here to view everybody's specific times for each day
'''
imagefilelocation = os.path.join(os.path.dirname(__file__),"instructions.png")
st.image(Image.open(imagefilelocation),caption="Click on API, then JSON")
rawTemp = st.text_area("Paste the JSON")
raw = rawTemp if rawTemp!="" else raw
data = json.loads(raw)
members = []
for i in data["members"]:
    members.append(data["members"][i])

df = pd.json_normalize(members)
df.pop("global_score")
df.pop("last_star_ts")
df.pop("id")
for i in df:
    iparts = i.split(".")
    if iparts[0] == "completion_day_level":
        if iparts[3] == "star_index":
            df.pop(i)
        else:
            df.rename(columns={i: f"Day{iparts[1].zfill(2)}Part{iparts[2]}"},inplace=True)
df.rename(columns={"name":"Name","stars":"Stars","local_score":"Score"},inplace=True)
df.sort_index(axis="columns",inplace=True,ascending=False)
dfColumns = list(df.columns.values)
dfColumns.insert(0,dfColumns[2])
dfColumns.pop(3)
df = df[dfColumns]
df.sort_values(by="Score",inplace=True,ascending=False)
for i in range(len(df["Name"])):
    if not isinstance(df.at[i,"Name"],str):
        df.at[i,"Name"] = "No name"
def unixToTime(unixTime,dayNumber):
    if np.isnan(unixTime)==False:
        day = dt.date.fromtimestamp(unixTime)
        timetaken = dt.datetime.fromtimestamp(unixTime) - dt.datetime(day.year, 12, dayNumber)
        if timetaken.days*24*60*60 + timetaken.seconds >= 360000:
            return "Hours > 100"
        else:
            return str(timetaken.days*24 + (timetaken.seconds//60//60) - 5).zfill(2)+":"+str(timetaken.seconds//60%60).zfill(2)+":"+str(timetaken.seconds%60).zfill(2)
    else:
        return "Not done"

for i in df.columns:
    if i != "Name" and i != "Score" and i != "Stars":
        for j in range(len(df[i])):
            df.at[j,i] = unixToTime(df.at[j,i],int(i[3:5]))

nameSearch = st.text_input("Search by name")
for i in range(len(df["Name"])):
    if nameSearch not in df.at[i,"Name"].lower() :
        df.drop(i,inplace=True)

st.dataframe(df)