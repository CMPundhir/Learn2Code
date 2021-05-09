var nums = [1,32,4,5,56,76,8]

function getSecondLargetsNum(nums) {
	nums.sort((a,b)=>b-a)
	return nums[1]
}

function getSecondSmallestNum(nums) {
	nums.sort(checkBadaChhota)
	return nums[1]
}

var sLargest = getSecondLargetsNum(nums)
var sSmallest = getSecondSmallestNum(nums)
console.log("Second Largets  =>>",sLargest)
console.log("Second Smallest =>>",sSmallest)

function checkBadaChhota(a,b){
	return a-b
}