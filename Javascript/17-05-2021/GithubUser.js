function addUser(user) {
	var li = document.createElement("li");
	var img = document.createElement('img');
	var div = document.createElement('div');
	var txt = document.createTextNode(user.login);

	img.src = user.avatar_url;

	div.appendChild(img);
	div.appendChild(txt);
	li.appendChild(div);
	document.getElementById("myUL").appendChild(li);
}

const getGihubUsers = async () => {
	const url = "https://api.github.com/users";
	
	fetch(url)
		.then(response => // promise
			response.json() // further json promise
			.then(data => ({ //
				data: data,
				status: response.status
			})).then(res => {
				console.log(res.status, res.data)
				const users = res.data;
				for(var i=0; i<users.length; i++){
					addUser(users[i]);
				}
			})
		);
}

getGihubUsers();