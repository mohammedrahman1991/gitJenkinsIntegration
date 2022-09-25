Selenium Interview Qs

1. Pre-requisites to create and execute Tests using WebDriver:
1) Web Element Locators (To Identify Elements/Objects)

2) WebDriver Methods (To Perform Operations on Elements)

3) Java Programming Concepts (To Enhance Tests or Test Cases)
------

2. Element Locators: To recognize the element in the web pages:
i) id

ii) name

iii) className

iv) tagName

v) linkText

vi) partialLinkText

vii) cssSelector

viii) xpath
absolute - goes to root and claws all the way to element
relative -faster and shorter

---
3. WebDriver Methods:
Browser's general method:

i) get()
ii) getTitle()
iii) getCurrentUrl()
iv) getPageSource()
v) close()
vi) quit()

---
4. Browser Navigation methods:

i) navigate().To() Method:
ii) navigate().back() Method
iii) navigate().forward() Method
iv) navigate().refresh(); Method
v)driver.manage().window().maximize();

5. Methods on Elements:

i) findElement()
ii) findElements()
iii) sendKeys()
iv) Clear()
v) Click()
vi) isEnabled()
ix) getText()
x) selectByVisibleText()
xi) selectByIndex()
xii)Explicitly Wait()

6. Handle Radio Button:

Click/Select
Check displayed status
Check enabled status
Check selected status

7. When do we use findElement() ?:

is used to find the first element in the current web page matching to the specified locator value. Take a note that only first matching element would be fetched.

8. When do we use findElements() ?:

ARRAYLIST Webelements
dropdown

findElements() is used to find all the elements in the current web page matching to the specified locator value. Take a note that all the matching elements would be fetched and stored in the list of WebElements.

9. Can Selenium handle windows based pop up?:

Selenium is an automation testing tool which supports only web application testing. Therefore, windows pop up cannot be handled using Selenium.

10. How can selenium handle web-based pop up?:

WebDriver offers the users with a very efficient way to handle these pop-ups using Alert interface.

11. How to assert title of the web page?:

//verify the title of the web page
assertTrue("The title of the window is incorrect.",driver.getTitle().equals("Title of the page"));

AssertTrue is a method with two parameters, the First parameter is the error message to be printed, the second one is the boolean value of the text.

12. Can captcha be automated?:
"Completely Automated Public Turing test to tell Computers and Humans Apart," (CAPTCHA) is a type of challenge-response test used in computing to determine whether or not the user is human. The main purpose of the CAPTCHA is to prevent bots or automated programs from using various types of computing services or collecting certain types of sensitive information. In other words, it is a security feature of the application which generally prevents bots from filling.

13. What is Object Repository? How can we create Object Repository in Selenium?:

Object Repository is a term used to refer to the collection of web elements belonging to Application Under Test (AUT) along with their locator values. Thus, whenever the element is required within the script, the locator value can be populated from the Object Repository. Object Repository is used to store locators in a centralized location instead of hardcoding them within the scripts.

In Selenium, objects can be stored in an excel sheet which can be populated inside the script whenever required.

14. important test type that are applied to the web application testing?:

Functionality,database,usability,compatibility,navigation (menu, link)not non functional testing

15. The advantage of Test Automation framework:
Reusability of code
Maximum coverage
Recovery scenario
Low-cost maintenance
Minimal manual intervention
Easy Reporting
In the short time, you can cover lots of test cases

16. How do you handle errors in your test scripts ?:

Using java error handling features, java exception handle mechanism

17. Did you use reusable component in your project?:
Yes, for the log in functionality while using the use cases. Eg. Use case 1(login to the account . Change the address then logout) . Use case2(login to the account and change the phone then logout)

18. Did you find any test scenario that is not to be automated in your project using selenium?:

Yes the functionality that require more user interaction (require dynamic test data submission)eg;usability testing human interaction involved application's look and feel aspect, color, font alignment of objects

19. How do you execute multiple java program at a time?:
 Using xml testNg framework 
 more specificly i can use TestNG and add dataproviders create a multidimention array 
 and allow test to run multiple times
 this is essential for TestNG use

20. What is Selenium? Selenium is the most popular browser automation tool. There are other ways, but the best way to use Selenium is via WebDriver, a powerful API that builds on top of Selenium and makes calls to a browser to automate it, carrying out actions such as "open this web page", "move over this element on the page", "click this link", "see whether the link opens this URL", etc. This is ideal for running automated tests.

(Selenium is an open source (free) automated testing suite to test web applications. It supports different platforms and browsers. It mainly used for Functional Testing and regression testing. Selenium is a set of different software tools. Each tool has a different approach in supporting web based automation testing.Selenium is a browser automation tool, commonly used for writing end-to-end tests of web applications. A browser automation tool does exactly what you would expect: automate the control of a browser so that repetitive tasks can be automated. At a very high level, Selenium is a suite of three tools.Selenium-WebDriver makes direct calls to the browser using each browser's native support for automation. Since there are so many browsers & so many programming languages there is need for common specification which will be provided by WebDriver API. Each browser has to implement this API which is called as Remote WebDriver or Remote WebDriver Server.)

21. Components of Selenium: 
Selenium IDE (Selenium Integrated Development Environment)
Selenium RC (Selenium Remote Control)
Selenium WebDriver
Selenium Grid, parallel test execution

22. Verification point for Selenium:
To check for page title
To check for certain Text
To check for certain elements

23. Why choose 'Selenium Webdriver' for QA test automation?:
Free and open source
Have large user base and helping communities
Cross-browser compatibility
Platform compatibility
Multiple programming languages support
24. Key features of Automation Testing ?:

Key features of Automation Testing is batch testing/Batch execution --Executing the series of test cases. Without human interaction .

25. What are the types of waits available in Selenium WebDriver:
Implicit Waits - The implicit wait tells to the WebDriver to wait for certain amount of time before it throws an exception
Explicit Waits -to wait for a certain condition to occur before proceeding further in the code.
Fluent Waits -We use FluentWait commands mainly when we have web elements which sometimes visible in few seconds and sometimes take more time than usual

26. What is an XPath?:
XPath can be used to navigate through elements and attributes in an XML document.

27. What is the difference between Assert and Verify in Selenium?:
Assert: In simple words, if the assert condition is true then the program control will execute the next test step but if the condition is false, the execution will stop and further test step will not be executed. To overcome this issue we use a try-catch block.
Verify: In simple words, there won't be any halt in the test execution even though the verify condition is true or false.Mostly, the Verify command is used to check non-critical things. In such cases where we move forward even though the end result of the check value is failed.eg . if else condition

28. What is webdriver?:
The WebDriver is an API , defined by a set of interfaces to discover and manipulate DOM elements on a page, and to control the behaviour of the containing browser.
Example of interfaces get(),getTitle(),getPagesourse(),close(),Quit().

29. What are the Open-source Frameworks supported by Selenium WebDriver?
JUnit and TestNG
30.  What are the Operating Systems supported by Selenium WebDriver?
Windows, Linux,Apple:
31. What is the firefoxdriver driver property?
Geko driver
---
32. What is data driven testing ?
Data Driven Testing is a Test design and execution strategy where the test scripts read test data from data sources (file or database) such as ADO objects, ODBC sources, CSV files, etc. rather than using hard-coded values.

33. How do you conduct data driven testing?
1- Specify the file location
File src = new File(location of the file)
2- Create file inputstream object which convert file into input stream
File InputStream fis = new Fileinputstream(src)
3- Load the file
pro.load(fis)

34. What are the types of xpath?
1) Absolute XPath .
2) Relative XPath .
Absolute XPath :
It is the direct way to find the element, but the disadvantage of the absolute XPath is that if there are any changes made in the path of the element then that XPath gets failed.
The key characteristic of XPath is that it begins with the single forward slash(/) ,which means you can select the element from the root node.
Relative xpath:
For Relative Xpath the path starts from the middle of the HTML DOM structure. It starts with the double forward slash (//), which means it can search the element anywhere at the webpage.

35. What are the types of wait available in Selenium?
Implicit Waits -is applicable for the entire page. The driver will wait until the required time to make sure that all the pages are loaded, before it throws exception.
Explicit Waits -WebDriverWait is applied on a certain element with defined expected condition and time. This wait is only applied to the specified element eg. advertisement/third party pop up . This wait can also throw an exception when an element is not found.driver will check the element in every second. Polling - we can supply how many interval time
Fluent Waits - FluentWait can define the maximum amount of time to wait for a specific condition and frequency with which to check the condition before throwing an "ElementNotVisibleException" exception.

36. How to input text in the text box without calling the sendKeys()?
// To initialize js object
JavascriptExecutor JS = (JavascriptExecutor)webdriver;
// To enter username
JS.executeScript("document.getElementById(User').value='SoftwareTestingMaterial.com'");
// To enter password
JS.executeScript("document.getElementById('Pass').value='tester'");
// To initialize js object
JavascriptExecutor JS = (JavascriptExecutor)webdriver;
// To enter username
JS.executeScript("document.getElementById(User').value='SoftwareTestingMaterial.com'");
// To enter password
JS.executeScript("document.getElementById('Pass').value='tester'");

37. How to pause a test execution for 5 seconds at a specific point?
By using java.lang.Thread.sleep(long milliseconds) method we could pause the execution for a specific time. To pause 5 seconds, we need to pass parameter as 5000 (5 seconds)
Thread.sleep(5000)

38. What is the alternative to driver.get() method to open an URL using Selenium WebDriver?
Alternative method to driver.get("url") method is driver.navigate.to("url")

39. What is the difference between driver.get() and driver.navigate.to("url")?
driver.get(): To open an URL and it will wait till the whole page gets loaded
driver.navigate.get(): To navigate to an URL and It will not wait till the whole page gets loaded

40. to navigate to the next web page with reference to the browser's history
driver.navigate().forward();

41. What is the difference between driver.findElement() and driver.findElements() commands?
findElement() returns a single WebElement (found first) based on the locator passed as parameter. Whereas findElements() returns a list of WebElements, all satisfying the locator value passed.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

42. How to select a value in a dropdown?
Using Select class
Select dropdown = new Select(mySelectElement);
dropdown.selectByVisibleText(Text);
dropdown.selectByIndex(Index);
dropdown.selectByValue(Value);

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

43. How to capture Screenshot in Selenium WebDriver?:

Selenium provides an interface called TakesScreenshot which has a method getScreenShotAs which can be used to take a screenshot of the application under test.

44. How to mouse hover on a web element using WebDriver?

By using Actions class
WebElement ele = driver.findElement(By.xpath("xpath"));
//Create object 'action' of an Actions class
Actions action = new Actions(driver);
//Mouseover on an element
action.moveToElement(ele).perform();

45. How can we handle web based pop-up?

To handle alerts popups we need to do switch to the alert window and call Selenium WebDriver Alert API methods.

46. How to handle hidden elements in Selenium WebDriver?
We can handle hidden elements by using javaScript executor

47. HTTP broken link status code
200 - Valid Link
404 - Link not found
400 - Bad request
401 - Unauthorized
500 - Internal Error

48. How to read a JavaScript variable in Selenium WebDriver?
By using JavascriptExecutor

49. How do you read test data from excels?
Test data can efficiently be read from excel using JXL or POI API. POI API has many advantages than JXL. JXL API (a.k.a. Java Excel API) is the most widely used API for executing Selenium data-driven tests, which allows users to read, write, create, and modify sheets in an Excel(.xls) workbook at runtime.

50. How you build Object Repository in your project?
In QTP, there is an Object Repository concept. When a user records a test, the objects and its properties are captured by default in an Object Repository. QTP uses this Object Repository to play back the scripts. Coming to Selenium, there is no default Object Repository concept. It doesn't mean that there is no Object Repository in Selenium. Even though there is no default one still we could create our own. In Selenium, we call objects as locators (such as ID, Name, Class Name, Tag Name, Link Text, Partial Link Text, XPath, and CSS). Object repository is a collection of objects. One of the ways to create Object Repository is to place all the locators in a separate file (i.e., properties file). But the best way is to use Page Object Model. In the Page Object Model Design Pattern, each web page is represented as a class. All the objects related to a particular page of a web application are stored in a class.

51. What is page factory?
We have seen that 'Page Object Model' is a way of representing an application in a test framework. For every 'page' in the application, we create a Page Object to reference the 'page' whereas a 'Page Factory' is one way of implementing the 'Page Object Model'.

52. What is the difference between Page Object Model (POM) and Page Factory?
Page Object is a class that represents a web page and hold the functionality and members.
Page Factory is a way to initialize the web elements you want to interact with within the page object when you create an instance of it.

53. How can you use the Recovery Scenario in Selenium WebDriver?
By using "Try Catch Block" within Selenium WebDriver Java tests.

54. List some scenarios which we cannot automate using Selenium WebDriver?
1. Bitmap comparison Is not possible using Selenium WebDriver
2. Automating Captcha is not possible using Selenium WebDriver
3. We can not read bar code using Selenium WebDriver

55. What is Object Repository in Selenium WebDriver?
Object Repository is used to store element locator values in a centralized location instead of hard coding them within the scripts. We do create a property file (.properties) to store all the element locators and these property files act as an object repository in Selenium WebDriver.

56. How to connect a Database in selenium?
As we all know Selenium WebDriver is a tool to automate User Interface. We could only interact with Browser using Selenium WebDriver.

We use JDBC Driver to connect the Database in Selenium (While using Java Programming Language).

57. How To Resize Browser Window Using Selenium WebDriver?
To resize the browser window to particular dimensions, we use 'Dimension' class to resize the browser window.

58. How To Scroll Web Page Down Or UP Using Selenium WebDriver?
JavaScript scrollBy() method scrolls the document by the specified number of pixels.