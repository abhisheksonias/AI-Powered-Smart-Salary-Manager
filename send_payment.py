# smart_salary_distribution.py

import tkinter as tk
from tkinter import messagebox
import requests
import json

# Step 1: Initialize GUI
root = tk.Tk()
root.title("AI-Powered Employee Salary Distribution")
root.geometry("800x400")
root.configure(bg="#f5f5f5")

# Welcome Message
def show_welcome_message():
    messagebox.showinfo("Welcome", "🚀 Welcome to AI-Powered Salary Distribution! Simplify employee payments.")

root.after(500, show_welcome_message)

# Step 2: Design the Form
header_label = tk.Label(root, text="💼 Employee Salary Distribution System", font=("Helvetica", 24, "bold"), bg="#f5f5f5", fg="#2c3e50")
header_label.pack(pady=30)

# Input Fields
form_frame = tk.Frame(root, bg="#f5f5f5")
form_frame.pack(pady=20)

def create_label_and_entry(frame, label_text, row):
    label = tk.Label(frame, text=label_text, font=("Arial", 14), bg="#f5f5f5", fg="#34495e")
    label.grid(row=row, column=0, sticky="w", padx=20, pady=10)
    entry = tk.Entry(frame, font=("Arial", 14), width=40, relief="solid", borderwidth=1)
    entry.grid(row=row, column=1, padx=10, pady=10)
    return entry

name_entry = create_label_and_entry(form_frame, "👤 Employee Name:", 0)
id_entry = create_label_and_entry(form_frame, "🆔 Employee ID:", 1)
leave_entry = create_label_and_entry(form_frame, "📅 Leave Days:", 2)

# Payman API Secret Key
PAYMAN_API_SECRET = "YWd0LTFmMDA5YTRmLTcwYWItNmFhMy05Y2UzLWZmN2NhN2M0ODI5MjpNOEdJa1hadk5qVE5kdVprYTRYUVlCT00zbA=="

# Step 3: Backend Integration - Send Payment
def send_payment():
    try:
        employee_name = name_entry.get().strip()
        employee_id = id_entry.get().strip()
        leave_days = int(leave_entry.get() or 0)

        if not employee_name or not employee_id:
            messagebox.showwarning("Input Error", "Please enter both Employee Name and Employee ID.")
            return

        with open("employees.json", "r") as file:
            employees = json.load(file)

        # Find employee by name and employee_id
        employee = next((emp for emp in employees if emp["name"] == employee_name and emp["employee_id"] == employee_id), None)

        if not employee:
            messagebox.showerror("Error", "❌ Employee not found.")
            return

        salary = int(employee["salary"])
        deducted_salary = salary - (leave_days * (salary // 30))

        url = "https://agent.payman.ai/api/payments/send-payment"

        payload = {
            "amountDecimal": deducted_salary,
            "payeeId": employee["id"]
        }

        headers = {
            "x-payman-api-secret": PAYMAN_API_SECRET,
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            messagebox.showinfo("Payment Sent", f"💸 Payment of {deducted_salary} sent to {employee_name} successfully!")
        else:
            messagebox.showerror("Payment Error", f"❌ Failed to send payment to {employee_name}: {response.text}")

    except Exception as e:
        messagebox.showerror("Error", f"❌ An error occurred: {str(e)}")

# Hover Effect
def on_enter(e):
    e.widget.config(bg="#2c3e50")

def on_leave(e):
    e.widget.config(bg="#3498db")

def create_styled_button(frame, text, command, col):
    button = tk.Button(frame, text=text, font=("Arial", 14, "bold"), command=command, bg="#3498db", fg="white", padx=20, pady=5, relief="flat", activebackground="#2980b9")
    button.grid(row=0, column=col, padx=15)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=30)

create_styled_button(button_frame, "Send Payment", send_payment, 0)

# Footer
footer_label = tk.Label(root, text="Powered by AI & Payman SDK", font=("Arial", 10), bg="#f5f5f5", fg="#7f8c8d")
footer_label.pack(side="bottom", pady=10)

# Step 4: Run the Application
root.mainloop()
