'use strict';
var lengthOfLongestSubstring = function(s) {
    let ans= 0;
    let set=new Set();
    for (let i=0;i < s.length; i++) {
        if (set.has(s[i])) {
            set=new Set();
            set.add(s[i]);
        }else {
            set.add(s[i]);
        };
    };
    return Array.from(set).join().replace(/,/g,'').length;
    
};

console.log(lengthOfLongestSubstring('abafgd'));

var lengthOfLongestSubstring_2 = function(s) {
    let ans= 0;
    let set=new Set();
    for (let i=0;i < s.length; i++) {
        if (set.has(s[i])) {
            return lengthOfLongestSubstring_2(s.slice(i,));
        }else {
            set.add(s[i]);
        };
    };
    return Array.from(set).join().replace(/,/g,'').length;
    
};
console.log(lengthOfLongestSubstring_2('aaafagd'));

var lengthOfLongestSubstring_3 = function(s) {
    let ans= 0;
    let arr=new Array();
    for (let i=0;i < s.length; i++) {
        if (arr.includes(s[i])) {
            let val=arr.slice().reverse().indexOf(s[i]);
            return lengthOfLongestSubstring_3(s.slice(i-val,));
        }else {
            arr.push(s[i]);
        };
    };
    return arr.join().replace(/,/g,'').length;
    
};

console.log(lengthOfLongestSubstring_3('aaafagd'));