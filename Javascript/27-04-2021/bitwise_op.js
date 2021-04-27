let a = 35
let b = 57
let c = a & b
let d = a | b
let e = a ^ b
let f = ~ a
let g = a >> 2 // 100011 >> 2  = 1000
let h = a << 2 // 100011 << 2  = 10001100
let i = a >>> 2 // 100011 >> 2  = 1000
let j = f >>> 2 // 

console.log(Number(a).toString(2), a);
console.log(Number(b).toString(2), b);
console.log(Number(c).toString(2), c);
console.log(Number(d).toString(2), d);
console.log(Number(e).toString(2), e);
console.log(Number(f).toString(2), f); // MSB for positive=0, for negative=1
console.log(Number(g).toString(2), g);
console.log(Number(h).toString(2), h);
console.log(Number(i).toString(2), i);
console.log(Number(j).toString(2), j);

//16 8 4 2 1

//"1.5"
// function dec2bin(dec) {
//   return (dec >>> 0).toString(2);
// }

// bitwise & 
// 101
// 100
// ___
// 100

// 100001
// 111001
// ------
// 111001 		


// 64 bit
// 000000000000000000000000000000000000000000000000000000000000100011

// boolean 1 bit
// 0 / 1
