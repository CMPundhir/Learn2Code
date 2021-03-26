function factorial(n) {
	// 5!
	// 5 x 4!
	// 5 x 4 x 3!
	// 5 x 4 x 3 x 2!
	// 5 x 4 x 3 x 2 x 1 
	// 120
	let temp = n;
	let fact = 1;
	while(temp>0){
		fact *= temp;
		temp--;
	}
	return fact;
}


// recursion
function factorialRec(n) {
	if(n==1){
		return 1;
	}
	return n * factorialRec(n-1);
}


function onClickNum() {
	let n = parseInt(document.getElementById('num').value);
	let res = factorialRec(n);
	document.getElementById('res_p').innerHTML = `Factorial of ${n} is ${res}`;
}