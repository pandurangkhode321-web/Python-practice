# def sum_digit(b):
#     n=b                 By using function finding the sum of digit 
#     sum=0
#     while n>0:
#         c=n%10
#         sum+=c
#         n=n//10
#     return sum
# print(sum_digit(3456))

# def second_largest(my_list):
#     l=0
#     sl=0
#     for i in my_list:          prints second largest number with two distinct number in  a list
#         if i>l:
#             sl=l
#             l=i
#         elif i>sl and l!=i:
#             sl=i
#     return sl
# print(second_largest([10,5,20,20,8]))


# def prime_num(My_list):
#     New_list=[]                   Extracting  prime number from My_list appending to New_list
#     n=2                             By uing defining function 
#     for i in My_list:
#         is_prime=True
#         for j in range(2,i):
#             if i%j==0:
#                 is_prime=False
#         if is_prime:
#             New_list.append(i)
#     return New_list
# print(prime_num([2,3,4,5,6,7,8,9]))      







