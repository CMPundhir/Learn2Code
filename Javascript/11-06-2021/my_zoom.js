
class MyClass{
	constructor(name, link, datetime){
		this.name = name;
		this.link = link;
		this.datetime = datetime;
		this.status = false;
		this.cronJob(link);
	}
	calculateLeftTime(){
		var now = new Date();
		return new Date(this.datetime) - now;
	}
	toString(){
		return "Name: "+this.name+",  link: "+this.link+", Time: "+this.datetime +", status: "+this.status +", Time left: "+this.calculateLeftTime();
	}
	cronJob(link){
		setTimeout(function(){ 
			//alert(link);
			window.open(link);
			//window.open(this.link, "_blank").focus();
			this.status = true;
		}, this.calculateLeftTime());
	}
}

var classeList = [];

function onSaveClicked() {
	var cName = document.getElementById('cname').value
	var cLink = document.getElementById('c_link').value
	var cDatetime = document.getElementById('datetime').value

	if(cName === ""){
		alert("Enter class Name")
		return;
	}
	if(cLink === ""){
		alert("Enter class Link")
		return;
	}
	if(cDatetime === ""){
		alert("Enter class time")
		return;
	}
	for (var i = classeList.length - 1; i >= 0; i--) {
		var cl = classeList[i]
		if(cl.name === cName){
			alert("Class '"+cName+"' already added")
			return;
		}
	}
	var mClass = new MyClass(cName, cLink, cDatetime)

	classeList.push(mClass)
	onRefresh()
	console.log(data)
}


function onRefresh() {
	document.getElementById('myUL').innerHTML = "";
	document.getElementById('last_refresh_time').innerHTML = new Date()
	for (var i = classeList.length - 1; i >= 0; i--) {
		var data = classeList[i]
		var li = document.createElement("li");
		var t = document.createTextNode(data.toString());
		li.append(t);
		document.getElementById("myUL").appendChild(li);
	}
}

