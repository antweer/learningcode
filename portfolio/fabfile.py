from fabric.api import run, put, env, sudo, cd, prefix

env.hosts = ['104.236.213.240']
env.user = 'tanweer'

DIR = '/home/tanweer/learningdjango/portfolio'
VENV = 'source /home/tanweer/.virtualenvs/learningdjango/bin/activate && source SECRETS.ENV'

def start ():
  with cd(DIR):
    with prefix(VENV):
      run('pm2 start uwsgi -- --ini uwsgi.ini > start.log')
      
def stop ():
  run('pm2 stop all > stop.log')
  
def deploy ():
  with cd(DIR):
    run('git pull')
    
    with prefix(VENV):
      run('pip install -r requirements.txt  > install.log')
      run('python manage.py migrate')
    
    put('db.sqlite3', '/home/tanweer/learningdjango/portfolio')  
    run('pm2 restart all > restart.log')
    
def hello ():
  print("Hello")