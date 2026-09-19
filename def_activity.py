# def is used to define a function - a reusable block of code that does a specific task
# You write it once and you can call it anytime with different values

def buy_load(amount):
    """Calculates discount for GCash Buy Load"""
    if amount >= 100:
        discount = amount * 0.10  # 10% discount
    elif amount >= 50:
        discount = amount * 0.05  # 5% discount
    else:
        discount = 0  # No discount

    final_price = amount - discount

    if discount > 0:
        print(f"Discount: {discount}. Pay: {final_price}")
    else:
        print(f"No discount. Pay: {final_price}")

# --- Test ---
buy_load(30)
buy_load(60)
buy_load(150)