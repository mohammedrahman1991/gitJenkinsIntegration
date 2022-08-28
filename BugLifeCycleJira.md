How to create Bug
1. create Bug on Jira
2. this requres to login and write steps
3. these steps are labeled 1,2,3,4,5 which explain the step to replicate bug
1. go to Url
2. check logo
3. refresh page
4. see missing slogan under the logo

Actual: missing phrase
Expected: logo slogan should be present under the logo

troubleshoot: go to browser network settings find END point of this Get call
copy the JSON response and paste it to POSTMAN
copy end point also paste it
verify JSON payload 
verify status code

find error 404

this indicates this that there is an error with this specific endpoint

Take screenshots of bug and past into JIRA report
add my own priorty as HGIH with low Severity


What happens next?

What is BUG LIFE CYCLE?
since i created a Bug, my QA TEAM LEAD was able to know right away [New]
i also let team know about this priority and severity  in my next Standup later that day

this BUG would be labeled as Open once developer takes a look at it [Open]

once it is fixed, the status will change to [Fixed]
then it will be assigned to me [Assigned]
dev may give a speicfic JSON payload to test against this endpoint 
or another set of tasks this will change status to [PendingTest]
during testing cycle its changed to [Retest]
once completed [verfied]
then [closed]
if issues comes against next spint [may create new Bug report again
or label previous bug as [Reopened]

if this bug report was previously made by another QA LABel as [Duplicate]
if priority is low, and we can set it to next sprint [Deferred]

more details: https://www.guru99.com/defect-life-cycle.html