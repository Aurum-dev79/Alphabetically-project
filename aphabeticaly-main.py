
import funtions_name


selector = None

while selector != '5': 
   
   print("   Welcome to alphabeticaly\nChose one option\n1)Add name\n2)Delete name\n3)Edit name\n4)Sort name\n5)salir")
   selector = input("chose: ")
   if selector == '1':
      aux = str(input("write the name to save:"))
      funtions_name.add_name(aux)

   elif selector == '2':
      aux = str(input("write the name to delete: "))
      funtions_name.delete_name(aux)
   
   elif selector == '3':   
      aux = str(input("write the name to edit: "))
      funtions_name.edit_name(aux)

   elif selector == '4':
      funtions_name.sort_name()

  



    



