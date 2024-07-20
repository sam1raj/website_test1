from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://sql12721125:Ufppd3fC4Q@sql12.freemysqlhosting.net/sql12721125?charset=utf8mb4")

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