# Prereqs
1. First, make sure you have Docker installed and ready to go. [Here][1] is a link to download docker and [here][2] are instructions on how to set it up.
2. Also, go grab the latest version of git from [here][3].
3. Download and install the latest version of PyCharm from [here][4]. Some of the features we'll be using require the professional version but don't worry, you can sign up for free with your school account [here][5]. Once you install it, go ahead and open it up and sign in to your freshly made pro account.

# Setup Dev Env
1. Open up git bash and change directory to where ever you want to download this example project and run the following:

   ```git clone https://github.com/krthornton/semesterproject.git```

2. Once that completes, open up PyCharm. On the splash screen, select "Open" and navigate to where you downloaded the project. Select the root `semesterproject` folder and open it in PyCharm.
3. In the top right of your screen will be a dropdown with `Django Runserver` in it. Select this and change to `Run Docker`.
4. Click the green play button! A bunch of consoles should open at the bottom of your screen (this is good). If this is your first time running this, it might take a second to download and build the necessary docker images. This is a one time process and it won't take this long everytime.
5. Once the docker containers are finished starting up: In the bottom left of your window there should be a list containg "Docker" and below that should be "Compose: docker-compose.yml". Expand this. Below that, expand "django". Right click on the container "/django" and choose "Exec".
7. In the popup menu, selct "Create" and type in `/bin/bash` into the box that pops up. This will give you a shell within the docker container running the Django webserver and DB. Any issues that arise with the DB or the webserver in general can be fixed through this so be familiar with it!
6. Skip down to the bottom of this readme and follow the instructions titled "How to Rebuild the Database". Come back here when you're done.
7. Finally, open up a browser and goto http://localhost:8080. If everything went well, this should land you on the homepage of my DCSP project!

[1]: https://download.docker.com/win/stable/Docker%20Desktop%20Installer.exe
[2]: https://docs.docker.com/docker-for-windows/install-windows-home/
[3]: https://git-scm.com/download/win
[4]: https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows
[5]: https://www.jetbrains.com/shop/eform/students

# How to Run the Web Server w/ Pycharm
1. Open the semesterproject folder in Pycharm
2. Click the "Configurations" dropdown from the top right (next to the play button)
3. Choose "Run Docker"
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
1. Check for and make any new migrations by running:

   ```python manage.py makemigrations app```
2. Now actually run the migrations by running:

   ```python manage.py migrate```
3. Finally, rebuild the DB by running:

   ```python manage.py shell < project/init_db.py```

hello world! soma;lkdsjf ligma joe mama what about yuri? tarded
