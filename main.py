tempurture = 0

def on_button_pressed_b():
    if (tempurture) >= (35):
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global tempurture
    tempurture = input.temperature()
    led.plot_bar_graph(tempurture, 40)
    if input.button_is_pressed(Button.A):
        basic.show_number(tempurture)
basic.forever(on_forever)
