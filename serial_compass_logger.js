input.onButtonPressed(Button.A, function () {
    pause += -1
    pause = Math.max(1, pause)
    basic.showNumber(pause)
})
input.onButtonPressed(Button.B, function () {
    pause += 1
    pause = Math.min(10, pause)
    basic.showNumber(pause)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(input.compassHeading())
})
let pause = 0
pause = 1
serial.redirectToUSB()
basic.forever(function () {
    basic.clearScreen()
    basic.pause(pause * 1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    serial.writeLine("" + input.compassHeading())
})
