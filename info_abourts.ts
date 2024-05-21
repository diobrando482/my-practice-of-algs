function id<T>(arg:T):T{
    return arg;
}
let output1 = id<string>('hello world')
let output2 = id<number>(42442424215235252)
console.log(output1 + output2);
