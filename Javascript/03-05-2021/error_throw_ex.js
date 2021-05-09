
console.log("file starting")

// conosle input
// example command : node error_handling.js 12
var age = process.argv[2]

if(age<18){
	throw {error: "Tum abhi baccha hai.."}
}else{
	console.log("wlecome ji")
}

console.log("end of file")