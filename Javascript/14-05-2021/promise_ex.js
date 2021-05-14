let homeworkPromise = new Promise(function (doneOnTime, notOnTime) {
	status = true
	setTimeout(()=>{
		if(status){
			doneOnTime("Home work completed successfully");
		}else{
			notOnTime("Busy in other homework...");
		}
	}, 2000);
});



function codingClass(){
	console.log("0=>>","Class work completed.")
	console.log("0=>>","Home assigned")
	homeworkPromise.then((msg)=>{
		console.log("0=>>",msg);
	}, (issue)=>{
		console.log("0=>>",issue);
	});
	console.log("0=>>","Class Finished")
}


async function finishHWinClass(){
	console.log("1=>>","Class work completed.")
	console.log("1=>>","Home assigned")
	await homeworkPromise.then((msg)=>{
		console.log("1=>>",msg);
	}, (issue)=>{
		console.log("1=>>",issue);
	});
	console.log("1=>>","Class Finished")
}

codingClass()
finishHWinClass()


