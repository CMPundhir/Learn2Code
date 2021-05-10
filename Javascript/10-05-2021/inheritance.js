class Animal{
	// constructor(){
	// 	// i am a default constructor
	// 	console.log("Animal created")
	// }
	constructor(noLegs, noOfEyes, phyla){
		this.noLegs = noLegs;
		this.noOfEyes = noOfEyes;
		this.phyla = phyla;
		//console.log("Animal created")
	}
	describe(){
		console.log("")
	}
}

// Human inherits property of Animal
class Human extends Animal{
	static x_factor = "Intelligence" // a static varibale belongs to class only
	address = "Earth" // this varibale belongs to an object only
	constructor(name, contact){
		super(2, 2, "Vertabrates"); // always invoke super() while inheritance , super() is calling parent constructor
		this.name = name;
		this.contact = contact;
		//console.log("Human created")
	}
	intro() {
		console.log(this.address)
		console.log("My Intro =>",this.name, this.contact, this.noLegs, this.noOfEyes, this.phyla)
	}
	// static is for class only
	static faltu(){
		console.log("sona rona dhona...")
	}
}

var human1 = new Human("Pranshu Sharma", "9876543210")
human1.intro()

var human2 = new Human("Harshil Sharma", "9876543210")
human2.intro()

Human.faltu()
console.log(Human.x_factor)

/**
 every class can have 
 1. variables
 	a. static variable     -> belongs class only
 	b. non static variable -> belongs object only
 2. funcitions/ methods/ constructor
  	a. static methods      -> belongs class only
 	b. non static methods  -> belongs object only
*/




