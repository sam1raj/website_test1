from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
'id':1,
  'title':'test1',
  'location':'tokyo',
'salary':'10000'
 },
{
'id':2,
  'title':'test3',
  'location':'osaka',
'salary':'10000'
 },
{
'id':3,
  'title':'test3',
  'location':'kyoto'

 },
  {
  'id':4,
    'title':'test4',
    'location':'nagano',
  'salary':'10000'
   }
]


@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS, 
                         company_name = 'samir sites')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS) 


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
