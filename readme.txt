Installation Manual: https://flask.palletsprojects.com/en/2.0.x/installation/
To add requirements.txt: pip freeze > requirements.txt

Run the project (local)
a. Go to Project folder
b. activate the environment: venv\Scripts\activate
c. (optional) pip install -r requirements.txt 
d. set FLASK_APP=index
e. flask run


Push changes to github
a. git add .
b. git commit -m "commit"
c. (optional) git remote add origin https://github.com/minna-lproc/madayaw.git
d. (optional) git remote -v
e. git push origin main

For remote changes
a. git pull origin main

Deploy to App Engine

DNS Map to UIC server
