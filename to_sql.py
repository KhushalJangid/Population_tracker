from sqlalchemy import create_engine
from notif import print_red
class store():  
    def save_data(loc,df,name="india"):
        try:
            engine=create_engine('mysql+pymysql://khushal:126444@localhost/my_project')
            conn=engine.connect()
            df.to_sql(con=conn,name=name,if_exists='replace',index=False) 
            df.to_csv(loc,sep='|')
        except :
            print_red("Error code(03):Could not connect to mysql.\nSaving Database to CSV file...")
            df.to_csv(loc,sep='|', index=False)


