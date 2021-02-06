alert("Hey")
let i = parseInt(prompt("Enter a number")) // 6
document.getElementById('p1').innerHTML = ++i; // pre increment 7
document.getElementById('p2').innerHTML = i++; // post increment 7(8)
document.getElementById('p3').innerHTML = i--; // post decrement 8(7)
document.getElementById('p4').innerHTML = --i; // pre decrement 6