from tkinter import CENTER, Tk, messagebox, ttk

# Initialize main window
root = Tk()
root.geometry("600x500")
root.title("Transaction Entry Form")

# Configure rows and columns for resizing
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)

# App title
app_title = ttk.Label(
    root,
    text="My Expenses Tracker",
    font=("Segoe UI", 16, "bold"),
    anchor="center"
)
app_title.grid(column=0, row=0, columnspan=2, pady=10)

# Transaction data storage
transaction_list = []

# ----------- FORM FRAME -----------
form_frame = ttk.LabelFrame(root, text="Add Transaction")
form_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
form_frame.columnconfigure(0, weight=1)
form_frame.columnconfigure(1, weight=2)

# Transaction Name
name_label = ttk.Label(form_frame, text="Transaction Name:")
name_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = ttk.Entry(form_frame)
name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# Transaction Details
details_label = ttk.Label(form_frame, text="Details:")
details_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
details_entry = ttk.Entry(form_frame)
details_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# Transaction Amount
amount_label = ttk.Label(form_frame, text="Amount:")
amount_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
amount_entry = ttk.Entry(form_frame)
amount_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# Category
category_label = ttk.Label(form_frame, text="Category:")
category_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
category_combo = ttk.Combobox(
    form_frame,
    state="readonly",
    values=["Salary", "Bills", "Food", "Rent", "Fuel", "Other"]
)
category_combo.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

# Type
type_label = ttk.Label(form_frame, text="Type:")
type_label.grid(row=4, column=0, sticky="e", padx=5, pady=5)
type_combo = ttk.Combobox(
    form_frame,
    state="readonly",
    values=["Income", "Expense"]
)
type_combo.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

# ----------- TABLE FRAME -----------
table_frame = ttk.LabelFrame(root, text="Transaction Table")
table_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Treeview Table
transaction_table = ttk.Treeview(
    table_frame,
    columns=("c1", "c2", "c3", "c4", "c5"),
    show='headings'
)
transaction_table.heading("c1", text="Name")
transaction_table.heading("c2", text="Details")
transaction_table.heading("c3", text="Amount")
transaction_table.heading("c4", text="Category")
transaction_table.heading("c5", text="Type")

for col in ("c1", "c2", "c3", "c4", "c5"):
    transaction_table.column(col, anchor=CENTER)

transaction_table.grid(row=0, column=0, sticky="nsew")
table_frame.rowconfigure(0, weight=1)
table_frame.columnconfigure(0, weight=1)

# ----------- FUNCTIONS -----------

def refresh_table():
    """Refresh the treeview with the latest transaction data"""
    transaction_table.delete(*transaction_table.get_children())
    for txn in transaction_list:
        transaction_table.insert(
            '', 'end',
            values=(txn["name"], txn["details"], txn["amount"], txn["category"], txn["type"])
        )

def submit():
    """Handle adding a new transaction"""
    t_name = name_entry.get().strip()
    t_details = details_entry.get().strip()
    t_amount = amount_entry.get().strip()
    t_category = category_combo.get().strip()
    t_type = type_combo.get().strip()

    if t_name and t_details and t_amount and t_category and t_type:
        try:
            t_amount = float(t_amount)
            transaction_list.append({
                "name": t_name,
                "details": t_details,
                "amount": t_amount,
                "category": t_category,
                "type": t_type
            })
            refresh_table()

            # Clear form fields
            name_entry.delete(0, 'end')
            details_entry.delete(0, 'end')
            amount_entry.delete(0, 'end')
            category_combo.set('')
            type_combo.set('')

            messagebox.showinfo("Success", "Transaction Added Successfully")
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")
    else:
        messagebox.showerror("Error", "Please fill all the details")

# Submit Button
submit_button = ttk.Button(form_frame, text="Submit", command=submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# ----------- RUN APP -----------
root.mainloop()
