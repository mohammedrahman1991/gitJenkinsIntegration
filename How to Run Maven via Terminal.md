How to run thru Maven command line in intelliJ with xml file 

xml files
showes 5 classes
it was failing everything


how to run from command line
mvn surefire:test -f pom.xml

so using surefire u 


<plugins>
<plugin>
   <groupId>org.apache.maven.plugins</groupId>
   <artifactId>maven-surefire-plugin</artifactId>
   <version>3.0.0-M7</version>
   <configuration>
      <includes>
         <include>**/*Test.kt</include>
      </includes>
      <suiteXmlFiles>
         <suiteXmlFile>testng.xml</suiteXmlFile>
      </suiteXmlFiles>
   </configuration>
</plugin>

pom xml is telling suite that the testing is on the tstng file
surefile plugin is reading hte xml
its realizing that its in the testng file
so it runs into testng
to run the test for me


the reason why we need test to run through command line
is because we need it to get integrated via Jenkins
and jenins can only acess the code or test scripts using terminal