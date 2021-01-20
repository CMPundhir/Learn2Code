// alert is a function

// i am a predefiend function
alert("I am a function, Eh!");

// we can also create our own functions
function multiplication(a, b) {
	// body...
	// a function can return something or not
	return a * b;
}

let x = parseInt(prompt("Enter first number : "));
let y = parseInt(prompt("Enter second number : "));
let z = multiplication(x, y);

console.log("multiplication : "+z);


function printTable(a) {
	// body...
	for (var i = 1; i <= 10; i++) {
		console.log(a * i);
	}
}

let num = parseInt(prompt("Kon sa table nhi aata, number likho : "));
printTable(num);
