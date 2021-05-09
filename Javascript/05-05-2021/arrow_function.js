var person = {
	f_name: "Prashu",
	l_name: "Sharma",
	aadhar_no: "123456789012",
	introduction: () => {
		return this.f_name + " " + this.l_name;
	}
}

console.log(person.f_name)
console.log(person.introduction())