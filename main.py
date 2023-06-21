loan_amount = 1000
apr = 0.05
for i in range(10):
  loan_amount +=(loan_amount*apr)
  print("Year", i+1, "is", round(loan_amount,2))