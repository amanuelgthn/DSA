#!/usr/bin/env python3
import pandas as pd


player_name = ["Bradely", "Cody", "Darwin", "Harvey", "Martin", "Harry"]
team = ["Liverpool", "Liverpool", "Liverpool", "Liverpool", "Arsenal", "Manchester United"]
number = [84, 18, 9, 19, 8, 5]
name_series = pd.Series(player_name)
team_series = pd.Series(team)
number_series = pd.Series(number)

df = pd.DataFrame({
    'Name' : name_series,
    'Team' : team_series,
    'Number': number_series
})

print(df)
print(name_series[:2])
print(df['Name'])