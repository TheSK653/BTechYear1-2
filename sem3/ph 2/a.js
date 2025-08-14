// let arr=[10,20,30,40,50];

// arr.forEach();
// let ret=arr.forEach(function(item,index){
//     console.log(item*item)
//     return item*item;
// } );

// let ret=arr.map(function(item,index){
//     return item+index
// })

// let ret=arr.filter(function(item,index){
//     if(item%10==0)
//         return item
// })

// console.log(ret);


let arr=[1,2,3,4,5,6];
let a=arr.map(function(item,index){
    return item*2
}).filter(function(item,index){
    if (item>=10)
    return true
})

console.log(a);

