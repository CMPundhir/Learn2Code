let homeworkPromise = new Promise(function (doneOnTime, notOnTime) {
	status = true
	if(status){
		doneOnTime("Home work completed successfully");
	}else{
		notOnTime("Busy in other homework...");
	}
});


homeworkPromise.then((msg)=>{
	console.log(msg);
}, (issue)=>{
	console.log(issue);
});
