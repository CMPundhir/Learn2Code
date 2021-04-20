var name = "CM"

console.log(name)

console.log(typeof name)

var car1 = {
	color: "black",
	name: "jaguar",
	price: 5000000,
	startEngine: function () {
		console.log("brrruuuuuuuhhhhhhh... engine running...")
	}
}


console.log(car1)

console.log(car1.color)


var car2 = {
	color: 'white',
	name: 'nano',
	price: 150000,
	startEngine: function () {
		console.log(`${this.name} is starting....`)
		console.log("tuk tuk...")
	}
}


console.log(car2)

console.log(typeof car2)

car1.startEngine()
car2.startEngine()

