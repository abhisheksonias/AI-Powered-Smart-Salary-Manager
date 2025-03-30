import tkinter as tk
import subprocess

# Function to open Add Employee Page
def open_add_employee():
    subprocess.Popen(['python', 'Create.py'])

# Function to open Pay Salaries Page
def open_pay_salaries():
    subprocess.Popen(['python', 'send_payment.py'])

# Function to open Check Balance Page
def open_check_balance():
    subprocess.Popen(['python', 'get_balance.py'])

# Initialize Home Page
home_root = tk.Tk()
home_root.title("Smart Salary Distribution System")
home_root.geometry("600x400")
home_root.configure(bg="#f5f5f5")

# Header
header_label = tk.Label(home_root, text="🏢 Smart Salary Distribution", font=("Helvetica", 24, "bold"), bg="#f5f5f5", fg="#2c3e50")
header_label.pack(pady=40)

# Button Style
def create_styled_button(root, text, command):
    return tk.Button(root, text=text, font=("Arial", 16, "bold"), bg="#3498db", fg="white", padx=20, pady=10, command=command, relief="flat", activebackground="#2980b9")

# Add Employee Button
add_employee_button = create_styled_button(home_root, "➕ Add Employee", open_add_employee)
add_employee_button.pack(pady=20)

# Pay Salaries Button
pay_salaries_button = create_styled_button(home_root, "💸 Pay Salaries", open_pay_salaries)
pay_salaries_button.pack(pady=20)

# Check Balance Button
check_balance_button = create_styled_button(home_root, "💰 Check Account Balance", open_check_balance)
check_balance_button.pack(pady=20)

# Footer
footer_label = tk.Label(home_root, text="Powered by AI & Payman SDK", font=("Arial", 10), bg="#f5f5f5", fg="#7f8c8d")
footer_label.pack(side="bottom", pady=10)

# Run Home Page
home_root.mainloop()
