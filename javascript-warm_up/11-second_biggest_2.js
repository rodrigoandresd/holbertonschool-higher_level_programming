const array = [1, 2, 78, 456, 5, 6, 7];
const orded = array.sort((a, b) => a - b);
const secondBiggest = orded.slice(-2,-1)
console.log(array);
console.log(orded);
console.log(secondBiggest);
