First download Java
make sure bash file .shenv in main folder says :
export JAVA_HOME=/Users/mohammedrahman/Library/Java/JavaVirtualMachines/jdk-17.0.4.jdk/Contents/Home
export ANDROID_HOME=/Users/mohammedrahman/Library/Android/sdk

once u have this run java on terminal

open intelliJ 
STEP 1: SELECT SDK ; it must match that of Java version open 17.0.4
now u will see src file in directory:

Step 2: Add maven dependencies
go to pom.xml

Meneu: 
code generate
search testNG hit enter

then u must SAVE ALL

go to right side and click on MAVEN tab

here u go to Lifecycle
click Install

check terminal it should say BUILD SUCCESS
now dependencies have been added

maven now has TESTng



