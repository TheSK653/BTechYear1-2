function fun(){
    var a=10;
    var b=20;
    function fu(a,b){
        a++;
        b++;
        console.log(a);
        console.log(b);
    }
    return fu(a,b);
}
fun();