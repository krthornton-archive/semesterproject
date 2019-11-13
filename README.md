# How to Download
1. Download git from https://git-scm.com
2. Using git, run "git clone https://github.com/krthornton/semesterproject"
3. If you don't already have python3, install it

# How to do First Time Setup
1. Open a command prompt in the semesterproject folder
2. Run "python3 -m pip install pipenv"
3. Once complete, run "pipenv install". This sets up a virtual environment to run the django web server in.

# How to Run the Web Server w/o Pycharm
1. Open a command prompt in the semesterproject folder
2. Run, "pipenv shell" to activate the virtual environment
3. cd to the code directory
4. Run, "python manage.py runserver localhost:8080"

# How to Run the Web Server w/ Pycharm
1. Open the semesterproject folder in Pycharm
2. Click the "Configurations" dropdown from the top right (next to the play button)
3. Choose "Django Runserver"
4. Click the green Play button

# How to Merge w/ Pycharm
1. Make your changes to the code
2. In Pycharm, in the bottom right click on "Git:_____" and choose "New Branch"
3. Name the new branch something meaningful to your changes (ligma does not count)
4. In the bottom left, click on "Version Control"
5. Click the green check-mark
6. Select all files you intend to push to the repo and type up a commit message
7. In the bottom right, choose the drop down under "Commit" and choose "Commit and Push"
8. Go to 'https://github.com/krthornton/semesterproject/branches' in your browser
9. Select your branch and select "Create Pull Request"

# How to Rebuild the Database
1. Open a terminal and cd to the "code" directory
2. Activate pipenv by running ```pipenv shell```
3. Delete the old database by running ```rm mydatabase```
4. Check for and make any new migrations by running ```python manage.py makemigrations app```
5. Now actually run the migrations by running ```python manage.py migrate```
6. Finally, rebuild the DB by running ```python manage.py shell < project/init_db.py```

hello world! soma;lkdsjf ligma joe mama what about yuri? tarded
