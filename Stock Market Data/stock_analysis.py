from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components, file_html
from bokeh.resources import CDN

#Setting the dates
start=datetime.datetime(2020,1,1)
end=datetime.datetime(2020,3,24)

#collecting the data from yahoo
df = data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)

#Function to have more control over the code

#functions to get intermediary values on the dataframe, making plotting easier
def inc_dec(c,o):
    if c > o:
        value="Increase"
    if c < o:
        value="Decrease"
    if c == o:
        value="Equal"
    return value

#differentiate between green and red
df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
#for the y-axis
df["Middle"]=(df.Open+df.Close)/2
#for the height of the rectangle
df["Height"]=abs(df.Close-df.Open)

#framing the chart
p=figure(x_axis_type="datetime",width=1000,height=300, title="Stock Market", sizing_mode="scale_both")
p.grid.grid_line_alpha=0.3

#the graph is seperated by miliseconds(width of the rectangle)
hours_12=12*60*60*1000

#defining the segment
p.segment(df.index,df.High,df.index,df.Low, color="black")

#2 different rectangles for the positive and negative values
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],
       hours_12, df.Height[df.Status=="Increase"],fill_color="green",line_color="black",fill_alpha=0.7)
p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],hours_12,
       df.Height[df.Status=="Decrease"],fill_color="red",line_color="black",fill_alpha=0.7)

#output file locally
output_file("CS.html")
show(p)
