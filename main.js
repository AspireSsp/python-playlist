// console.log("calling...");
// let fetchData = async()=>{
//     const data = await fetch('https://jsonplaceholder.typicode.com/posts');
//     console.log(data);
// }

// fetchData();


let a = function (){
    let name = "sanjay";
    function b(){
        console.log(name);
        console.log(c)
    }
    b();
}
let c = 10;
a();