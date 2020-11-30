"use strict";

var makeNode= function ({val = null, Nextnode =null ,sub="node"}={}){
	return {
		name : sub,
		link : function (node ) {
			Nextnode=node;},
		getVal : function () {
			return val;},
		getNext : function() {
			return Nextnode;},
		updateVal : function (value) {
			val=value;}
		};
	};


let a = makeNode({sub:"a"});
console.log(a.getVal());
a.updateVal(10);
let b = makeNode({val:20, Nextnode:a, sub:"b"});
console.log(a.val);
console.log(a.getVal());
console.log(b.getNext());

function ListNode(val, next) {
      this.val = (val===undefined ? 0 : val)
      this.next = (next===undefined ? null : next)
}


var addTwoNumbers = function(l1, l2) {
    let i = 0;
    let carry= 0;
    let prevNode=null;
    let ans = null;
    while (l1!=null || l2!=null) {
        val1=(l1.val===undefined ? 0 : l1.val);
        val2=(l2.val===undefined ? 0 : l2.val);
        valtmp=val1+val2+carry;
        val=valtmp%10;
        carry=parseInt(valtmp/10);
        if (i == 0) {
            prevNode=new ListNode(val,null);
            l1=l1.next;
            l2=l2.next;
            ans=prevNode;
            }else {    
                next=new ListNode(val,null);
                l1=l1.next;
                l2=l2.next;
                prevNode.next=next;
                prevNode=next;
            };
        i=i+1;
    };
	if (carry!=0) {
		next=new ListNode(carry,null);
		prevNode.next=next;
		prevNode=next;
	};
    return ans;
};



