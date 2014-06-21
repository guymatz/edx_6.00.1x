#!/usr/bin/env python

def calc_remaining_balance(bal, payment, apr):
  for n in range(12):
    bal -= payment
    bal = bal * (1 + apr/12)
    #print("Payment %i, Bal = %0.2f : Payment = %0.2f" % (n, bal, payment) )

  #print
  return bal

def main(bal, apr):

  remaining_balance = bal
  payment = 0

  while remaining_balance > 0:
    remaining_balance = calc_remaining_balance(bal, payment, apr)
    if remaining_balance > 0:
      payment += 10

  print("Lowest Payment: %0.2f" % payment)
    
#balance=3926
#annualInterestRate = 0.2
main(balance, annualInterestRate)
