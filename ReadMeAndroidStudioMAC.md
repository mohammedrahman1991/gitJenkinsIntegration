First login into Jenkins
go to website login

admin is original password;



open new Port:

go to path C:\Windows\System32\cmd.exe
go to terminal and insert command:
open new port 

java -jar jenkins.war --httpPort=8080
after this paste this ont browser of choice:  https://localhosts.mobi/8080
 

 login id and password; this is ADMIN login and pass, u get it first, so SAVE IT [important]


if 8080 gives error use 9090

see statement on CMD:  Jenkins is fully up and running
jenins is initialized into the specific port

u have gained access to jenkins on port 8080 good job
save to git hub



Here we FIX APPIUM


Step 1: Download Android Studio MAC
this is similar to InteliJ
install then OPEN empty 
then let ide install JDK and libraries
and wait

download ADP

for MAC OS:
download Homebrew
google search homebrew
copy paste link on website onto Command line
put password and let it download Homebrew
type brew --version
check installation is there or not
once u have Brew installed

go google search Appium
then click official link 
scroll down to find commands to install node.js into terminal

copy paste into terminal and install
type node -v
check version once installed 
INSTALL APPIUM copy paste next command from website
type: npm install -g appium
tpye next command
tpye: npm install wd [this downloads appium client]

installation complete
type appium into command
u can now RUN apppium

Now install desktop version of appium:
this will allow u to inspect elements and provide a GUI feelings
search appium desktop version into google
go to github page
download the mac .dmg file
copy to applications
run app
it will say sysstem has found malicious activity and cannot be trusted
go System Preferences
go to Security and Pivacy
under Genral tab
you will see Open Anyway click on it when it states regarding Appium

Open Appium Desktop Version
error might come once u try to Run it this is because u have 2 isntances of Port 
being used

close one.
either terminal or here and refresh
u can reopen and Appium will Run 

How to Run on Command Appium:
type Appium 

either close terminal or desktop client and run in ONE.
port needs be to free to start appium

Install Appium Doctor to check installation and dependencies
this is important for testers

go to: https://www.npmjs.com/package/appium-doctor
follow commands to install:

into command: 
npm install appium-doctor -g
type npm audit fix
fixed any vulnerabilities these are issues pre existing and command adjusts to it
npm install appium-doctor -g

it will run and install doctor
check installation"
type: appium-doctor -v
coomands should appear


test
type appium-doctor --ios

errors will show that it needs dependencies

u can use brew and fix some
type brew update
type brew install carthage 

this will isntall this depenecies problems still needed to fix

more dependecies to install are listed in this error messages
can be added

for xcrun: error: unable to find utility "simctl" 
download XCODE

