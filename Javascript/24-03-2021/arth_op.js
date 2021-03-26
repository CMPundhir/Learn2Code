
function onClickAreaBtn() {
	let length = parseInt(document.getElementById('length').value);
	let width = parseInt(document.getElementById('width').value);
	console.log("length: "+length);
	console.log("width: "+width);
	let area = calculateArea(length, width);
	console.log("area: "+area);
	alert("Area is "+area);
}

function onClickPerimeterBtn() {

}

function onClickVowelsBtn() {
	let name = document.getElementById('name').value;
	vowelsAndConsonants(name);
}

function calculateArea(length, width) {
	return length * width;
}

function perimeter(length, width) {
	return 2 * (length + width);
}

function vowelsAndConsonants(s) {
	// print all vowels in new line using console.log()
	let length = s.length; // 10
	console.log("Lenght of string: "+length);
	for (var i = 0; i<length; i++) {
		var c = s.charAt(i);
		if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
			console.log(c);
		}
	}
	for (var i = 0; i<length; i++) {
		var c = s.charAt(i);
		if(c !== 'a' && c !== 'e' && c !== 'i' && c !== 'o' && c !== 'u'){
			console.log(c);
		}
	}
}







