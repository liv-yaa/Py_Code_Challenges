
/**
Demo for some basic JS stuff, copied from Hackerrank's 
10 days of JS demo (https://www.hackerrank.com/challenges/js10-data-types/problem?h_r=next-challenge&h_v=zen&isFullScreen=false)
- function organization
- Number Type conversions
**/

'use strict';

// Define constants 
let inputString = '';
let currentLine = 0;

class Monster {

    // Used in the for-of loop in function jsLoops
    constructor(name, home, description) {
        this.name = name;
        this.home = home;
        this.description = description;

    }
}


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

 /**JavaScript does not allow named parameters, but you can simulate named
parameters using an object:**/
function namedParamSim(opt={}) {
    const{ color, letter } = opt;

    console.log(color, letter);
}


/*
JS Loops - demo of for, while, do-while, for-in, for-of
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


function main() {
    /**
    *   main function reads input with readLine(), and calls greeting
    **/
    // const parameterVariable = readLine();

    // greeting(parameterVariable);

    // dataTypes();

    // const secondInteger = readLine();
    // const secondDecimal = readLine();
    // const secondString = readLine();
    
    // performOperation(secondInteger, secondDecimal, secondString);

    // namedParamSim({ color: 'red', letter: 'Z' });

    jsLoops(99);


}


main()

























