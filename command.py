
import pandas as pd
import numpy as np
import mysql.connector as sqlc
import matplotlib.pyplot as plt
from notif import print_red
from fetch_data import fetch 
try:
    mycon=sqlc.connect(
                host="localhost",
                user='khushal',
                passwd="126444",
                database='my_project',
                auth_plugin="mysql_native_password"
                )
except:
    print_red("Error code(03):Could not connect to mysql.")

class command():
    def update_database(*args):
        try:
            fetch.scrape_data_from_world()
            fetch.scrape_data_from_india()
        except:
            try:
                print_red("Error code(04): No internet connection error !")
                dtf=pd.read_sql("SELECT * From world_pop",mycon)       
                dtf2=pd.read_sql("SELECT * From india_pop",mycon)
            except :
                print_red("Error code(03):Could not connect to mysql.")
                print_yellow("Loading Database from CSV file...")
                dtf=pd.read_csv("""..\\population-tracker\\csv_files\\world_pop.csv""",sep='|')
                dtf2=pd.read_csv("""..\\population-tracker\\csv_files\\india_pop.csv""",sep='|')
    def select_head(dtf,xaxis="text"):
        print(dtf.head(20))
        graph=input("\nWould you like to plot a Graph ? (y/n)\n")
        if graph == 'y':
            a=dtf.head(20).plot(x=xaxis,y="Population",kind='bar')
            a=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
            a=plt.title("Population")
            b=dtf.head(20).plot(x=xaxis,y="Density",kind='bar',color="red")
            b=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
            b=plt.title("Density")
            plt.show()
    def select_tail(dtf,xaxis="text"):
        print(dtf.tail(20))
        graph=input("\nWould you like to plot a Graph ? (y/n)\n")
        if graph == 'y':
            a=dtf.tail(20).plot(x=xaxis,y="Population",kind='bar')
            a=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
            a=plt.title("Population")
            b=dtf.tail(20).plot(x=xaxis,y="Density",kind='bar',color="red")
            b=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
            b=plt.title("Density")
            plt.show()
    def search(dtf,country="country"):
        try:
            dtf.index= dtf[country]
            col=input("Enter Row Name : ")
            print("\n",dtf.loc[col,:])
        except:
            print_red("Error code(05): Search term not found in selected table !\n(hint: First letter of every word should be capital)")
    def compare(dtf,xaxis="country"):
        dtf.index= dtf[xaxis]
        try:
            x=int(input("No. of Rows : "))
            col=[]
            for i in range(0,x):
                inp=input("Name of Row : ")             
                data=inp
                col.append(data)
            slice_=dtf.loc[dtf.index.intersection(col)]
            print(slice_)
            graph=input("\nWould you like to plot a Graph ? (y/n)\n")
            if graph == 'y':
                a=slice_.plot(x=xaxis,y="Population",kind='bar')
                a=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
                a=plt.title("Population")
                b=slice_.head(20).plot(x=xaxis,y="Density",kind='bar',color="red")
                b=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
                b=plt.title("Density")
                plt.show()           
        except:
           print_red("Error code(02): Wrong input in the specified datatype !")

     
