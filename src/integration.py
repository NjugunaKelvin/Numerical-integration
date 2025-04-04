import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from scipy.integrate import quad
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to safely evaluate expressions
def safe_eval(expr, x):
    allowed_names = {"x": x, "np": np}
    try:
        return eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception:
        return None

# Numerical integration methods
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1  # Ensure even intervals for Simpson's Rule
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return (h/3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

# Function to perform integration
def integrate():
    try:
        expr = function_var.get()
        a = float(lower_limit_entry.get())
        b = float(upper_limit_entry.get())
        n = int(intervals_entry.get())
        if a >= b or n <= 0:
            messagebox.showerror("Error", "Invalid limits or intervals.")
            return

        def f(x): return safe_eval(expr, x)
        
        trapz_result = trapezoidal_rule(f, a, b, n)
        simpsons_result = simpsons_rule(f, a, b, n)
        standard_result, _ = quad(f, a, b)

        result_label.config(text=f"Trapezoidal: {trapz_result:.4f}\nSimpson's: {simpsons_result:.4f}\nStandard: {standard_result:.4f}")
        plot_function(f, a, b, expr)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to plot the graph with hover effect
def plot_function(f, a, b, expr):
    x_vals = np.linspace(a, b, 100)
    y_vals = f(x_vals)
    
    fig, ax = plt.subplots(figsize=(5, 3))
    line, = ax.plot(x_vals, y_vals, label=f"$f(x) = {expr}$", color="blue")
    ax.fill_between(x_vals, y_vals, alpha=0.3, color="cyan")
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid()

    hover_text = ax.text(0, 0, "", fontsize=10, color="black", bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    hover_text.set_visible(False)
    
    def on_hover(event):
        if event.inaxes == ax:
            x, y = event.xdata, event.ydata
            hover_text.set_text(f"x: {x:.2f}\ny: {y:.2f}")
            hover_text.set_position((x, y))
            hover_text.set_visible(True)
            fig.canvas.draw_idle()
        else:
            hover_text.set_visible(False)
            fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect("motion_notify_event", on_hover)

    for widget in frame_plot.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to reset inputs
def reset_inputs():
    function_var.set("")
    lower_limit_entry.delete(0, tk.END)
    upper_limit_entry.delete(0, tk.END)
    intervals_entry.delete(0, tk.END)
    result_label.config(text="")
    for widget in frame_plot.winfo_children():
        widget.destroy()

# Set up the main window
root = tb.Window(themename="darkly")
root.title("Numerical Integration Calculator")
root.geometry("600x600")
root.configure(bg="#2c3e50")

frame_main = ttk.Frame(root, padding=20)
frame_main.pack(pady=10)

title_label = ttk.Label(frame_main, text="Numerical Integration", font=("Arial", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

function_var = tk.StringVar()
function_label = ttk.Label(frame_main, text="Enter function f(x):")
function_label.grid(row=1, column=0, sticky="w")
function_entry = ttk.Entry(frame_main, textvariable=function_var, width=30)
function_entry.grid(row=1, column=1, pady=5)

lower_limit_label = ttk.Label(frame_main, text="Lower limit (a):")
lower_limit_label.grid(row=2, column=0, sticky="w")
lower_limit_entry = ttk.Entry(frame_main, width=10)
lower_limit_entry.grid(row=2, column=1, pady=5)

upper_limit_label = ttk.Label(frame_main, text="Upper limit (b):")
upper_limit_label.grid(row=3, column=0, sticky="w")
upper_limit_entry = ttk.Entry(frame_main, width=10)
upper_limit_entry.grid(row=3, column=1, pady=5)

intervals_label = ttk.Label(frame_main, text="Number of intervals:")
intervals_label.grid(row=4, column=0, sticky="w")
intervals_entry = ttk.Entry(frame_main, width=10)
intervals_entry.grid(row=4, column=1, pady=5)

calculate_button = ttk.Button(frame_main, text="Integrate", command=integrate, bootstyle="primary")
calculate_button.grid(row=5, column=0, pady=10)

reset_button = ttk.Button(frame_main, text="Compute Again", command=reset_inputs, bootstyle="secondary")
reset_button.grid(row=5, column=1, pady=10)

result_label = ttk.Label(frame_main, text="", font=("Arial", 12, "bold"))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

frame_plot = ttk.Frame(root)
frame_plot.pack(pady=10)

root.mainloop()