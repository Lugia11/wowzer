from pyscript import document
import keyboard

def on_w_press(event):
    if event.name == 'w':
        print("w is pressed")
        # If you want to execute JS code, you'd need a web context.

keyboard.on_press(on_w_press)
print ("Hello world")
output_div = document.querySelector("#textarea")

output_div.innerText = "hello world!"




