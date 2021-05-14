// A callback is a function passed as an argument to another function.

var status = process.argv[2]

//console.log(status)
//var status = "BUSY" // BUSY or AVAILABLE

// callback example
function callMe(){
	console.log("Harshil's Phone Ringing...");
}

function callNow(msg, callMeBack){
	if(status === "1"){
		console.log("Harshil : "+msg+"\nPranshu: I am good, tell yours.")
	}else{
		setTimeout(callMeBack, 2000)
		console.log("busy... call your back in 2 seconds")
	}
	console.log("call finished");
}

callNow("Hey, how's you?", callMe)