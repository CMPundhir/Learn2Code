console.log("Hello node");

let arr = [2, 3, 6, 6, 5];
console.log(arr);

let largestNo = 0;
let secondLargestNo = 0;

for (var i = arr.length - 1; i >= 0; i--) {
	if(largestNo < arr[i]){
		secondLargestNo = largestNo;
		largestNo = arr[i];
	}
}

console.log(largestNo);
console.log(secondLargestNo);
