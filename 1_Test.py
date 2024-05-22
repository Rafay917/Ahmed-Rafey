def reverse_and_print_digits(num):
    if num < 0: 
        num = abs(num)
         
    while num > 0:
        digit = num % 10  
        print(digit)      
        num = num // 10   
reverse_and_print_digits(num=int(input("Enter the number : ")))