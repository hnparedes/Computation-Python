# tax.no_function.py

def get_inputs():
    amount = float(input('What is the price: '))
    extra = float(input('What is the tax rate?: '))
    return calculate_price_with_tax(amount, extra)


def calculate_price_with_tax(price, tax):
    return price * (100 + tax) / 100


done = False
while not done:
    sentinel = str.upper(input(f'Enter Q for quit or any other key to compute tax: '))
    if sentinel == 'Q':
        done = True
        print(sentinel, done)
        continue
    else:
        print("Compute Tax")
        print(f'The calculated price is ', get_inputs())
