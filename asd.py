# ==========open  a file ===============================
import numpy as np
# ========file handling==================================
# f=open("file.txt","r")
# print(f.read())
# ============close the file===============
# f.close()
# print(f.read())
# # ============Another method to open file =================
# with open("file.txt","r") as f:
#     print(f.read())
# # ============readline not complete  paragraph============
# with open("file.txt","r") as f:
#     print(f.readline())
#     print(f.readline())

# =========writting a file with the append method ===============
# with open("file.txt","a") as f:
#     f.write("this is new line added to the file. \n")
#========================================================
with open("file.txt") as f:
    print(f.read())
# =============overwitting the file with the "w" method =============
# with open("file.txt","w") as f:
#     f.write("oops! i have overwritingthe whole file.\n")
# # ================reading the file after the file after appending================
# with open ("file.txt","r") as f:
#     print(f.read())
# # ========creat a new file using the "x" method=====================
# f=open("filehangling.txt","x")
    

