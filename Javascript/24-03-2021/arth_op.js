
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

function calculateArea(length, width) {
	return length * width;
}

function perimeter(length, width) {
	return 2 * (length + width);
}