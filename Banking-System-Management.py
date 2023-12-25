import random

compte={56:200,20:360}    #numc,soldec
client={1:"566",2:"836"}  #numcl,mpc
clientcompte={1:56,2:20}   #numcl,numc


print("Are you Agent or clien ?")
Q=int(input('if you are a Client enter 1.\n But if you are an agent enter 2 :  '))

if Q==2:
   print("hello agent : ")
   print("what do you want : ")
   print("1 : add an account .")
   print("2 : delet an account .")
   print("chose 1 ,2 ")
   x = int(input())
   if x==1:
      def ajouter_client():
         numcl = int(input("le numero de client: "))
         a = (random.randint(0,100))
         numc = numcl*100+a

         mpc = input ("le code : ")
         soldec = input ("le solde : ")

         compte.update({numc : soldec})
         client.update({numcl : mpc})
         clientcompte.update({numcl : numc})
      ajouter_client()

   elif x==2:
      def supprimerClient():
         C = int(input("le num de compt que vous voulez supprimer: "))
         del compte[C]
         for key,value in clientcompte.items():
           if C == value:
              x = key
         del client[x]
         del clientcompte[x]
      
      print (compte)
      print (client)
      print (clientcompte)
      supprimerClient()
      print (compte)
      print (client)
      print (clientcompte)

   else:
      print("Choix invalide !!")

elif Q==1:
   print("hello client : ")
   print("what do you want : ")
   print("1 : edit the pass word .")
   print("2 : show  the balance .")
   print("3 : Depose money .")
   print("4 : retire money .")
   print("chose 1 ,2 ,3 ,4 :")
   x=int(input())
   if x == 1 :
      def modifier_mpc():
         numcl = int(input(" le numero de client : "))
         Mpo=input("enter the old password  : ")
         mpc = input("enter the new password : ")
         client[numcl] = mpc
         print("the password is changed succelfuly .")
      modifier_mpc()
      print(client)


   elif x==2 :
      def showbalance():
         numc = int(input("le numero de compte :"))
         print('your balance is : ')
         for key,value in compte.items():
            if numc == key:  
               solde = "10000 dh"
            compte [numc] = solde
         
         
      showbalance()

   elif x==3 :
      def deposer_argent():
         numc = int(input("le numero de compte :"))
         soldec = int(input("la somme de l'argent que tu veux ajoute :"))
         for key,value in compte.items():
            if numc == key:        
               s = value + soldec
         compte [numc] = s

      deposer_argent()
      print(compte)


   elif x==4:
      def retire_argent():
         numc = int(input("donner moi le numero de compte :"))
         soldec = int(input("l'argent ajoute :"))
         for key,value in compte.items():
            if numc == key:        
               d = value - soldec
         compte [numc] = d

      retire_argent()
      print(compte)
   else:
     print("Choix invalide !!")

else:
   print("Choix invalide !!")
