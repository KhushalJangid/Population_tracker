import requests
from bs4 import BeautifulSoup
import html5lib
import numpy as np
import pandas as pd
import wikipedia as wp 
import mysql.connector as sqlc
from sqlalchemy import create_engine
from to_sql import store
from notif import print_green,print_yellow,print_red
try:
    mycon=sqlc.connect(
        host="localhost",
        user='khushal',
        passwd="126444",
        database='my_project',
        auth_plugin="mysql_native_password"
        )
    mycursor = mycon.cursor()
except:
    print_red("Error code(03):Could not connect to MySQL.\n")
world_csv_loc="""C:\\Users\\Khushal\\Documents\\Python\\my_project\\world_pop.csv"""
india_csv_loc="""C:\\Users\\Khushal\\Documents\\Python\\my_project\\india_pop.csv"""

class fetch():
    def scrape_data_from_world():
        print_yellow("Fetching Data from website .....")
        #--------------------------------------------------------  Retrieving World Data from the website  ----------------------------------------------
        r=requests.get('''https://www.worldometers.info/world-population/population-by-country/''')
        soup = BeautifulSoup(r.content,features="html5lib")
        table = soup.find('table')

        #---- Generating 2-D array from Table 
        list_of_rows = []
        for row in table.find_all('tr'):
            list_of_cells = []
            for cell in row.findAll(["th","td"]):
                text = cell.text
                list_of_cells.append(text)
            list_of_rows.append(list_of_cells)
        table_content=np.array(list_of_rows)

        #----- converting array into DataFrame
        column_names=['Country','Population','Yearly_Change','Net Change','Density','Land Area (Km²)',\
                    'Migrants (net)','Fert. Rate','Med. Age','Urban Pop %','World_Share']
        dtf= pd.DataFrame(table_content[1:,1:],index=range(1,236),columns=column_names)

        #----- converting string values o int and float
        dtf['Population'] = dtf.Population.str.split(',').str.join('').astype(int)
        dtf['Density'] = dtf.Density.str.split(",").str.join('').astype(int)
        dtf['World_Share'] = dtf.World_Share.str.split('%').str.join('').astype(float)
        dtf['Yearly_Change'] = dtf.Yearly_Change.str.split('%').str.join('').astype(float)
        #--------  storing the data
        

        mycursor.execute("DROP TABLE IF EXISTS world_pop")
        print_yellow("Saving Data to MySQL and CSV .....")
        try:
            store.save_data(loc=world_csv_loc,df=dtf,name="world_pop")
            print_green("Updated Successfully !")
        except:
            print_red("Error !")

    def scrape_data_from_india():
        print_yellow("Fetching Data from website .....")
        #-------------------------------------------------  Retrieving INDIA-States data from the website  ----------------------------------------------

        r=requests.get('''http://statisticstimes.com/demographics/india/indian-states-population.php''')
        soup = BeautifulSoup(r.content,features="lxml")
        table = soup.find('table',id="table_id")
        list_of_rows = []
        for row in table.find_all('tr'):
            list_of_cells = []
            for cell in row.findAll("td"):
                text = cell.text
                list_of_cells.append(text)
            if list_of_cells!=[]:
                list_of_rows.append(list_of_cells)

        table_content=np.array(list_of_rows)
        dtf2= pd.DataFrame(table_content[:,1:],columns=['State/UT','Population','population11','increment','%','Share','contry','Rank'])

        dtf2 = dtf2.drop(['population11','increment','%','contry'], axis=1)
        dtf2=dtf2.drop(36,axis=0)
        dtf2 = dtf2.set_index('State/UT')
        dtf2['Population'] = dtf2.Population.str.split(',').str.join('').astype(int)
        dtf2['Share'] = dtf2.Share.astype(float)
        dtf2['Rank'] = dtf2.Rank.astype(int)
        dtf2=dtf2.sort_values("Population",ascending=False)


        ##---------------------  Retrieving Areas of states -------------------------

        html = wp.page("List of states and union territories of India by population").html().encode("UTF-8")

        df = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area',)[1]
        df.columns = ['Rank','State/UT','Area','Zone','Area_Share','contry','ref']

        df = df.set_index('State/UT')

        df=df.drop('India',axis=0)
        df=df.drop(['Rank','Zone','contry','ref'],axis=1)

        df['Area'] = df.Area.str.split(',').str.join('').astype(int)
        df['Area_Share'] = df.Area_Share.astype(float)
        df.rename(index={'NCT Delhi':'Delhi','Dadra and Nagar Haveli and Daman and Diu':'Dadra & Nagar Haveli and Daman & Diu',\
                        'Andaman and Nicobar Islands':'A.& N.Islands','Jammu and Kashmir':'Jammu & Kashmir'},inplace=True)
        ##----------------  Creating final DataFrame -----------------
        dtf2['Area']=df.Area
        dtf2['Area_Share']=df.Area_Share
        dtf2['Density']=dtf2['Population']/dtf2['Area']
        dtf2['State/UT']= dtf2.index

        dtf2=dtf2[['State/UT','Population','Share','Area','Area_Share','Density','Rank']]
        dtf2.index=range(1,37)

        mycursor.execute("DROP TABLE IF EXISTS india_pop")
        print_yellow("Saving Data to MySQL and CSV .....")
        try:
            store.save_data(loc=india_csv_loc,df=dtf2,name="india_pop")
            print_green("Updated Successfully !")
        except:
            print_red("Error !")

# fetch.scrape_data_from_india()
# fetch.scrape_data_from_world()





