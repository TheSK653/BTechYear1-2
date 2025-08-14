let person={
    name:"soham",
    age:20,
    favcolor:"blue"
}
person.ismale=true
console.log(person.ismale)
Object.freeze(person)
person.name="soham kundu"
console.log(person.name)