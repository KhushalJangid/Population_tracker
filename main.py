import pandas as pd
import numpy as np
import mysql.connector as sqlc
import matplotlib.pyplot as plt
from notif import startup,print_red,print_yellow,get_time,write_time
startup()
from fetch_data import fetch 
from command import command
from datetime import datetime 
from colorama import Fore,init
import sys
init(convert=True)
try:
    get_time()
except:
    pass
try:
    try:
        mycon=sqlc.connect(
            host="localhost",
            user='khushal',
            passwd="126444",
            database='my_project',
            auth_plugin="mysql_native_password"
            )    
        dtf=pd.read_sql("SELECT * From world_pop",mycon)       
        dtf2=pd.read_sql("SELECT * From india_pop",mycon)
    except :
        print_yellow("Loading Database from CSV file...")
        dtf=pd.read_csv("""..\\population-tracker\\csv_files\\world_pop.csv""",sep='|')
        dtf2=pd.read_csv("""..\\population-tracker\\csv_files\\india_pop.csv""",sep='|')
except :
    try:
        print_red("Error code(07): No CSV files found !")
        fetch.scrape_data_from_india()
        fetch.scrape_data_from_world()
    except:
        print_red("Error code(04): No internet connection error !\nAborting the Program")
        sys.exit()

while True:
    print(Fore.RED+'>>>>',Fore.RESET,end="")
    cmd=input().lower()
    cmd=cmd.replace(" ","")
    try:
        dtf=pd.read_sql("SELECT * From world_pop",mycon)       
        dtf2=pd.read_sql("SELECT * From india_pop",mycon)
    except :
        dtf=pd.read_csv("""..\\population-tracker\\csv_files\\world_pop.csv""",sep='|')
        dtf2=pd.read_csv("""..\\population-tracker\\csv_files\\india_pop.csv""",sep='|')
    if cmd=="updatedatabase":
        try:
            mycon=sqlc.connect(
            host="localhost",
            user='khushal',
            passwd="126444",
            database='my_project',
            auth_plugin="mysql_native_password"
            )
            command.update_database()
        except :
            print_red("Error code(03):Could not connect to mysql.")
            print_yellow("Loading Database from CSV file...")

    elif cmd == "showtables":
        print("\n1.india_population\n2.world_population")

    elif cmd == "select*fromindia_population":
        print(dtf2,"\n")
        print("Total Population of India (as of 2019) : ",sum(dtf2.Population))

        graph=input("\nWould you like to plot a Graph ? (y/n)\n")
        if graph == 'y':
            a=dtf2.plot(x="State/UT",y="Population",kind='bar')
            a=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
            a=plt.title("Population")
            b=dtf2.plot(x="State/UT",y="Density",kind='bar',color="red")
            b=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
            b=plt.title("Density")
            plt.show()

    elif cmd == "select*fromworld_population":
        print(dtf.loc[0:59,:])
        print(dtf.loc[60:119,:])
        print(dtf.loc[120:179,:])
        print(dtf.loc[180:234,:])
        print("\nTotal Population of the World (Live) : ",sum(dtf.Population))
        graph=input("\nWould you like to plot a Graph ? (y/n)\n")
        if graph == 'y':
            a=dtf.plot(x="Country",y="Population",kind='bar')
            a=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
            a=plt.title("Population")
            b=dtf.plot(x="Country",y="Density",kind='bar', color="red")
            b=plt.grid(color="black",alpha=0.3,linestyle="--",linewidth=1)
            b=plt.title("Density")
            plt.show()

    elif cmd == "selectheadfromindia_population":
        command.select_head(dtf2, "State/UT")

    elif cmd == "selectheadfromworld_population":
        command.select_head(dtf,"Country")
            
    elif cmd == "selecttailfromindia_population":
        command.select_tail(dtf2,"State/UT")

    elif cmd == "selecttailfromworld_population":
        command.select_tail(dtf,"Country")

    elif cmd=="searchinworld_population":
        command.search(dtf,"Country")

    elif cmd=="searchinindia_population":
        command.search(dtf2,"State/UT")

    elif cmd == "compareworld_population":
        command.compare(dtf,"Country")    

    elif cmd == "compareindia_population":
        command.compare(dtf2,"State/UT")  
    
    elif cmd=='dropdatabase':
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

    elif cmd in ["exit","quit"]:
        break

    elif cmd=="help":
        print_yellow('''1> show tables\t\t\t\t\t\tShows all tables in the DataBase
2> update databse\t\t\t\t\tUpdates the existing DataBase
3> select * from <table name>\t\t\t\tShows the complete data of selected table
4> select head from <table name>\t\t\tShows 20 most populated Countries/States of selcted Table
5> select tail from <table name>\t\t\tShows 20 least populated Countries/States of selcted Table
6> search in <table name>\t\t\t\tShows the selected row from the selected Table\n   Attributes : Country/State's Name
7> compare <table name>\t\t\t\t\tShows multiple selected rows from selected Table\n   Attributes : No. of Rows, Rows' names
8> drop database\t\t\t\t\tDrops the Database from MySQL connection.
9> exit/quit\t\t\t\t\t\tTerminate the Program''')

    else:
        print_red("""Error code(01) : you have an error in your syntax !
Enter 'help' for interactive help.""")



                                                           
