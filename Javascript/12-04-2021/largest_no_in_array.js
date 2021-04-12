console.log("Hello node");

let arr = [2, 3, 6, 6, 5];
console.log(arr);

let largestNo = -762783263862863;
let secondLargestNo = largestNo;
for (var i = arr.length - 1; i >= 0; i--) {
	if(largestNo < arr[i]){
		secondLargestNo = largestNo;
		largestNo = arr[i];
	}
}

console.log(largestNo);
console.log(secondLargestNo);
