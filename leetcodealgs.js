// // var longestPalindrome = function(s) {
// //     if (!s) {
// //         return "";
// //     }

// //     function expandAroundCenter(s, left, right) {
// //         while (left >= 0 && right < s.length && s[left] === s[right]) {
// //             left--;
// //             right++;
// //         }
// //         return right - left - 1;
// //     }

// //     let start = 0;
// //     let end = 0;

// //     for (let i = 0; i < s.length; i++) {
// //         const odd = expandAroundCenter(s, i, i);
// //         const even = expandAroundCenter(s, i, i + 1);
// //         const max_len = Math.max(odd, even);

// //         if (max_len > end - start) {
// //             start = i - Math.floor((max_len - 1) / 2);
// //             end = i + Math.floor(max_len / 2);
// //         }
// //     }

// //     return s.substring(start, end + 1);    
// // };
// // console.log(longestPalindrome('argentinamanitnegra'))
// var longestCommonPrefix = function(strs) {
//     let pref = strs[0];
//     let prefLen = pref.length;

//     for (let i = 1; i < strs.length; i++) {
//         let s = strs[i];
//         while (pref !== s.substring(0, prefLen)) {
//             prefLen--;
//             if (prefLen === 0) {
//                 return "";
//             }
//             pref = pref.substring(0, prefLen);
//         }
//     }

//     return pref;    
// };
// выучил я эту задачу на leetcode постоянно там практикуюсь 
//постараюсь выполнить как можно больше задач и решать их максимально продуктивно для меня 
// let array = [1,2,3,45,2,3,234,1]

// const quickSort =(array)=>{
//     let clonedArr =[...array];
//     if(clonedArr.length<=1){ 
//         return clonedArr;
//     }
//     let pivot = array[0]
//     let left = []
//     let right = []

//     for(let i =1; i<clonedArr.length; i++){
//         if(clonedArr[i] <pivot){
//             left.push(clonedArr[i])
//         }else{
//             right.push(clonedArr[i])
//         }
        
//     }
//     // return [...left pivot ...right]
// }
// console.log(quickSort(array))
let array = [4,34,623,65,-10, 52]

const quickSort = (arr) => {
  let clonedArr = [...arr];
  
  if(clonedArr.length <= 1) {
    return clonedArr;
  }
  
  let pivot = arr[0];
  let leftArr = [];
  let rightArr = [];
  
  for(let i=1; i<clonedArr.length; i++) {
    if(clonedArr[i] < pivot) {
      leftArr.push(clonedArr[i])
    } else {
      rightArr.push(clonedArr[i])
    }
  }
  
  return [...quickSort(leftArr), pivot, ...quickSort(rightArr)]
}

quickSort(array);
