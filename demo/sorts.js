"use strict";
const readline = require("readline");
const rl = readline.createInterface({
	input : process.stdin,
	output : process.stdout,
});

rl.close();
let set=new fib ();

function rej (w) {
	console.log(w)
} 



var question = function(q) {
	return new Promise ((res, rej) => {
	rl.question(q,answer => {
		res(answer);
		});
	});	
};

(async function main() {
	var answer ;
	while (answer !="close") {
	answer = await question("enter fibonacci term");
	if (answer != "close") {
	console.log(set.term(answer)); }
	};
	console.log('finally you are sure!');
	rl.close();

});





function fib () {
	this.arr=Array(0,1);
	this.term = function (n) {
	if (n<this.arr.length) {
		return this.arr[n] ;
	} else  {
	tmp = this.term(n-1) + this.term(n-2);
	this.arr[n]=tmp;
	return tmp;
		}
	};
};


function sort_(arr) {
	let i = 1 ;
	let y=0;
	while (i<arr.length){
		let j=i-1;
		let a= i;
		while(j>=0 && arr[a]<arr[j]) {
			let tmp=arr[j];
			arr[j]=arr[a];
			arr[a]=tmp;
			j=j-1;
			a=a-1;
			y=y+1;			
		};
		i=i+1;
		}; 
	console.log(y);
	return arr;
}; 

let vi = [21,17,16,2,3,9,10,11,2,6,7,1,3,5,4,7];
console.log(sort_(vi));

function Bsort(arr) {
	let y=0;
	for(let j=0;j<arr.length;j++ ) {
		for(let i=j+1;i<arr.length;i++) {
			if (arr[i]<arr[j]) {
				let tmp=arr[j];
				arr[j]=arr[i];
				arr[i]=tmp;
			};
			y=y+1;
		};
	};
	console.log(y);
	return arr;
};

 vi = [21,17,16,2,3,9,10,11,2,6,7,1,3,5,4,7];
console.log(Bsort(vi));

function MergeSort(arr,n) {
	if (arr.length==1) {return arr;}
	else if (arr.length==2) {
		if (arr[0]>arr[1]) {
			let tmp=arr[1];
			arr[1]=arr[0];
			arr[0]=tmp;};
		//console.log("stack depth : " + n);
		//console.log(arr);
		return arr;}
	else {
		const m=parseInt(arr.length/2);
		let l=MergeSort(arr.slice(0,m),n+1);
		let r =MergeSort(arr.slice(m,arr.length),n+1);
		let y=l.length+r.length, a= 0, b=0;
		let tmp = Array(y); 
		while(a+b<y) {
			if (l[a] < r[b] && a<l.length) {tmp[a+b]=l[a];a++;}
			else if(b>=r.length) {tmp[a+b]=l[a];a++;} 
			else {tmp[a+b] = r[b];b++};};
	//console.log("stack depth : " + n);
	//console.log(tmp);
	return tmp;};		 		
};
vi = [21,17,16,2,3,9,10,11,2,6,7,1,3,5,4,7];
console.log(MergeSort(vi,0));
