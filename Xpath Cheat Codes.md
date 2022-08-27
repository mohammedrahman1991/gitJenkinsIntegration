How to find any xpath use these tricks

https://devhints.io/xpath#class-check

explanation: 
https://www.lambdatest.com/blog/most-exhaustive-xpath-locators-cheat-sheet/


master these :

h1:not([id]) 	//h1[not(@id)] 	?
Text match 	//button[text()="Submit"] 	?
Text match (substring) 	//button[contains(text(),"Go")] 	 
Arithmetic 	//product[@price > 2.50] 	 
Has children 	//ul[*] 	 
Has children (specific) 	//ul[li] 	 
Or logic 	//a[@name or @href] 	?
Union (joins results) 	//a | //div