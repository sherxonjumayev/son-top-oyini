#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:46:09 2022

@author: sezar
"""



# from random import sample as s

# # print("'SON-TOP' o'yiniga xush kelibsiz?")

# start =input("\nTayyormisiz? O'yinni boshladik. boshlash uchun biror tugmani bosing:")
# komp = s(range(1,11),1).pop()  
# user = int(input("1 dan 10 gacha son o'yladim. Topishga harakat qilib ko'ring. \n>>>"))

# while True:
#     urinish = 1
#     if komp > user:
#           user = int(input("\nXato. Men o'ylagan son bundan kattaroq. Yana urinib ko'ring.\n>>>"))
#     if komp<user:
#           user =int(input("\nXato. Men o'ylagan son bundan kichikroq. Yana urinib ko'ring.\n>>>"))
#     if user == komp:
#           break
#     urinish += 1
# print(f"TABRIK. Men {komp} sonini o'ylagan edim. Siz {urinish} urunishda topdingiz")   
   
# # sizning navbatingiz    
# print("\n1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.\n")
# start = input("Son o'ylagan bo'lsangiz istalgan tugmani bosing:")
# komp2 = s(range(1,11),1).pop()

# javob = input(f"\nSiz {komp2} sonini o'yladingiz:to'g'ri (t), men o'ylagan son bundan kattaroq(+),"
#               "men o'ylagan son bundan kichikroq(-) bo'lsa qavs ichidagi belgini kiriting:\n>>>")
# while True:
#     urinish2 = 1
#     if javob == '+':
#         komp2 = s(range(komp2,11), 1).pop()
#         javob = input(f"\nSiz {komp2} sonini o'yladingiz:to'g'ri (t), men o'ylagan son bundan kattaroq(+),"
#                       "men o'ylagan son bundan kichikroq(-) bo'lsa qavs ichidagi belgini kiriting:\n>>>")
#     if javob == '-':
#         komp2 = s(range(1,komp2), 1).pop()
#         javob = input(f"\nSiz {komp2} sonini o'yladingiz:to'g'ri (t), men o'ylagan son bundan kattaroq(+),"
#                       "men o'ylagan son bundan kichikroq(-) bo'lsa qavs ichidagi belgini kiriting:\n>>>")
#     if javob == 't' or'T':
#         break
#     urinish2 +=1
# print(f"Men {urinish2} urunishda topdim.")

# if urinish == urinish2:
#     print(f"Ikkalamiz {urinish} urunishda topdik. O'yin durrang bo'ldi")
# if urinish< urinish2:
#     print(f"Siz {urinish} urunishda topdingiz va yutdingiz")
# if urinish > urinish2:
#     print(f"MEn {urinish} urunishda topdim va yutdim")

# =============================================================================
# 2-urinish
# =============================================================================
def son_top(son):
    import random as r
    print('Keling o\'ylagan sonni topish o\'ynaymiz')

#1-qism. Kompyuter    
    user_son = int(input("\n1 dan 10 gacha son o'yladim, topa olasizmi?\n>>"))
    pc_son = r.choice(list(range(1,son)))
    while True:
        n = 1
        if pc_son> user_son:
            user_son = int(input("Xato, men o'ylagan son bundan kattaroq. Yana urinib ko'ring\n>>"))
        if pc_son < user_son:
            user_son = int(input("Xato, men oylagan son bundan kichikroq. Yana urinib ko'ring\n>>"))
        if pc_son == user_son:
            break
    print(f"TABRIK! Siz to'g'ri topdingiz. Men {pc_son} sonini o'ylagan edim."
              f"Siz {n} ta tahmin bilan topdingiz.")
        
son_top(10)

