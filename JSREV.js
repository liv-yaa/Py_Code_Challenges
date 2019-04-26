
/**
Demo for some basic JS stuff, copied from Hackerrank's 
10 days of JS demo (https://www.hackerrank.com/domains/tutorials/10-days-of-javascript)

**/

'use strict';

// Define constants 
let inputString = '';
let currentLine = 0;


/* Simple JS class */
class Monster {

    // Used in the for-of loop in function jsLoops
    constructor(name, home, description) {
        this.name = name;
        this.home = home;
        this.description = description;

    }
}

/* Warm Up 
JS Basics Day ): https://www.hackerrank.com/challenges/js10-hello-world/topics/javascript-basics
*/
function readLine() {
    /**
    *   helper function reads input (not totally working)
    **/
    return inputString[currentLine++];

}


function greeting(parameterVariable) {
    /** 
    *   A line of code that prints "Hello, World!" on a new line is provided in the editor. 
    *   Write a second line of code that prints the contents of 'parameterVariable' on a new line.
    *   parameterVariable - A string of text.
    **/
    
    console.log('Hello, world');
    console.log(parameterVariable);

}

/* 
DataTypes demo
https://www.hackerrank.com/challenges/js10-data-types/topics/javascript-data-types
*/
function dataTypes() {
    /* 
    Demo for all 7 JS datatypes 
    */

    // Number
    var var1 = 1.5e5;
    
    // String
    var var2 = 'Hello';
    
    // Boolean 
    var var3 = true;
    
    // Symbol 
    var var4 = Symbol('some Symbol variable');
    
    // Null Object
    var var5 = null;
    
    // Undefined
    var var6;
    
    // Object
    var var7 = {a: 1, b: 2};
    
    // Not a number NaN
    var var8 = Math.sqrt(-1);



    console.log(var1 + " is a " + typeof var1);
    console.log(var2 + " is a " + typeof var2);
    console.log(var3 + " is a " + typeof var3);
    console.log(var4.toString() + " is a " + typeof var4);
    console.log(var5 + " is an " + typeof var5);
    console.log(var6 + " is an " + typeof var6);
    console.log(var7 + " is an " + typeof var7);
    console.log(var8 + " is a " + typeof var8);

    /*  150000 is a number
        Hello is a string
        true is a boolean
        Symbol(some Symbol variable) is a symbol
        null is an object
        undefined is an undefined
        [object Object] is an object
        NaN is a number
    */

}

/* 
Day1: Arithmetic operators
https://www.hackerrank.com/challenges/js10-arithmetic-operators/topics/javascript-arithmetic-operators
DataTypes Conversion
*/
function performOperation(secondInteger, secondDecimal, secondString) {
    // https://www.hackerrank.com/challenges/js10-data-types/problem?h_r=next-challenge&h_v=zen&isFullScreen=true
    // Declare a variable named 'firstInteger' and initialize with integer value 4.
    const firstInteger = 4;
    
    // Declare a variable named 'firstDecimal' and initialize with floating-point value 4.0.
    const firstDecimal = 4.0;
    
    // Declare a variable named 'firstString' and initialize with the string "HackerRank".
    const firstString = 'HackerRank ';
    
    // Write code that uses console.log to print the sum of the 'firstInteger' and 'secondInteger' (converted to a Number        type) on a new line.
    console.log(firstInteger + Number(secondInteger));
    
    
    // Write code that uses console.log to print the sum of 'firstDecimal' and 'secondDecimal' (converted to a Number            type) on a new line.
    console.log(Number(firstDecimal) + Number(secondDecimal));
    
    
    // Write code that uses console.log to print the concatenation of 'firstString' and 'secondString' on a new line. The        variable 'firstString' must be printed first.
    console.log(firstString + secondString);

}

/*  Calculate the area of a rectangle. */
function getArea(length, width) {
    let area;
    // Write your code here

    area = length * width;
    
    return area;
}

/* Calculate the perimeter of a rectangle. */
function getPerimeter(length, width) {
    let perimeter;
    // Write your code here

    perimeter = (2 * length) + (2 * width);
    
    return perimeter;
}

/* Day1: Functions https://www.hackerrank.com/challenges/js10-function/topics/javascript-function */
function recursiveFactorial(n) {
    /**
    *   Defines a named recursive function referenced by the fib variable. 
    *   @param {Number} n
    *   @returns {Number} The value of fibonacci(n).         
    **/
    var fib = function fibonacci(n){
        if (n > 2) {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
        else if (n < 1) {
            return 0;
        }
        // else, return 1
        return 1;
    }
    return fib;
}





/* Non-Identity or Strict Inequality (!==)
*/
function nonIdentity() {
    console.log(1 !== 1); // False
    console.log(1 !== "1"); // True
    console.log('1' !== 1); // True
    console.log(0 !== false); //True
    console.log(0 !== null); // True
    console.log(0 !== undefined); // True
    console.log(null !== undefined); // True

    // These evaluate to False: and are 'falsy'
    // false
    // undefined
    // null
    // 0
    // NaN
    // "" (i.e., the empty string)
}

/* Switch conditional */
function switchConditional() {
    // switch (expression) {
    // case label1:
    //     statement1;
    //     break;
    // case label2:
    //     statement2;
    //     break;
    // case label3:
    //     statement3;
    //     statement4;
    //     break;
    // default:
    //     statement;

}


/**JavaScript does not allow named parameters, but you can simulate named
parameters using an object:**/
function namedParamSim(opt={}) {
    const{ color, letter } = opt;

    console.log(color, letter);
}


/*
JS Loops - demo of for, while, do-while, for-in, for-of
https://www.hackerrank.com/challenges/js10-loops/topics/javascript-loops
*/
function jsLoops(input) {
    let actress = {
        firstName: "Julia",
        lastName: "Roberts",
        dateOfBirth: "October 28, 1967",
        nationality: "American",
        firstMovie: "Satisfaction"
    };

    let actressMap = new Map([
        ["firstName", "Julia"],
        ["lastName", "Roberts"],
        ["dateOfBirth", "October 28, 1967"],
        ["nationality", "American"],
        ["firstMovie", "Satisfaction"]
    ]);
    
    // for (initialization; condition; finalExpression) { ... }
    for (let i=0; i < input; i += 1) {
        process.stdout.write(i + " ");
    }

    let j = 8;
    for (; j > 0; j -= 1) {
        process.stdout.write(j + " ");
    }

    // Infinite for loop with a break
    let k = 0;
    for (;;) {
        if (k > input) {
            break;
        }
        process.stdout.write(k + " ");
        k ++;
    }

    // while
    let x = input;
    while (x===input) {
        console.log(x);
        x ++;

        if (x != input) {
            break;
        }
    }

    // do...while
    var y = 1;

    do {
        process.stdout.write(y + " ");

        y ++;
    } while (y <= input);
    console.log();

    // for-in
    for (var property in actress) {
        console.log('actress.' + property + " = " + actress[property]);

    }

    // for-in with a Monster object:
    var monster = new Monster('Fred', 'Canada', 'Frightening');

    // This representation is an array
    console.log(monster);

    // Use a for-in loop to print each element on a new line:
    for (let property in monster) {
        console.log(property + ": " + monster[property]);
    }

    // Creat an array (an interable)
    var array = [1, 2, 3, 4, 4];
    console.log(array);

    // for-of  for (let variable of iterable)
    for (let int of array) {
        console.log(int);
    }

    // for-of  to iterate over the Map {k:[v, v], k: [v, v], ...}
    for (let info of actressMap) {
        console.log(info);
    }

    // Use indexing to access values in the map
    for (let info of actressMap) {
        console.log(info[0] + ": " + info[1]);
    }

}

/* Passed - factorial for loop 
https://www.hackerrank.com/challenges/js10-function/problem?isFullScreen=true
*/
function factorial(n) {
    let f = 1;

    for (let i=1; i <= n; i += 1) {
        process.stdout.write(i + " ");
        f *= i;
    }
    return f;
}

/* Day1: declaration of variables (let, const, var) 
https://www.hackerrank.com/challenges/js10-let-and-const/topics/javascript-let-const-var

const : to create a read-only reference to a value, meaning the value referenced
 by this variable cannot be reassigned. Because the value referenced by a 
 constant variable cannot be reassigned, JavaScript requires that constant 
 variables always be initialized.

let : We use the let keyword to declare variables that are limited in scope to 
the block, statement, or expression in which they are used. This is unlike the 
var keyword, which defines a variable globally or locally to an entire function 
regardless of block scope.


*/
function letConst(input) {
    let a = input;

    // This will throw "SyntaxError: Identifier 'a' has already been declared"
    let a = input + 1;

    console.log(a); 
}

/* Demo - Const demo 
https://www.hackerrank.com/challenges/js10-let-and-const/problem?isFullScreen=true
*/
function constDemo(r) {

    const PI = Math.PI;
    // const r = readLine();
    
    // Print the area, perimeter of the circle:
    console.log(r ** 2 * PI);
    console.log(2 * PI * r);

    try {    
        // Attempt to redefine the value of constant variable PI
        PI = 0;
        // Attempt to print the value of PI
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}

/* Passed - Complete the getGrade(score) function in the editor. It has one parameter: an integer, , denoting the number of points Julia earned on an exam. It must return the letter corresponding to her  according to the following rules...
https://www.hackerrank.com/challenges/js10-if-else/problem?isFullScreen=true
*/
function getGrade(score) {
    let grade;
    // Write your code here

    
    return grade;
}

/* Passed - Complete the getGrade(score) function in the editor. It has one 
parameter: an integer, score, denoting the number of points Julia earned on an exam. 
It must return the letter corresponding to her  according to the following rules...
https://www.hackerrank.com/challenges/js10-if-else/problem?isFullScreen=true
*/
function getGrade(score) {
    let grade;
    if (25 < score && score <= 30) {
        grade = 'A';
    } else if (20 < score && score <= 25) {
        grade = 'B';
    } else if (15 < score && score <= 20) {
        grade = 'C';
    } else if (10 < score && score <= 15) {
        grade = 'D';
    } else if (5 < score && score <= 10) {
        grade = 'E';
    } else  {
        grade = 'F';
    } 
    
    return grade;
}


/* Demo - Arrays Methods Day 3
https://www.hackerrank.com/challenges/js10-arrays/topics/javascript-arrays
The JavaScript Array object:
- a global object used in the construction of arrays; which are high-level, 
- list-like objects.
- has attributes a.length (because it is an object)

*/
function array() {
    // Create
    var a = ['a', 'r', 'r', 'a', 'y']; // create Array object
    console.log(a); // attribute 
    console.log(a.length); // attribute - not a function

    // Same as Python?
    console.log(a[0]);
    console.log(a[a.length - 1]); 

    // Loop over array using forEach() function inside - how does this work???
    a.forEach(function(e, i, array) {
        // 'i' is index
        // 'e' is element
        console.log(i + ' ' + e);
    });

    // Append 'third' to array 'a'
    a.push('third');
    console.log(a);

    // Remove the last element from the array and save it 
    let rem1 = a.pop();
    console.log(a);
    console.log(rem1);

    // Remove the first element from the array
    let rem2 = a.shift();
    console.log(a);
    console.log(rem2);

    // Insert element at the beginning of the array
    a.unshift('xxx');
    console.log(a);

    //  Find the Index of an Item in the Array
    let position = a.indexOf('xxx');
    console.log(position);

    // Remove an Item by Index Position
    a.splice(1, 2) // position=1, elements to remove=2
    console.log(a);

    // Copy an array
    let b = a.slice();
    console.log(b);

    // Sort in ascending lexicographical order using a built-in
    var c = ['c', 'a', 'd', 'b', 'aa'];
    var d = [9, 2, 13, 7, 1, 12, 123];
    c.sort();
    d.sort()
    console.log(c);
    console.log(d);

    // Iterate over an array
    for (let e of c) {
        console.log(e);

    }

}

/* Passed - https://www.hackerrank.com/challenges/js10-arrays/problem
 */
function getSecondLargest() {

}


/* Passed - https://www.hackerrank.com/challenges/js10-loops/problem?h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&isFullScreen=true
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vows = [ 'a', 'e', 'i', 'o', 'u' ];

    for (let letter of s) {

        if (vows.indexOf(letter) != -1) { 
            console.log(letter);
        }

    }
    for (let letter of s) {

        if (vows.indexOf(letter) === -1) {
            console.log(letter);
        }

    }
}

/* Better - Loops only once! found on discussions
 */
function vowelsAndConsonants2(s) {
    let vows = 'aeiou';
    let cons = '';

    for (let i = 0; i < s.length; i += 1) {
        if (vows.includes(s[i])) {
            console.log(s[i]);

        }
        else {
            cons += s[i] + '\n';
        }

    }

    console.log(cons.trim());

}

/*
https://www.hackerrank.com/challenges/js10-regexp-1/topics/javascript-regex
A regular expression literal is a RegEx pattern encosed within forward slashes:
const re = /ab+c/;
*/
function regEx() {

}



function main() {
    /**
    *   main function reads input with readLine(), and calls greeting
    **/

    getSecondLargest();

    // array()

    // console.log(getGrade(44));
    // console.log(getGrade(4));
    // console.log(getGrade(14));
    // console.log(getGrade(28));
    
    // constDemo(8);

    // console.log(factorial(5));


    // const parameterVariable = readLine();

    // greeting(parameterVariable);

    // dataTypes();

    // const secondInteger = readLine();
    // const secondDecimal = readLine();
    // const secondString = readLine();
    
    // performOperation(secondInteger, secondDecimal, secondString);

    // namedParamSim({ color: 'red', letter: 'Z' });

    // jsLoops(99);

    // vowelsAndConsonants2('sotlkjeidcksldkgtyroekf');

    // console.log(recursiveFactorial(4));

    // let n = 9;
    // let fib = function fibonacci(n){
    //     if (n > 2) {
    //         return fibonacci(n - 1) + fibonacci(n - 2);
    //     }
    //     else if (n < 1) {
    //         return 0;
    //     }
    //     // else, return 1
    //     return 1;
    // }
    // console.log(fib);



}



main()

























