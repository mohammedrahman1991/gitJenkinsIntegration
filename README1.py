# gitJenkinsIntegration
Step by Step process of using GitHub and Jenkins see below:
https://github.com/mohammedrahman1991/gitJenkinsIntegration.git



Begin:  First make sure you have Git respotory up and Running and Make sure you can make changes
step 0:  git clone https://github.com/libgit2/libgit2 make a clone of Previous Repository
then go to that repository file location and OPEN bash. should be located where original file was made

1. git add .
2. git commit -m "test1"
3. type git push [notice this may take some time of wait]
4. Done: refresh check git repository for changes on the clone


"User, now you should be able to see changes to Git repository from use IDE."

Next we must integrate with Jenkins.

1: Login in to Jenkins, enter USERNAME and PASSWORD.
this can be done at the https://localhosts.mobi/8080
Download git plugin on Manage setting
go to first Source code management, click Git, add the repository link
https://github.com/mohammedrahman1991/gitJenkinsIntegration.git

if error here for to Manage Jenkins / Global Tool Configuration / under Path to Git executable
paste location of your git.exe in computer as such: 
C:\Program Files\Git\bin\git.exe
apply then save

then go back to build in Dashboard, and it should now RUN.