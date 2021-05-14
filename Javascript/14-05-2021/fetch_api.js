fetch("https://api.github.com/users/cmpundhir")
.then(x => x.text())
.then(y => myDisplay(y));