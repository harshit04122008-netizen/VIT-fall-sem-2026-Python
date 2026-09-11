from nicegui import ui

n_input = ui.input(label='Enter a number')
l_input = ui.input(label='Enter a list of numbers separated by spaces')
result_label = ui.label()

def calculate():
    n = int(n_input.value)
    l = [int(x) for x in l_input.value.split()]

    output = ""

    for i in range(n):
        output += f"{l[i-2]}"

    result_label.set_text(f"Result: {output}")

ui.button('Calculate', on_click=calculate)

ui.run()