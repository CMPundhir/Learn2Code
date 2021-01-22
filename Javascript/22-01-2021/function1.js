// what is function?
// A function is a code snippet that can be called by other code or by itself, or a variable that refers to the function

// Different types of functions
// 1. An anonymous function is a function without a function name. Only function expressions can be anonymous, function declarations must have a name:
// 2. A named function is a function with a function name.
// 3. An inner function is a function inside another function (square in this case).
// 4. An outer function is a function containing a function (addSquares in this case).
// 5. A recursive function is a function that calls itself.
// 6. An Immediately Invoked Function Expressions (IIFE) is a function that is called directly after the function is loaded into the browser’s compiler.


// Functions on the basis of parameter
// 1. Parameterized function
// 2. Non Parameterized function


// Functions on the basis of return type
// 1. Return something
// 2. Return nothing / no return


// anonymous function
(function () {
	// body...
	console.log("I am anonymous function.");
})

// how we can use it??????
const sum = (function(a,b){return a+b});
console.log(sum(10,12));

setTimeout(function () {
    console.log('Execute later after 1 second')
}, 10000); // 1000 ms = 1 sec


// named function
function function1() {
	console.log("I am without parameter function.");
}

function1(); // function call


// parameterized function
function function2(parameter) {
	console.log("I am with parameter function and value of parameter is "+parameter);
}

function2("CMPundhir"); // function call

// another parameterized function
function function3(parameter1, parameter2) {
	console.log("I am 2 parameter function and here are the values of both parameters are \n");
}

function3("Harshil", "Pranshu"); // function call

// function with return type
function square(argument) {
	return argument * argument;
}

const squareOf4 = square(4); // function call to return a value
console.log("square Of 4 : "+squareOf4);

// 
function outerFunction(){
	console.log("I am outerFunction hahahahahah...");
	function innerFunction() {
		console.log("I am innerFunction hihihihihihi...");
	}
	innerFunction(); // we call an inner function only inside its outer function/ current function
}

outerFunction(); 

// 1! = 1; 
// 2! = 2 x 1! = 2
// 3! = 3 x 2! = 6
// 4! = 4 x 3! = 24
// 5! = 5 x 4! = 120

// very important concept
// recursive function
function factorial(num) {
	// always add a base case to terminate recursion
	if(num===1){
		return 1; // 1! = 1;
	}
	return num * factorial(num-1);	
}

const factorialOf5 = factorial(13);
console.log(factorialOf5);




