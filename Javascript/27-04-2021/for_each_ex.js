var list = [1,2,3,44,6,7,8]

//list.forEach(eval);

// function eval(e, index) {
// 	// body...
// 	console.log(index, e)
// }

for (var i = 0; i <list.length; i++) {
	if(list[i] >40){
		break; // stops further execution of a loop
	}
	console.log(list[i])
}

console.log("-------********---------")

for (var i = 0; i <list.length; i++) {
	if(list[i] >40){
		continue; // move to next step of execution of a loop
	}
	console.log(list[i])
}