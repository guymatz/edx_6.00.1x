#!/usr/bin/env python

def calc_remaining_balance(bal, payment, apr):
  for n in range(12):
    bal -= payment
    bal = bal * (1 + apr/12)
    print("Payment %i, Bal = %0.2f : Payment = %0.2f" % (n, bal, payment) )

  print
  return bal

def main(bal, apr):

  remaining_balance = bal
  payment = 0
  lo_payment = bal / 12
  hi_payment = remaining_balance * (1 + apr)
  ctr = 0

  while abs(remaining_balance) > .01:
    payment = ( hi_payment + lo_payment ) / 2
    print("lo = %0.2f, hi = %0.2f" % ( lo_payment  , hi_payment ) )
    ctr += 1
    remaining_balance = calc_remaining_balance(bal, payment, apr)
    if remaining_balance > 0:
      lo_payment = payment
    else:
      hi_payment = payment

  print("Checked %i times" % ctr)
  print("Lowest Payment: %0.2f" % payment)
    
balance=999999
annualInterestRate = 0.18
main(balance, annualInterestRate)
