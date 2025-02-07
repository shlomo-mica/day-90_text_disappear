from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import ttk
import time

S = 11


class TimerApp:
    def __init__(self, root, text):
        self.root = root
        self.root.title("Timer App")
        self.text = text

        # Label
        self.label = ttk.Label(root, text="Select Timer Duration (seconds):")
        self.label.pack(pady=10)
        # Combobox
        self.combo = ttk.Combobox(root, values=[10, 20, 30, 40, 50, 60])
        self.combo.pack(pady=10)
        self.combo.current(0)  # Set default value

        # Start Button
        self.start_button = ttk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=1)
        # Text Area

        textarea = self.text(root, height=4, font=("Helavetica", 22), fg='red')

        textarea.pack(pady=5, padx=33)
        # Timer Label
        self.timer_label = ttk.Label(root, text="")
        self.timer_label.pack(pady=5, padx=133)

    def start_timer(self):
        try:
            duration = int(self.combo.get())
            self.timer_label.config(text=f"Time remaining: {duration} seconds")
            self.root.update()
            while duration > 0:
                time.sleep(1)
                duration -= 1
                self.timer_label.config(text=f"Time remaining: {duration} seconds")
                self.root.update()
            self.timer_label.config(text="Time's up!")
        except ValueError:
            self.timer_label.config(text="Please select a valid duration.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x350')
    root['bg'] = '#33cc00'
    t = tk.Text

    app = TimerApp(root, t)
    root.mainloop()


#############################################################################
# program 2
def key_handler(event):
    print(event.char, event.keysym, event.keycode)





def Hex_color_code_list():
    global S
    print(S)
    S -= 1
    COLOR_DICT = {1: '#ffffff', 2: '#e5e5e5', 3: '#cccccc', 4: '#b2b2b2', 5: '#999999',
                  6: '#7f7f7f', 7: '#666666', 8: '#4c4c4c',
                  9: '#333333', 10: '#191919', 11: '#000000'}

    # for key, value in COLOR_DICT.items():
    #     print(COLOR_DICT[key])
    if S == 0:
        print("STOP")
        S = 11

        text_area.delete('1.0',tk.END)
        text_area.config(background="white", foreground="black")
        text_area.insert("1.0", "Try typing again\n\n\n")


    else:
        gradually_change_color_2(COLOR_DICT[S], text_area)

    # for i in reversed(COLOR_DICT):
    #     gradually_change_color_2(COLOR_DICT[i], text_area)
    #     print(COLOR_DICT[i])


def gradually_change_color_2(bg_color, text_area_widget):
    # NEW FUNCTION WITH HEX COLORS CODE
    # time.sleep(1)
    text_area_widget.config(foreground=bg_color)

    # text_area_widget.config(bg=bg_color,foreground='#000000')
    # text_area_widget.insert("test words")
    # Schedule the next step

    text_area_widget.after(500, Hex_color_code_list)


def gradually_change_color(widget, current_color, target_color, steps, step=0):
    """
    Gradually changes the background color of the widget.
    """
    if step > steps:
        print(step)
        return  # End of transition

    # Calculate intermediate color
    r = int(current_color[0] + (target_color[0] - current_color[0]) * (step / steps))
    g = int(current_color[1] + (target_color[1] - current_color[1]) * (step / steps))
    b = int(current_color[2] + (target_color[2] - current_color[2]) * (step / steps))

    # Set the new background color
    color = f"#{r:02x}{g:02x}{b:02x}"
    print(f"#{r:02x}")
    # NEW FUNCTION WITH HEX COLORS CODE

    widget.config(bg=color)

    # Schedule the next step
    widget.after(50, gradually_change_color, widget, current_color, target_color, steps, step + 1)


def start_color_transition():
    # Starting color (black) and target color (white)
    start_color = (0, 0, 0)  # RGB for black
    end_color = (255, 255, 255)  # RGB for white
    steps = 50  # Number of steps for the transition

    gradually_change_color(text_area, start_color, end_color, steps)


# Main Tkinter application
root = tk.Tk()
root.title("Gradual Background Transition")
root.bind("<Key>", key_handler)
text_area = tk.Text(root, fg="black", bg="white", wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")
text_area.insert("1.0", "The background color will transition gradually from black to white.")
text_area.insert("1.0", "text words\n")
# text_area.config(foreground="red")
# Button to start the color transition
start_button = tk.Button(root, text="Start Transition", command=start_color_transition, pady=11)
start_button.pack()
second_button = tk.Button(root, text="hex color change", command=Hex_color_code_list)
second_button.pack()
root.mainloop()
