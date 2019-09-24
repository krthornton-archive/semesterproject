# How to Download
1. Download and install Git (https://git-scm.com)
2. Open Git bash, cd to the folder you want to download this project, and run "git clone git@github.com:krthornton/semesterproject.git"

# How to Install Docker
1. Go to https://www.docker.com/get-started and follow the instructions to install

# How to Run
1. Open up a command prompt in the project folder created by the clone from above
2. Run "docker-compose up -d --build && docker-compose logs -f" to start the docker containers and bring up their logs
3. If this is your first time running, also open another terminal and run "docker-compose run django python /code/manage.py migrate" to initiate the database
