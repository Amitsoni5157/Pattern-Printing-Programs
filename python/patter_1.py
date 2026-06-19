# print("Square Star Pattern")
#     # ****
#     # ****
#     # ****
#     # ****
# for i in range(4):
    
#         for j in range(4):
#             print("*", end="")

#         print()

# print("Hollow Square Star Pattern !");
# # /*  
# #     ****
# #     *  *
# #     *  *
# #     ****
# # */
# size = 4

# for i in range(size):    
#         for j in range(size):
#             if i == 0 or i == size -1 or j == 0 or j == size -1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
        
   


#  print("Rhombus Star Pattern")
 #         //    ****
#         //     ****
#         //      ****
#         //       ****
size = 4

for i in range(size):
    
    for space in range(i):
        print(" ", end="")

    for k in range(size):
        print("*", end="")

    print("")