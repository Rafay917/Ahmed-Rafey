 def reverse_number(num):
     if num < 0:
         num = abs(num)
     while num > 0 :
         digit= num % 10
         print(digit)
         num = num //10
 reverse_number(int(input("Enter the Number : ")))
