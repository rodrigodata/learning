package conditionals

fun main(args: Array<String>) {
    // IF, ELSE IF, ELSE
    println("!! IF, ELSE IF, ELSE !!")
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

    println("----------------------")

    // WHEN
    println("!! WHEN !!")
    val mode: Int = 10

    when(mode){
        1 -> println("the mode is lazy.")
        2 -> {
            println("the mode is 2")
            println("So the mode is busy.")
        }
        3 -> println("The mode is super productive")
        else -> {
            println("Unknown mode.")
        }
    }

    println("----------------------")
}
