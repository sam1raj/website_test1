from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['DB_connections']
engine = create_engine(db_connection_string)

#def load_jobs_from_db():
 #  result = conn.execute(text("select * from jobs"))
  #  jobs = []
   # for row in result.all():
    #  jobs.append(dict(row))
   # return jobs



def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM jobs"))
      jobs = []
      for row in result.mappings():
          
          jobs.append(dict(row))
      return jobs