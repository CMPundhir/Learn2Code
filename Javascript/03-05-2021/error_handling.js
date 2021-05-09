"use strict"
console.log("file starting")

// conosle input
// example command : node error_handling.js 12
var age = process.argv[2]


// error handling
try{
	if(isNaN(age)) throw {message: "Please enter a age in numbers", name:"InvalidAgeError"}
	//console.log(age.length())
	checkAge(age)
}catch(error){
	console.log(error.message)
}

// function to validate age else throw error
function checkAge(age) {
	console.log("checking age...")
	if(age<18){
		throw {message: "Tum abhi baccha hai.."}
	}else{
		console.log("wlecome ji")
	}
	console.log("checking age process completed")
}

// line to print to check program ended properly or not
console.log("end of file")