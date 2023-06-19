function calculate() {
    var input = document.getElementById("yearinput").value
    if (input % 4 == 0) {
        if (input % 100 == 0) {
            if (input % 400 == 0) {
                document.getElementById("result").innerHTML = "You are lucky! This is a leap year!"
            } else {
                document.getElementById("result").innerHTML = "Bad Luck! This is not a leap year!"
            }
        } else {
            document.getElementById("result").innerHTML = "You are lucky! This is a leap year!"
        }
    } else {
        document.getElementById("result").innerHTML = "Bad Luck! This is not a leap year!"
    }
}