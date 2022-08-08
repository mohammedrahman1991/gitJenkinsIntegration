Installing Rest Assured and run first Assertion/validation: on path to learn END TO END API automation testing

1. we need to understand PostMan manuel API testing first as foundation
2. we download IntelliJ
3. open maven 
4. make sure java installed 17 or below
5. add 4 major depencies
6. go to mvn repository website: add depenecy
a. testNG
b. hamcrest
c. selenium java client 
d. Rest assured 

save click lifecycle on maven tab
install
Build sucess
save all
reopen maven file

go to src go to test
Create new JAVA CLASS

you are ready for Rest assured API automation.

NOTE: this is important
hamcrest will say in outiput once u run program:
error:
" cannot access org.hamcrest.Matcher class file for org.hamcrest Matcher not found"
to fix this:
1. go to Maven pom.xml file
2. go to dependencies
3. find hamcrest details
4. delete last line where it has info to SCOPE.
after delete save all
reopen maven file / report inteliJ

now run program, it should automate successfully.


How to run assertions on specfic JSON data body
we will
1st look at validated JSON "scope" value based on payload/body from actual
continue previous code from .then()
this is validations method
all validations are continued here
just use "." and write the new method for more validations

so we continue but before we do, we must access the liberary from the hamcrest depenency so we do not have an error

go top and type import static org.hamcrest.Matches.*;
then go back to method and write:
.body
so in body
("Scope" the scope needs to go with correct match parameters based on hamcrest method
so  ("Scope", equalTo ("APP"))
this will allow to create validations on automated regarding specific details of Body and look at scope.

2nd Key validation:
do validations on Server to make sure you are hacked or not. Look at Apache version
this is done on all API tests
so we do a response validation on the server header
u find header new response body after send request
go to bottom then tab to Headers
type .header method into intelliJ
this is like input,
but this is output validation

so how to use package
create package in main class or its child
then create new class
then create new method inside class
then go back to makin code source
copy or cut the long code of JSON body
paste into return method of the class/method of new Payload file
go back to place where u cut the JSON body
type the class.method() and it will replace long strand of code.

this is vital to make code look more smooth
Code should be running
if issues check syntax error
import the new package
make sure no red errors when typing code
run code see if it runs 
any errors read and find error
and fix slowly
be calm and collected