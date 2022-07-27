HOW to swtich JAVA jdk on basher

to to mac folder application
type command up
coomand up
until u cannot any more

go to MAC computer 
mine is called untitled
open
go to users
go to name: mohammedrahman
go to .zshenv
open this is file where java version can be updated and where ANDROID_HOME has to be updated
so computer knows what version and where and location of SDK

type:

export JAVA_HOME=/Users/mohammedrahman/Library/Java/JavaVirtualMachines/jdk-17.0.4.jdk/Contents/Home
export ANDROID_HOME=/Users/mohammedrahman/Library/Android/sdk


notice: MAKE sure that EXPORT is type in lower case
it may auto fix, so click left button manually and make sure it is lower case

then command S
save

go to terminal run java -version
see changed version to java

run appium-doctor 
see changes
error regarding ADP for emulator should be resovled.

ANDROID STUIOD should be running fine and u can run TESTs now.


notice: also close other IDE so we can run smoothly
as these apps require lots of RAM