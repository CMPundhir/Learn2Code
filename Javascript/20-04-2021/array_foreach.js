var marks = [75, 68, 68, 78, 79]

marks.forEach(calculateGrade);

function calculateGrade(marks) {
	let grade;
	if(marks>75){
		grade = "A"
	}else if(marks>70){
		grade = "B"
	}else if(marks>65){
		grade = "C"
	}else {
		grade = "D"
	}
	console.log(`${marks} : ${grade}`);
}

console.log("Adding computer marks in array");
marks.push(71)

for (var i = marks.length - 1; i >= 0; i--) {
	let mark = marks[i]
	calculateGrade(mark)
}


// calculate average
var avg = 0
for (var i = marks.length - 1; i >= 0; i--) {
	avg += marks[i]
}
avg /= marks.length
console.log(avg)




