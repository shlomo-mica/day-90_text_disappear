import threading
import tkinter as tk
import keyboard
import time

S=11
class TypingTimer:
    def __init__(self):
        self.timer = None
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root, width=100, height=100)
        self.text_area = tk.Text(self.frame, fg="black", bg="white", wrap="word", font=("Arial", 18))
        self.start_button = tk.Button(self.root, text="Start Transition",command=self.timer_expired, pady=11)
        self.start_button.pack()
        self.second_button = tk.Button(self.root, text="hex color change", command=self.Hex_color_code_list)
        self.second_button.pack()
        self.setup_gui()
        self.set_keypress_listener()

    def timer_expired(self):
        print("Timer expired!")
        self.Hex_color_code_list()

        #gself.text_area.insert("1.0", "Try typing again\n\n")

    def reset_timer(self):
        if self.timer is not None:
            self.timer.cancel()
        self.timer = threading.Timer(3.0, self.timer_expired)
        self.timer.start()

    def setup_gui(self):
        self.frame.bind("<KeyPress>", self.keydown)
        self.frame.bind("<KeyRelease>", self.keyup)
        self.frame.pack()
        self.text_area.pack(expand=True, fill="both")
        self.frame.focus_set()

    def keyup(self, e):
        print('up', e.char)

    def keydown(self, e):
        print('down', e.char)
        self.reset_timer()

    def set_keypress_listener(self):
        keyboard.on_press(lambda _: self.reset_timer())

    def run(self):
        self.root.mainloop()
        keyboard.wait('esc')
    def Hex_color_code_list(self):
        global S
        print(S)
        S -= 1
        COLOR_DICT = {1: '#ffffff', 2: '#e5e5e5', 3: '#cccccc', 4: '#b2b2b2', 5: '#999999',
                      6: '#7f7f7f', 7: '#666666', 8: '#4c4c4c',
                      9: '#333333', 10: '#191919', 11: '#000000'}


        if S == 0:
            print("STOP")
            S = 11

            self.text_area.delete('1.0', tk.END)
            self.text_area.config(background="white", foreground="black")
            self.text_area.insert("1.0", "Try typing again\n\n\n")


        else:
            self.gradually_change_color_2(COLOR_DICT[S], self.text_area)




    def gradually_change_color_2(self,bg_color, text_area_widget):
        # NEW FUNCTION WITH HEX COLORS CODE
        #time.sleep(1)
        text_area_widget.config(foreground=bg_color)


        text_area_widget.after(300, self.Hex_color_code_list)



if __name__ == "__main__":
     typing_timer = TypingTimer()
     typing_timer.run()

# In this class:
# - The `__init__` method initializes the timer and sets up the GUI.
# - The `timer_expired` method is called when the timer expires.
# - The `reset_timer` method resets the timer.
# - The `setup_gui` method sets up the GUI.
# - The `keyup` and `keydown` methods handle key press and release events.
# - The `set_keypress_listener` method sets up the key press event listener using the `keyboard` library.
# - The `run` method starts the Tkinter main loop and waits for the 'esc' key to exit the script.
#
# Now, the code is organized and encapsulated within a class. Feel free to customize it further as needed!
# # for i in reversed(COLOR_DICT):
#         #     gradually_change_color_2(COLOR_DICT[i], text_area)
#         #     print(COLOR_DICT[i])