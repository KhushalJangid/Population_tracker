
import pandas as pd
import numpy as np
import mysql.connector as sqlc
import matplotlib.pyplot as plt
from notif import print_red
from fetch_data import fetch 

class command():
    def update_database():
        try:
            fetch.scrape_data_from_world()
            fetch.scrape_data_from_india()
        except:
            try:
                print_red("Error code(04): No internet connection error !")
                dtf=pd.read_sql("SELECT * From world_pop",mycon)       
                dtf2=pd.read_sql("SELECT * From india_pop",mycon)
            except :
                print_red("Error code(03):Could not connect to mysql.\nLoading Database from CSV file...")
                dtf=pd.read_csv("""c:\\Users\\Khushal\\Documents\\Python\\my_project\\world_pop.csv""",sep='|')
                dtf2=pd.read_csv("""c:\\Users\\Khushal\\Documents\\Python\\my_project\\india_pop.csv""",sep='|')
    def select_head(dtf,xaxis="text"):
        print(dtf.head(20))
        graph=input("\nWould you like to plot a Graph ? (y/n)\n")
        if graph == 'y':
            a=dtf.head(20).plot(x=xaxis,y="Population",kind='bar')
            b=dtf.head(20).plot(x=xaxis,y="Density",kind='bar',color="red")
            plt.show()
    def select_tail(dtf,xaxis="text"):
        print(dtf.tail(20))
        graph=input("\nWould you like to plot a Graph ? (y/n)\n")
        if graph == 'y':
            a= dtf.tail(20).plot(x=xaxis,y="Population",kind='bar')
            b=dtf.tail(20).plot(x=xaxis,y="Density",kind='bar',color="red")
            plt.show()
    def search(dtf,country="country"):
        try:
            dtf.index= dtf[country]
            col=input("Enter Row Name : ")
            print(dtf.loc[col,:])
        except:
            print_red("Error code(05): Search term does not maches the index of selected table !")
    def compare(dtf,xaxis="country"):
        dtf.index= dtf[xaxis]
        try:
            x=int(input("No. of Rows : "))
            col=[]
            for i in range(0,x):
                inp=input("Name of Country : ")             
                data=inp
                col.append(data)
            slice_=dtf.loc[col]
            print(slice_)
            graph=input("\nWould you like to plot a Graph ? (y/n)\n")
            if graph == 'y':
                a= slice_.plot(x=xaxis,y="Population",kind='bar',width=0.5)
                b=slice_.plot(x=xaxis,y="Density",kind='bar',color="red")
                plt.show()           
        except:
            print_red("Error code(02): Wrong input in the specified datatype !")
    def drop_database():
        try:
            mycon=sqlc.connect(
            host="localhost",
            user='khushal',
            passwd="126444",
            database='my_project',
            auth_plugin="mysql_native_password"
            )
            mycursor = mycon.cursor()
            mycursor.execute("DROP TABLE world_pop")
            mycursor.execute("DROP TABLE india_pop")
        except:
            print_red("Error code(06): No Table to drop")
