package conditionals

fun main(args: Array<String>) {
    val age: Int = 28
    if(age < 18){
        println("You can`t register")
    }
    else if(age < 21){
        println("Maybe you can register")
    }
    else {
        println("You are good to go!")
    }
}