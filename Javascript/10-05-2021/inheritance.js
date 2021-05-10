/*
 Inheritance
 1. a class can inherit another class. 
 2. it means it can take inherit varibales and method of parent class
 3. The class which inherit another class is called child/ subclass
 4. Inerited class is called Parent / Super class
*/

/**
 every class can have 
 1. variables
 	a. static variable     -> belongs class only
 	b. non static variable -> belongs object only
 2. funcitions/ methods/ constructor
  	a. static methods      -> belongs class only
 	b. non static methods  -> belongs object only
*/

class Animal{
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

Human.faltu() // faltu() is static so can be accessed via ClassName.methodName()
console.log(Human.x_factor) // x_factor is also static and can be accessed by class only





