def calculate_tax(income, tax_rate):
    # Intentional bug: if tax_rate is 0, this will crash
    return income / tax_rate

if __name__ == "__main__":
    result = calculate_tax(50000, 0)
    print(f"Tax calculated: {result}")
