import tkinter as tk
from tkinter import font as tkFont
import fullCalc as fc

def main():
    start()

def start():
    root = tk.Tk()
    
    # Set up the window
    root.title("Calculator")
    # root.resizable(width=False, height=False)

    window_width = 800
    window_height = 400
    dp = 3  # decimal places in the result
    MAX_DP = 50
    MAX_LEN = 65
    dark_mode = False
    default_colour = "#F0F0F0"
    dark_colour = "#333333"
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    empty_response = ""


    def user_solve():
        eq = clc_eq.get()
        ans = fc.solve(eq)
        if ans[0] == "I":
            clc_result["text"] = empty_response
            clc_error["text"] = ans
        else:
            clc_result["text"] = wrap(ans, 20)
            if fc.disp_power_disc:
                clc_error["text"] = "NOTE: this is considered undefined on standard calculators."
                fc.disp_power_disc = False
            else:
                clc_error["text"] = ""
            if len(clc_result["text"]) > 17 and len(clc_result["text"]) < MAX_LEN: 
                clc_error["text"] = "WARNING: values over 16 digits may return incorrect answers due to floating-point arithmetic error"
            if len(clc_result["text"]) >= MAX_LEN:
                clc_result["text"] = wrap(("{:e}".format(float(ans))), 20)
        global dp
        dp = 3


    def incr_dp():
        global dp
        eq = clc_eq.get()
        ans = fc.solve(eq)
        if ans[0] == "I":
            clc_result["text"] = empty_response
            clc_error["text"] = ans
        else:
            if dp < MAX_DP:
                dp += 1
            clc_result["text"] = wrap(fc.solve(eq, dp), 20)
            if fc.disp_power_disc:
                clc_error["text"] = "NOTE: this is considered undefined on standard calculators."
                fc.disp_power_disc = False
            else:
                clc_error["text"] = ""
            if len(clc_result["text"]) > 17 and len(clc_result["text"]) < MAX_LEN: 
                clc_error["text"] = "WARNING: values over 16 digits may return incorrect answers due to floating-point arithmetic error"
            if len(clc_result["text"]) >= MAX_LEN:
                clc_result["text"] = wrap(("{:e}".format(float(ans))), 20)
            # else:
            #     clc_error["text"] = ""


    def decr_dp():
        global dp
        eq = clc_eq.get()
        ans = fc.solve(eq)
        if ans[0] == "I":
            clc_result["text"] = empty_response
            clc_error["text"] = ans
        else:
            if dp > 0:
                dp -= 1
            clc_result["text"] = wrap(fc.solve(eq, dp), 20)
            if fc.disp_power_disc:
                clc_error["text"] = "NOTE: this is considered undefined on standard calculators."
                fc.disp_power_disc = False
            else:
                clc_error["text"] = ""
            if len(clc_result["text"]) > 17 and len(clc_result["text"]) < MAX_LEN: 
                clc_error["text"] = "WARNING: values over 16 digits may return incorrect answers due to floating-point arithmetic error"
            if len(clc_result["text"]) >= MAX_LEN:
                clc_result["text"] = wrap(("{:e}".format(float(ans))), 20)


    def wrap(string, max_width):
        para = ""
        temp = ""
        count = 0
        for i in range(len(string)):
            temp += string[i]
            count += 1
            if count == max_width or i == len(string)-1:
                para += temp + "\n"
                temp = ""
                count = 0
        return para


    def invert_colour_mode():
        global dark_mode
        dark_mode = not dark_mode
        if dark_mode:
            root.config(bg=dark_colour)
            clc_col_mode.config(bg=default_colour, fg="black")
            
            clc_title.config(bg=dark_colour, fg=default_colour)
            clc_subtitle.config(bg=dark_colour, fg=default_colour)
            clc_info.config(bg=dark_colour, fg=default_colour)
            clc_error.config(bg=dark_colour, fg="pink")
            clc_result.config(bg=dark_colour, fg=default_colour)
        else:
            root.config(bg=default_colour)
            clc_col_mode.config(bg="black", fg=default_colour)

            clc_title.config(bg=default_colour, fg=dark_colour)
            clc_subtitle.config(bg=default_colour, fg=dark_colour)
            clc_info.config(bg=default_colour, fg=dark_colour)
            clc_error.config(bg=default_colour, fg="dark red")
            clc_result.config(bg=default_colour, fg=dark_colour)

    ###################### USER KEYBOARD FUNCTIONS ######################
    def user_solve_kb(event):
        user_solve()


    def incr_dp_kb(event):
        incr_dp()


    def decr_dp_kb(event):
        decr_dp()


    root.bind('<Return>', user_solve_kb)
    root.bind('<Up>', incr_dp_kb)
    root.bind('<Down>', decr_dp_kb)
    ###################### USER KEYBOARD FUNCTIONS ######################

    # center of screen
    cx = int(screen_width/2 - window_width/2)
    cy = int(screen_height/3 - window_height/3)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{cx}+{cy}')

    # frm_entry = tk.Frame(master=root)
    root.config(bg=default_colour)
    clc_eq = tk.Entry(master=root, width=30)

    # Layout the temperature Entry and Label in frm_entry
    # using the .grid() geometry manager


    # All user buttons
    clc_col_mode = tk.Button(
        master=root,
        text="\N{BLACK SUN WITH RAYS}",
        command=invert_colour_mode,
        width=3,
        height=2,
        bg="black",
        fg=default_colour
    )

    clc_calc = tk.Button(
        master=root,
        text="\N{RIGHTWARDS BLACK ARROW}",
        command=user_solve,
        width=8,
        height=1,
        bg="green"
    )

    clc_decrdp = tk.Button(
        master=root,
        text="\N{DOWNWARDS BLACK ARROW}",
        command=decr_dp,
        width=1,
        height=1,
        bg="grey"
    )

    clc_incrdp = tk.Button(
        master=root,
        text="\N{UPWARDS BLACK ARROW}",
        command=incr_dp,
        width=1,
        height=1,
        bg="grey"
    )

    # Fonts
    ttl_font = tkFont.Font(family='Yu Gothic', size=30, weight="normal")
    sttl_font = tkFont.Font(family='Yu Gothic', size=12, weight="normal")
    btn_font = tkFont.Font(family='Yu Gothic', size=12, weight="bold")

    # Labels
    clc_title = tk.Label(
        master=root, 
        text="General Expression Calculator", 
        bg=default_colour, 
        font=ttl_font)

    clc_subtitle = tk.Label(
        master=root, 
        text="To start, please enter an equation in the box below.", 
        font=sttl_font, 
        bg=default_colour)

    clc_info = tk.Label(
        master=root, text="""
    You may use 
    '+' for addition,
    '-' for subtraction,
    '*' for multiplciation,
    '/' for division,
    '^' for exponentiation,
    'log(x)' for log (base e) (x) calculations, and 
    'exp(x)' for e^x calculations.
    Parentheses '()' are also allowed.

    Click the green button to evaluate your expression, 
    and the arrow buttons to change the number of decimal places shown.
    """,
    font=sttl_font,
    bg=default_colour
    )

    clc_info.config(font=("Yu Gothic", 10), justify="left")
    clc_result = tk.Label(master=root, text=empty_response, font=("Segoe UI", 11), bg=default_colour)
    clc_error = tk.Label(master=root, text="", bg=default_colour, fg="dark red")
    clc_calc.config(font=btn_font)
    clc_incrdp.config(font=btn_font)
    clc_decrdp.config(font=btn_font)

    ###################### POSITIONING ALL WIDGETS ######################
    clc_title.place(relx=0.5, rely=.1, anchor='center')
    clc_subtitle.place(relx=0.5, rely=.2, anchor='center')
    clc_info.place(relx=0.28, rely=.7, anchor='center')
    clc_eq.place(relx=.2, rely=.35, anchor='center')
    clc_calc.place(relx=.5, rely=.35, anchor='center')
    clc_result.place(relx=.8, rely=.375, anchor='center')
    clc_incrdp.place(relx=.685, rely=.35, anchor='center')
    clc_decrdp.place(relx=.915, rely=.35, anchor='center')
    clc_error.place(relx=.5, rely=.45, anchor='center')
    clc_col_mode.place(relx=.95, rely=.9, anchor='center')

    
    # send gui to front
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.focus_force()
    clc_eq.focus_set() # focus the equation entry on load
    # win32gui.SetForegroundWindow(root.winfo_id())
    # Run the application
    root.mainloop()


if __name__ == '__main__':
    main()
