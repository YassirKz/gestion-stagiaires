rep=1
while rep<=3 :
    login=input("Login :")
    passe =input("Password :")
    rep+=1
    with open("comptes.pas", "r") as f:
        l = f.readlines()
    lignes = tuple(l)
    for line in lignes:
        d=line.split(";")

        log=d[0]
        p1=d[1]

        if(login==log and passe==p1):
            print("bienvenue .....")
            exit()
    else :
        print("login ou mot de passe incorect !!")

else :
    print("contacter admin !!")

