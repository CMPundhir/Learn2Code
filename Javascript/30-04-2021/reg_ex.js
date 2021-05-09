var para = "Hello everyone i am chander mohan pundhir"

var result = para.search("chander") // string search method

console.log(result)

result = para.replace("chander", "ChandeR") // string replace method

console.log(result)

result = para.replace("Chander", "ChandeR") // string replace method

console.log(result)

var pattern = /Chander/i;

result = para.replace(pattern, "ChandeR") // string replace method

console.log(result)

var para2 = "My phone number is 9392812345, my eamil address is abc@gmail.com"

var pattern2 = /[0-9]{10}/g

result = para2.match(pattern2)

console.log(result)

// result.forEach((e)=>{
// 	console.log(e)
// });

const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

const my_email1 = "abc@gmail.com"
const my_email2 = "abc@gmail.c"
const my_email3 = "abcgmail.com"
// email validation with reg ex
const r1 = re.test(my_email1)
const r2 = re.test(my_email2)
const r3 = re.test(my_email3)

console.log(my_email1, r1)
console.log(my_email2, r2)
console.log(my_email3, r3)

// unicode to print a special character
const account_balce = "₹ 100"

console.log(account_balce)

result = account_balce.search(/[\u20b9]/g)

console.log(result)

result = account_balce.match(/[\u20b9]/g)

console.log(result)

result = account_balce.replace(/[\u20b9]/g, "$")

console.log(result)






