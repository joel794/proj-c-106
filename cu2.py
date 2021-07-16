import plotly.express as px
import csv

with open ('sale of tv.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = 'Size', y = 'Average time')
    fig.show()
    




