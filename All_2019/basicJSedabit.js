// basicJSedabit.js
function squared(a) {
	return a**2;
}

function lessThanOrEqualToZero(num) {
	// Create a function that takes a number as its only argument and returns true if it's less than or equal to zero, otherwise return false.
	return num <= 0;
}

function dividesEvenly(a, b) {
	// Given two integers, a and b, return true if a can be divided evenly by b. Return false otherwise.
	return a % b == 0;
}

function profitableGamble(prob, prize, pay) {
	// Create a function that takes in three arguments (prob, prize, pay) and returns true if prob * prize > pay; 
	return prob * prize > pay;
}

function addition(num) {
	// Create a function that takes a number as an argument, increments the number by +1 and returns the result.
	return num + 1;
}

function animals(chickens, cows, pigs) {
	//  returns the total number of legs of all the animals.
	return chickens * 2 + cows * 4 + pigs * 4;
}

function convert(minutes) {
	// Write a function that takes an integer minutes and converts it to seconds.
	return minutes * 60;
}

function checkEquality(a, b) {
  // Numbers
	// Strings
	// Booleans (false or true)
	// Special values: undefined, null and NaN
	// What have you learnt so far that will permit you to do two different checks (value and type) with a single statement?
	// Implement a function that returns true if the parameters are equal, and false if they are different.
	return a === b;
}

function remainder(x, y) {
	return x % y;
}




