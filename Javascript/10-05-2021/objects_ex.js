var user1 = {
	first_name: "Pranshu",
	last_name: "Sharma"
}

console.log(user1)
user1.class = 10
console.log(user1.first_name)
console.log(user1)

class User{
	constructor(first_name, last_name){
		this.first_name = first_name;
		this.last_name = last_name;
	}
}

var user2 = new User("Harshil", "Sharma");
console.log(user2)
console.log(user2.first_name)

user2.class = 9
console.log(user2)
