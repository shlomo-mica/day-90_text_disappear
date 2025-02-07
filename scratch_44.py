import tkinter as tk
import time as time
import ast


def start_timer(seconds_count):
    while seconds_count != 0:
        if on_key_press == 33:
            print("pressss")
            break
        time.sleep(1)
        seconds_count -= 1
        print(seconds_count)
    else:
        return None


def on_key_release(event):
    start_timer(3)
    print('start timer,,,Key release')



def on_key_press(event):
    t1 = time.strftime("%S")
    print(t1)
    print("Key pressed:", event.keysym, t1)
    start_timer(0)
    # print(f"t2 time == {on_key_release(event)}")
    return 33


# start timer 4 seconds


root = tk.Tk()
root.geometry('150x150')
root.title("Key Event Example")

# Bind the key press event to the on_key_press function
# root.bind("<KeyPress>", on_key_press)

root.bind("<KeyRelease>", on_key_release)
root.bind("<KeyPress>", on_key_press)
zero_press_time = time.strftime('%S')

print(zero_press_time)
# Run the application
text_area = tk.Text(root, fg="black", bg="orange", wrap="word", font=("Arial", 18))
text_area.pack(expand=True, fill="both")

string_number = "123"
integer_number = ast.literal_eval(string_number)
print(integer_number - 23)  # Output: 123

root.mainloop()

# while on_key_press(event):
#     print(on_key_press(event))
#     while duration != 0:
#         time.sleep(1)
#         duration -= 1
#         print(duration)


# def on_key_release(event):
#     t2 = time.strftime("%S")
#     running_time = ast.literal_eval(t2)
#     start_typing_time = ast.literal_eval(zero_press_time)
#     print("release", event.keysym, t2)
#     print("zero press time,", zero_press_time)
#     print(running_time - start_typing_time)
#
#     if abs(running_time - start_typing_time) > 15:
#         print("end session")
#         root.destroy()
#     else:
#         print("below zero #")  # kt1==try again zero )
