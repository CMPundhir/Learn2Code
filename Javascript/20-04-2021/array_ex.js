var cars = ["alto","s3","volvo","q3"]
// 				0    1     2      3
console.log(cars)

console.log(cars[2])

var pocket = ["phone", "pen", "keys", 20]
console.log(pocket)

console.log(typeof pocket)

console.log(pocket.length) // length is a property

console.log(cars.sort())


// looping through an array
for (var i = cars.length - 1; i >= 0; i--) {
	if(cars[i] == "alto"){
		console.log("We have a maruti")
	}
	console.log(cars[i])
}


