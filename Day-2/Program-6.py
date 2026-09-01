price = 2000
discount = 15
tax = 18

discount_amount = price * discount / 100
discounted_price = price - discount_amount

tax_amount = discounted_price * tax / 100
final_price = discounted_price + tax_amount

print("Final price =", final_price)