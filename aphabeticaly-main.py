
import funtions_name
import os


selector = None

while selector != '5': 
   
   print("   Welcome to alphabeticaly\nChose one option\n1)Add name\n2)Delete name\n3)Edit name\n4)Sort name\n5)salir")
   selector = input("chose: ")
   os.system('cls')
   if selector == '1':
      aux = str(input("write the name to save:"))
      cent = funtions_name.add_name(aux)
      if cent == True:
         print("The name has been saved successfully")
      print("Press any buttom to cotinue")
      input()      
      os.system('cls')

   elif selector == '2':
      aux = str(input("write the name to delete: "))
      cent = funtions_name.delete_name(aux)
      if cent == True:
         print("The name has been deleted")
      print("Press any buttom to cotinue")
      input()      
      os.system('cls')
   
   elif selector == '3':   
      aux = str(input("write the name to edit: "))
      cent = funtions_name.edit_name(aux)
      if cent == True:
         print("the name has been edited")
      print("Press any buttom to cotinue")
      input()      
      os.system('cls')

   elif selector == '4':
      cent = funtions_name.sort_name()
      if cent == True:
         print("the name has been sorted")
      print("Press any buttom to cotinue")
      input()      
      os.system('cls')

   else:
      print("See you later")
  






    



