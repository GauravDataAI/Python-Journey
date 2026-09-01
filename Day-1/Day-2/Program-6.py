price = 1000
discount = 10
tax = 18

discount_amount = price * discount / 100
price_after_discount = price - discount_amount

tax_amount = price_after_discount * tax / 100
final_price = price_after_discount + tax_amount

print("Final Price:", final_price)