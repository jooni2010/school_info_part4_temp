let tempurture = 0
input.onButtonPressed(Button.B, function () {
    if (tempurture >= 30) {
        basic.showString("hot")
    }
})
basic.forever(function () {
    tempurture = input.temperature()
    led.plotBarGraph(
    tempurture,
    40
    )
    if (input.buttonIsPressed(Button.A)) {
        basic.showNumber(tempurture)
    }
})
