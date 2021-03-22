function p1Clicked() {
	alert("Aaj kamaal hoga...\nKya Kamaal hoga...??\nAny idea??");
}
function checkDate() {
	alert(Date());
}
function letsParty() {
	let secretParty = "Gokuldhaam Society Party sharty karenge...";
	document.getElementById('p1').innerHTML = secretParty;
}
function showTable() {
	let n = parseInt(prompt("Enter a number"));
	let table = '';
	for (var i = 1; i <11; i++) {
		table += `<br> ${n} x ${i} = ${i*n}`;
	}
	document.getElementById('p2').innerHTML = table;
}