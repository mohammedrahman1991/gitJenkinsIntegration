Java OOPS concepts explained:

Must know for all JOb applications:
source: https://www.digitalocean.com/community/tutorials/overriding-vs-overloading-in-java


 OOPs (Object-Oriented Programming System)
----------------------------------------------------------

1.object:
means a real-world entity such as a pen, chair, table, computer, watch, etc. Object-Oriented Programming is a methodology or paradigm to design a program using classes and objects. It simplifies software development and maintenance by providing some concepts:
----------------------------------------------------------

2. Collection of objects is called class. It is a logical entity.

A class can also be defined as a blueprint from which you can create an individual object. Class doesn't consume any space.
----------------------------------------------------------

3. Inheritance

When one object acquires all the properties and behaviors of a parent object, it is known as inheritance. It provides code reusability. It is used to achieve runtime polymorphism.

----------------------------------------------------------

4. Polymorphism

If one task is performed in different ways, it is known as polymorphism. For example: to convince the customer differently, to draw something, for example, shape, triangle, rectangle, etc.

In Java, we use method overloading and method overriding to achieve polymorphism.

----------------------------------------------------------

Another example can be to speak something; for example, a cat speaks meow, dog barks woof, etc.

MethodOverloading:
1. What is Overloading and Overriding?

When two or more methods in the same class have the same name but different parameters, it’s called Overloading. When the method signature (name and parameters) are the same in the superclass and the child class, it’s called Overriding.
methodoverrloading: 

2. Overriding vs Overloading

    Overriding implements Runtime Polymorphism whereas Overloading implements Compile time polymorphism.
    The method Overriding occurs between superclass and subclass. Overloading occurs between the methods in the same class.
    Overriding methods have the same signature i.e. same name and method arguments. Overloaded method names are the same but the parameters are different.
    With Overloading, the method to call is determined at the compile-time. With overriding, the method call is determined at the runtime based on the object type.
    If overriding breaks, it can cause serious issues in our program because the effect will be visible at runtime. Whereas if overloading breaks, the compile-time error will come and it’s easy to fix.


3. Overloading and Overriding Example

Here is an example of overloading and overriding in a Java program.

package com.journaldev.examples;

import java.util.Arrays;

public class Processor {

	public void process(int i, int j) {
		System.out.printf("Processing two integers:%d, %d", i, j);
	}

	public void process(int[] ints) {
		System.out.println("Adding integer array:" + Arrays.toString(ints));
	}

	public void process(Object[] objs) {
		System.out.println("Adding integer array:" + Arrays.toString(objs));
	}
}

class MathProcessor extends Processor {

	@Override
	public void process(int i, int j) {
		System.out.println("Sum of integers is " + (i + j));
	}

	@Override
	public void process(int[] ints) {
		int sum = 0;
		for (int i : ints) {
			sum += i;
		}
		System.out.println("Sum of integer array elements is " + sum);
	}

}

The process() method is overloaded in the Processor class. Then, they are overridden in the child class MathProcessor.

simple terms:

overloading LP : change in arugments of same parameter
overiding: same arguments same parameter
but actual code behind is is different
for exmaple as have a parent to child class
where child class is the logo page tests
now we try to inherit the method for find test() but it does not work for child class
thus we use @overrirde
call method test()
now we add an if statement and now code works
this override will impact this inherited class and its uses for entirity of this new child class
