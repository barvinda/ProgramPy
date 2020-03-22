from requests import get
from bs4 import BeautifulSoup
from time import sleep, time
from random import randint
from IPython.core.display import clear_output
from warnings import warn

#creating a list
l=[]

pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2000,2008)]

#preparing the monitoring of the loop
start_time=time()
requests=0

#for years between '01-'07
for year in years_url:

    #for pages 1-4 in those years
    for page in pages:

        #response (using get)
        r = get("https://www.imdb.com/search/title/?release_date=" + year + "&sort=num_votes,desc&page=" + page)

        #pause the requests between 8 and 15 secs (to make it seem more human and not get IP banned)
        sleep(randint(8,15))

        #Monitoring all the requests sent out
        requests += 1
        elapsed_time = time() - start_time
        print("Request:{}; Frequency:{} requests/s".format(requests, requests/elapsed_time))
        #to keep the terminal clean
        clear_output(wait = True)


        if r.status_code !=200:
            warn("Request:{}; Status code:{}".format(requests,r.status_code))

        #break the loop if number of requests is more than 72
        if requests > 72:
            warn("Number of requests was greater than expected.")
            break

        #parsing the html
        soup=BeautifulSoup(r.text,"html.parser")

        #variable of the class all of the movies have
        movie_containers=soup.find_all("div", class_ = "lister-item mode-advanced")

        #scraping the data for all movies
        for items in movie_containers:
            if items.find("div", class_="ratings-metascore") is not None:

                #defining the dictionary
                d={}
                d["Names"] = items.h3.a.text

                d["Year"] = items.h3.find("span", class_="lister-item-year text-muted unbold").text

                d["IMDb Rating"] = float(items.strong.text)

                d["MetaScore"] = int(items.find("span", class_="metascore").text)

                d["Votes"] = int(items.find("span", attrs = {"name":"nv"})["data-value"])

                #putting all the info into the dictionary
                l.append(d)


import pandas

#storing the data into a dataframe
df=pandas.DataFrame(l)

#cleaning up the data
#removing the () from the year
df.loc[:, 'Year'] = df['Year'].str[-5:-1].astype(int)

#standardising the imdb rating
df["n_IMDb"] = df["IMDb Rating"]*10

#convert to csv
df.to_csv("IMDb Movies 2000-2007")


# In[ ]:
