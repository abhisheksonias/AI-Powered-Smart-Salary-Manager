import tkinter as tk
from tkinter import messagebox
import requests

# Payman API Secret Key
PAYMAN_API_SECRET = "YWd0LTFmMDA5YTRmLTcwYWItNmFhMy05Y2UzLWZmN2NhN2M0ODI5MjpNOEdJa1hadk5qVE5kdVprYTRYUVlCT00zbA=="

# Function to fetch balance
def fetch_balance():
    try:
        url = "https://agent.payman.ai/api/balances/currencies/TSD"

        headers = {
            "x-payman-api-secret": PAYMAN_API_SECRET,
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            balance_data = response.json()

            # Handle direct float response
            if isinstance(balance_data, float):
                balance = balance_data
            elif "balanceDecimal" in balance_data:
                balance = balance_data["balanceDecimal"]
            else:
                balance_label.config(text="❌ Unexpected response format.")
                return

            # Update balance label
            balance_label.config(text=f"💰 Current Balance: {balance} TSD")
        else:
            balance_label.config(text=f"❌ Failed to fetch balance: {response.text}")

    except Exception as e:
        balance_label.config(text=f"❌ An error occurred: {str(e)}")

# Initialize GUI
balance_root = tk.Tk()
balance_root.title("Check Account Balance")
balance_root.geometry("500x300")
balance_root.configure(bg="#f5f5f5")

# Header
header_label = tk.Label(balance_root, text="💼 Payman AI - Check Balance", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#2c3e50")
header_label.pack(pady=20)

# Balance Display
balance_label = tk.Label(balance_root, text="", font=("Arial", 16), bg="#f5f5f5", fg="#2c3e50")
balance_label.pack(pady=20)

# Button to Fetch Balance
balance_button = tk.Button(balance_root, text="🔍 Get Balance", font=("Arial", 14, "bold"), bg="#3498db", fg="white", padx=20, pady=10, command=fetch_balance)
balance_button.pack(pady=30)

# Footer
footer_label = tk.Label(balance_root, text="Powered by AI & Payman SDK", font=("Arial", 10), bg="#f5f5f5", fg="#7f8c8d")
footer_label.pack(side="bottom", pady=10)

# Run the GUI
balance_root.mainloop()
