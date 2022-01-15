# Lab 1: Basic Elements of C++ and Java
To make a profit, a local store marks up the prices of its items by a certain percentage. 

Write a program that reads:
* the original price of the item sold, 
* the percentage of the marked-up price, and 
* the sales tax rate. 

The program then outputs:
* the original price of the item, 
* the percentage of the mark-up, 
* the store’s selling price of the item, 
* the sales tax rate, 
* the sales tax, and 
* the final price of the item. 

(The final price of the item is the selling price plus the sales tax.)

{% next %}

## Program Tasks in C++

Open `salesTax.cpp` in the editor and in the main function:

* Define the following floating-point variables:
    * originalPrice
    * markupPCT
    * taxPCT
    * sellingPrice 
    * salesTax 
    * finalPrice 

* Prompt the user to provide input for: 
    * originalPrice and read, 
    * markupPCT and read,
    * taxPCT and read.

* Calculate 
    * sellingPrice as (originalPrice * (1+markupPCT))
    * salesTax as (sellingPrice * taxPCT)
    * finalPrice as (sellingPrice + salesTax)

* Output all variables in one line (originalPrice markupPCT taxPCT sellingPrice salesTax finalPrice) separated with a space

{% next %}

### Compile and test C++ code

* To compile execute: `g++ salesTax.cpp -o salesTax` in your terminal.
* To run your program execute: `./salesTax` in your terminal.

Use the following data to check your results:
* originalPrice 100
* markupPCT 0.30
* taxPCT 0.24

The output should be:
100 0.30 0.24 130 31.2 161.2

{% next %}

## Program Tasks in Java

Open `salesTax.java` in the editor and in the main method:

* Define the following floating-point variables:
    * originalPrice
    * markupPCT
    * taxPCT
    * sellingPrice 
    * salesTax 
    * finalPrice 

* Prompt the user to provide input for: 
    * originalPrice and read, 
    * markupPCT and read,
    * taxPCT and read.

* Calculate 
    * sellingPrice as (originalPrice * (1+markupPCT))
    * salesTax as (sellingPrice * taxPCT)
    * finalPrice as (sellingPrice + salesTax)

* Output all variables in one line (originalPrice markupPCT taxPCT sellingPrice salesTax finalPrice) separated with a space

{% next %}

### Compile and test Java code

* To compile execute: `javac salesTax` in your terminal.
* To run your program execute: `java salesTax` in your terminal.

Use the following data to check your results:
* originalPrice 100
* markupPCT 0.30
* taxPCT 0.24

The output should be:
100.0 0.30 0.24 130.0 31.2 161.2

{% next %}

## SUBMIT YOUR WORK

Make sure that we finished and tested:

- [x] salesTax.cpp
- [x] salesTax.java
- [x] and you have compile and tested your code :tada:

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token


```
submit50 mkotsovoulou/itc2197sp22/main/labs/salesTax
```


@github/mkotsovoulou Do you have any questions?