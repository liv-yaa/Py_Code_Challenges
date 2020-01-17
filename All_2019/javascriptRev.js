// reviewing javascript
'use strict';


// const x = 8

// if (x > 8) {
//     console.log('too much');
// } else if (x < 8) {
//     console.log('too little');
// } else {
//     console.log('Cool');
// }



process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   A line of code that prints "Hello, World!" on a new line is provided in the editor. 
*   Write a second line of code that prints the contents of 'parameterVariable' on a new line.
*
*   Parameter:
*   parameterVariable - A string of text.
**/
function greeting(parameterVariable) {
    // This line prints 'Hello, World!' to the console:
    console.log('Hello, World!');

    // Write a line of code that prints parameterVariable to stdout using console.log:
    
}


function main() {
    const parameterVariable = readLine();
    
    greeting(parameterVariable);
}






// Number Data Type:
var firstVar = 1.5e5; 

// String Data Type:
var secondVar = 'Hello'; 

// Boolean Data Type:
var thirdVar = true; 

// Symbol Data Type:
var fourthVar = Symbol("some Symbol variable"); 

// Null Object:
var fifthVar = null; 

// Undefined Data Type:
var sixthVar; 

// Object:
var seventhVar = {a: 1, b: 2}; 

// NaN (It is a Number):
var eighthVar = Math.sqrt(-1); 

console.log(firstVar + " is a " + typeof firstVar);
console.log(secondVar + " is a " + typeof secondVar);
console.log(thirdVar + " is a " + typeof thirdVar);
console.log(fourthVar.toString() + " is a " + typeof fourthVar);
console.log(fifthVar + " is an " + typeof fifthVar);
console.log(sixthVar + " is an " + typeof sixthVar);
console.log(seventhVar + " is an " + typeof seventhVar);
console.log(eighthVar + " is a " + typeof eighthVar);




var actress = {
    firstName: "Julia",
    lastName: "Roberts",
    dateOfBirth: "October 28, 1967",
    nationality: "American",
    firstMovie: "Satisfaction"
};

for (var property in actress) {
    console.log("actress." + property + " = " + actress[property]);
}


function main(input) {
    var i = 1;

    do {
        process.stdout.write(i + " ");

        i++;
    } while (i <= input);
}


for (var property in actress) {
    console.log("actress." + property + " = " + actress[property]);
}

// Objects!
class Monster {
    constructor(name, home, description) {
        this.name = name;
        this.home = home;
        this.description = description;
    }
}

function main(input) {
    var monster = new Monster(input[0], input[1], input[2]);

    // Print array
    console.log(monster);

    // Print each of its elements on a new line
    for (let property in monster) {
        console.log(property + ": " + monster[property]);
    }
}

// Split the words read as input into an array of words
var array = input.split(new RegExp("[ \n]+"));

// Print each Key-Value pair in the map
for (let info of actress) {
    console.log(info);
}

// Print each Key and Value as "Key: Value"
console.log();
for (let info of actress) {
    console.log(info[0] + ": " + info[1]);
}

// Loop only once
function vowelsAndConsonants(s) {
    const vowels = 'aeiou';
    var consonants = '';
    
    for(var i = 0; i < s.length; i++) {
       if (vowels.includes(s[i])) {
           console.log(s[i]);
       }
       else {
           consonants += s[i] + '\n';
       }
    }
    
    console.log(consonants.trim());
}

















