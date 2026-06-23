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
        
   

# ------------------------------------------------------
#   print("Rhombus Star Pattern")
#  #         //    ****
# #         //      ****
# #         //       ****
# #         //        ****
# size = 4

# for i in range(size):
    
#     for space in range(i):
#         print(" ", end="")

#     for k in range(size):
#         print("*", end="")

#     print("")
# -----------------------------------------------------------
# print("Rectangle Star Pattern")
# row = 4
# column = 6

# for row in range(4):
#     for column in range(6):
#         print("*",end="")
#     print("")
# ------------------------------------------------

# print("Mirrored Rhombus Star Pattern")
#      ****
#     ****
#    ****
#   ****

# size = 4

# for i in range(size):
#     for j in range(size, i, -1):
#       print(" ",end="")

#     for k in range(size,0,-1):
#         print("*", end="")
    
    # print("")
# ----------------------------------------
# print("Triangle Star Pattern")

# # *
# # **
# # ***
# # ****
# size = 4
# for i in range(size):
#     for j in range(i+1):
#        print("*",end="")
#     print("")
# -----------------------------
# //       *
# //      ***
# //     *****
# //    *******
# print("Pyramid Star Pattern")

# row = 4
# for i in range(row):
#     for space in range(row - i -1):
#          print(" ", end="")

#     for star in range(2 * i +1):
#          print("*",end=(""))  

    # print("")

# //       *
# //      ***
# //     *****
# //    *******
# print("Rev Pyramid Star Pattern")

# row_ = 4
# for i in range(row_, 0, -1):
#     for space in range(row_ - i):
#          print(" ", end="")

#     for star in range(2 * i -1):
#          print("*",end=(""))  

#     print("")
# ---------------------------------------------
#     *
#    * *
#   *   *
#  *******
print(" Hollow  Pyramid  Star Pattern");

row = 4

row = 4
for i in range(row):
    for space in range(row - i -1):
         print(" ", end="")

    for star in range(2 * i +1):
         if star == 0 or star == 2* i or i == row -1:
            print("*",end="")
         else:
            print(" ",end=(""))  

    print("")