"""
GST Billing & Inventory System
"""

from datetime import datetime

# ---------- Data structure ----------
# products: dict keyed by product_code
# each product is a dict:
# {
#   "name": str,
#   "cost_price": float,
#   "gst_rate": float,    # percent e.g. 18.0
#   "stock": int,
#   "sold": int,
#   "selling_price": float  # MUST be set by user; if <=0 it is considered "not set"
# }
products = {}


# ---------- Core operations ----------
def add_product():
    code = input("Enter product code (unique): ").strip()
    if not code:
        print("Product code cannot be empty.")
        return
    if code in products:
        print("Product code already exists. Use update instead.")
        return

    name = input("Product name: ").strip() or "Unnamed Product"

    # simple float input (one attempt, basic check)
    cp_raw = input("Cost price (₹): ").strip()
    try:
        cost_price = round(float(cp_raw), 2)
        if cost_price < 0:
            print("Cost price cannot be negative.")
            return
    except Exception:
        print("Invalid cost price. Aborting add.")
        return

    gst_raw = input("GST rate (%) e.g. 18 : ").strip()
    try:
        gst_rate = round(float(gst_raw), 2)
        if gst_rate < 0:
            print("GST rate cannot be negative.")
            return
    except Exception:
        print("Invalid GST rate. Aborting add.")
        return

    stock_raw = input("Opening stock quantity: ").strip()
    try:
        stock = int(stock_raw)
        if stock < 0:
            print("Stock cannot be negative.")
            return
    except Exception:
        print("Invalid stock quantity. Aborting add.")
        return

    sp_raw = input("Selling price (₹) (must be > 0): ").strip()
    try:
        selling_price = round(float(sp_raw), 2)
        if selling_price <= 0:
            print("Selling price must be greater than 0. Aborting add.")
            return
    except Exception:
        print("Invalid selling price. Aborting add.")
        return

    products[code] = {
        "name": name,
        "cost_price": cost_price,
        "gst_rate": gst_rate,
        "stock": stock,
        "sold": 0,
        "selling_price": selling_price,
    }
    print(f"[Added] Product '{name}' with code '{code}' added.")


def update_product():
    code = input("Enter product code to update: ").strip()
    p = products.get(code)
    if not p:
        print("Product not found.")
        return

    print("Leave blank to keep current value.")
    new_name = input(f"Name [{p['name']}]: ").strip()
    if new_name:
        p["name"] = new_name

    cp = input(f"Cost price [{p['cost_price']}]: ").strip()
    if cp:
        try:
            val = round(float(cp), 2)
            if val >= 0:
                p["cost_price"] = val
            else:
                print("Negative cost ignored.")
        except Exception:
            print("Invalid cost price; keeping old value.")

    gst = input(f"GST rate (%) [{p['gst_rate']}]: ").strip()
    if gst:
        try:
            val = round(float(gst), 2)
            if val >= 0:
                p["gst_rate"] = val
            else:
                print("Negative GST ignored.")
        except Exception:
            print("Invalid GST rate; keeping old value.")

    sp = input(f"Selling price [{p['selling_price']}]: ").strip()
    if sp:
        try:
            val = round(float(sp), 2)
            if val > 0:
                p["selling_price"] = val
            else:
                print("Selling price must be > 0; keeping old value.")
        except Exception:
            print("Invalid selling price; keeping old value.")

    print("[Updated] Product updated.")


def delete_product():
    code = input("Enter product code to delete: ").strip()
    if code in products:
        confirm = input(f"Type 'yes' to confirm deletion of {products[code]['name']}: ")
        if confirm.lower() == "yes":
            del products[code]
            print("[Deleted] Product removed.")
        else:
            print("Deletion cancelled.")
    else:
        print("Product not found.")


def purchase_stock():
    code = input("Enter product code to purchase (add to stock): ").strip()
    p = products.get(code)
    if not p:
        print("Product not found.")
        return

    qty_raw = input("Quantity purchased (positive integer): ").strip()
    try:
        qty = int(qty_raw)
        if qty <= 0:
            print("Quantity must be positive.")
            return
    except Exception:
        print("Invalid quantity. Aborting purchase.")
        return

    cost_each_raw = input(
        f"Cost price per unit (current {p['cost_price']}, enter 0 to keep): "
    ).strip()
    try:
        cost_each = float(cost_each_raw)
        if cost_each < 0:
            print("Negative cost ignored.")
            cost_each = 0.0
    except Exception:
        print("Invalid cost input; keeping current cost.")
        cost_each = 0.0

    if cost_each > 0:
        p["cost_price"] = round(cost_each, 2)
    p["stock"] += qty
    print(f"[Purchased] {qty} units added. New stock: {p['stock']}")


def sell_product():
    code = input("Enter product code to sell: ").strip()
    p = products.get(code)
    if not p:
        print("Product not found.")
        return
    if p["stock"] <= 0:
        print("No stock available to sell.")
        return

    # SELLING PRICE MUST BE SET
    sp = p.get("selling_price", 0)
    if not sp or sp <= 0:
        print("Selling price is not set for this product. Please update the product with a valid selling price before selling.")
        return

    qty_raw = input("Quantity to sell: ").strip()
    try:
        qty = int(qty_raw)
        if qty <= 0:
            print("Quantity must be positive.")
            return
    except Exception:
        print("Invalid quantity. Aborting sale.")
        return

    if qty > p["stock"]:
        print(f"Insufficient stock. Available: {p['stock']}")
        return

    gst_amount = calc_gst_amount(sp, p["gst_rate"])
    total_price_per_unit = sp + gst_amount
    total = round(total_price_per_unit * qty, 2)

    p["stock"] -= qty
    p["sold"] += qty
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[Sold] {qty} units of '{p['name']}' at ₹{sp} + GST ₹{gst_amount} per unit.")
    print(f"Total (incl. GST): ₹{total} — Time: {timestamp}")


# ---------- Calculations ----------
def calc_gst_amount(amount, gst_rate_percent):
    """Return GST amount for given amount and GST%."""
    return round((amount * gst_rate_percent) / 100.0, 2)


def view_product():
    code = input("Enter product code to view: ").strip()
    p = products.get(code)
    if not p:
        print("Product not found.")
        return
    print_product(code, p)


def print_product(code, p):
    sp = p.get("selling_price", 0)
    if not sp or sp <= 0:
        sp_display = "N/A (not set)"
        sp_note = "(not set)"
        gst_amt = "N/A"
    else:
        sp_display = f"₹{sp}"
        sp_note = "(stored)"
        gst_amt = f"₹{calc_gst_amount(sp, p['gst_rate'])}"

    print("-" * 40)
    print(f"Code: {code} | Name: {p['name']}")
    print(f"Cost price: ₹{p['cost_price']}")
    print(f"Selling price (before GST): {sp_display} {sp_note}")
    print(f"GST rate: {p['gst_rate']}%  | GST on 1 unit: {gst_amt}")
    print(f"Stock: {p['stock']}  | Sold: {p['sold']}")
    print("-" * 40)


def view_all_products():
    if not products:
        print("No products to show.")
        return
    print(f"Total products: {len(products)}")
    for code, p in products.items():
        print_product(code, p)


def product_profit_report():
    code = input("Enter product code for profit report (or 'all' for all products): ").strip()
    if code.lower() == "all":
        total_profit = 0.0
        for c, p in products.items():
            profit = compute_profit_for_product(p)
            print(f"{c} | {p['name']} | Profit so far: ₹{profit}")
            total_profit += profit
        print(f"Total profit for all products (so far): ₹{round(total_profit,2)}")
    else:
        p = products.get(code)
        if not p:
            print("Product not found.")
            return
        profit = compute_profit_for_product(p)
        print(f"Profit for {p['name']}: ₹{profit}")


def compute_profit_for_product(p):
    """
    Profit: (selling_price_before_gst - cost_price) * sold
    If selling_price not set, profit is treated as 0 (can't compute).
    """
    sp = p.get("selling_price", 0)
    if not sp or sp <= 0:
        return 0.0
    profit_per_unit = round(sp - p["cost_price"], 2)
    total_profit = round(profit_per_unit * p["sold"], 2)
    return total_profit


def find_price_details():
    code = input("Enter product code: ").strip()
    p = products.get(code)
    if not p:
        print("Product not found.")
        return
    sp = p.get("selling_price", 0)
    if not sp or sp <= 0:
        print("Selling price not set for this product. Please update it first.")
        return
    gst = calc_gst_amount(sp, p["gst_rate"])
    total = round(sp + gst, 2)
    print(f"Product: {p['name']}")
    print(f"Cost price: ₹{p['cost_price']}")
    print(f"Selling price (before GST): ₹{sp}")
    print(f"GST (@{p['gst_rate']}%): ₹{gst}")
    print(f"Total price (incl GST): ₹{total}")


# ---------- Menu ----------
def print_menu():
    print("\n=== GST Billing & Inventory System ===")
    print("1. Add product")
    print("2. Update product")
    print("3. Delete product")
    print("4. Purchase stock (add)")
    print("5. Sell product")
    print("6. View product details")
    print("7. View all products")
    print("8. Find price & GST for a product")
    print("9. Profit report")
    print("0. Exit")


def main():
    # In-memory only: no load/save steps
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            purchase_stock()
        elif choice == "5":
            sell_product()
        elif choice == "6":
            view_product()
        elif choice == "7":
            view_all_products()
        elif choice == "8":
            find_price_details()
        elif choice == "9":
            product_profit_report()
        elif choice == "0":
            print("Exiting... Goodbye! :)")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
