class Human{
	constructor(name, age){
		this.name = name;
		this.age = age;
	}
	intro(){
		console.log(`I am ${this.name}. I am ${this.age} years old`)
	}
}


let pranshu = new Human("Pranshu Sharma", 15)
let harshil = new Human("Harshil Sharma", 15)


// console.log(pranshu)
// console.log(harshil)

pranshu.intro()
harshil.intro()