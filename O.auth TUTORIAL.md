THis IS HOW to generate Google Access token and get JSON body for gmail account

login to gmai account
open postman

go to console.cloud.google.com
go to libraries
access data beloning to Google user
enable BLUE BOX click
enable API

set up consent screen:
external user type create it
application name: Post MAN tRAINING [ANYTHING U WANT]
gmail for support email
dont need any domains
real application uses domain name etc
require when integrating gmail API with actual Application

click SAVE


go to creditentials create
GMAIL API
click on gmail api
create credentials 
o.auth  client ID
what application type: Webapplication
name: any u want [webclinet1]

authorized redirect URL is required:
https://oauth.pstmn.io/vi/callback
this url always remains the same
o.auth client ID will be created

u have client ID:
and client secret:

u need this info for postman



go to post man
create new collection name it gmail
create get reuqest name it [get messages] this is email messages
This is first reuqest method
require URL
go back to google API references:
REQUEST URL is at top first link

click on users.messages LIst
get type request with end point
go to references see link

copy request url [endpoint]
it has parameters

there is Authorization:
u need this to get access to gmail
go to scope this makes authorization have limits

go to Postman create variable userID in global put email there
on the URL end point paraments requires USER ID {{USERid}}
this will grab variable from environment and use it for URL request END POINT

go to authorization tab
generate access token
how to do it:
click: get new access token
if first time: it will be blank
provide all data
token name: gmaik
grant type: authorization code
callback URL is https://oauth.pstmn.io/vi/callback
auth URL: provile: https://accounts.google.com/o/oauth2/auth
client ID: go to API section [edit dashbooard] in gmail go to api details edit button
copy paste iD
copy paste Secret ID:
scope: paste the scope as talked about prior scope determines the limit
u can provide all access or simply modify 
modify is suggested so everything is not altered in email.

click create acess token
postman will try to open Mozila and pop up will open for a verification
allow pop ups
sign in gmail and allow this particular action
click allow again

then postman pop will show  access granted Green signal
post man will say authentication complete
both places needs signal browser and postman
now u have gernated token successfully and u can use it.

delete previous tokens as it gets changed for security purposes
need to generate again every session
API gets authenticated again

now click use token
automatically avaiable in ppostman available token list
select it

NOw send blue button and see the status is 200
shows time
and u will get a list of all messages in Body
this gets a list of all messages

now u can go further in gmail API
u get get message as well

get all details u can use  get message go to google api info page and click get
explains parameters requires

go add another REQUEST in postman
get specific message name
or get by ID
use end point profivded in google api info list copy paste into new endpoint in postman

gmail envioronment
usid varriabel in parameter /ID 
go to authentication tab use token from previous
if invalid generate new one
it will generate MESSAGES for that particular ID
u can grab value and put into tests if u want

it is a useful API where u can validate scenrionrs where u sent
emails and u validate by opening gmail and valfidating the details

this is normal while working on automations
opening gmail
and verifying message has content or not.

all info can be found here in this youtube video link: 
https://www.youtube.com/watch?v=x7uG1-H0aDU




