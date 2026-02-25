class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket POS System")
        self.root.geometry("900x600")

        self.cart = []

        # ===== Title =====
        title = tk.Label(root, text="SUPERMARKET POS SYSTEM", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # ===== Product Frame =====
        product_frame = tk.Frame(root)
        product_frame.pack(pady=10)

        tk.Label(product_frame, text="Product Name").grid(row=0, column=0, padx=5)
        tk.Label(product_frame, text="Price").grid(row=0, column=1, padx=5)
        tk.Label(product_frame, text="Quantity").grid(row=0, column=2, padx=5)

        self.name_entry = tk.Entry(product_frame)
        self.name_entry.grid(row=1, column=0, padx=5)

        self.price_entry = tk.Entry(product_frame)
        self.price_entry.grid(row=1, column=1, padx=5)

        self.qty_entry = tk.Entry(product_frame)
        self.qty_entry.grid(row=1, column=2, padx=5)

        add_btn = tk.Button(product_frame, text="Add to Cart", command=self.add_to_cart, bg="green", fg="white")
        add_btn.grid(row=1, column=3, padx=10)

        # ===== Cart Table =====
        self.tree = ttk.Treeview(root, columns=("Name", "Price", "Qty", "Total"), show="headings")
        self.tree.heading("Name", text="Product Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Qty", text="Quantity")
        self.tree.heading("Total", text="Total")

        self.tree.pack(pady=20, fill="both", expand=True)

        # ===== Bottom Frame =====
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(pady=10)

        self.total_label = tk.Label(bottom_frame, text="Total: 0.00", font=("Arial", 14, "bold"))
        self.total_label.grid(row=0, column=0, padx=10)

        remove_btn = tk.Button(bottom_frame, text="Remove Selected", command=self.remove_item, bg="orange")
        remove_btn.grid(row=0, column=1, padx=5)

        clear_btn = tk.Button(bottom_frame, text="Clear Cart", command=self.clear_cart, bg="red", fg="white")
        clear_btn.grid(row=0, column=2, padx=5)

        checkout_btn = tk.Button(bottom_frame, text="Checkout", command=self.checkout, bg="blue", fg="white")
        checkout_btn.grid(row=0, column=3, padx=5)

    # ===== Functions =====
    def add_to_cart(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        qty = self.qty_entry.get()

        if name == "" or price == "" or qty == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            price = float(price)
            qty = int(qty)
        except ValueError:
            messagebox.showerror("Error", "Invalid price or quantity")
            return

        total = price * qty
        self.cart.append((name, price, qty, total))

        self.tree.insert("", tk.END, values=(name, price, qty, total))
        self.update_total()

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)

    def update_total(self):
        total = sum(item[3] for item in self.cart)
        self.total_label.config(text=f"Total: {total:.2f}")

    def remove_item(self):
        selected = self.tree.selection()
        if not selected:
            return

        for item in selected:
            index = self.tree.index(item)
            self.tree.delete(item)
            del self.cart[index]

        self.update_total()

    def clear_cart(self):
        self.tree.delete(*self.tree.get_children())
        self.cart.clear()
        self.update_total()

    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Warning", "Cart is empty")
            return

        receipt = "Receipt\n\n"
        for item in self.cart:
            receipt += f"{item[0]} x{item[2]} = {item[3]:.2f}\n"

        total = sum(item[3] for item in self.cart)
        receipt += f"\nTotal: {total:.2f}"

        messagebox.showinfo("Checkout", receipt)
        self.clear_cart()

# ===== Run Program =====
if __name__ == "__main__":
    root = tk.Tk()
    app = POS(root)
    root.mainloop()