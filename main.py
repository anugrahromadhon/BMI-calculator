import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height to meters

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")

        bmi = weight / (height ** 2)
        category = get_bmi_category(bmi)

        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.config(bg="#e6f7ff")

# Widgets
header_label = tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"), bg="#e6f7ff", fg="#0073e6")
header_label.pack(pady=10)

weight_label = tk.Label(root, text="Enter your weight (kg):", font=("Arial", 12), bg="#e6f7ff", fg="#333333")
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Enter your height (cm):", font=("Arial", 12), bg="#e6f7ff", fg="#333333")
height_label.pack()
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12), bg="#0073e6", fg="white", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e6f7ff", fg="#333333", justify="center")
result_label.pack(pady=10)

# Run the application
root.mainloop()
