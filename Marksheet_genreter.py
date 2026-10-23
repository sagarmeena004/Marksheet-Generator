# Marksheet genreter (With the help of Net legent)

Name = input("Enter the name :")
enrol = input("Enter the enrol :")
roll = input("Enter the roll No :")
sem = input("Enter the Semester :")
sec = input("Enter the section :")
scol = input("Enter the scollor no :")

hindi = int(input("Enter the Number Hindi :"))
english = int(input("Enter the Number English :"))
physics = int(input("Enter the Number Physics:"))
chemistry = int(input("Enter the Number Chemistry :"))
biology = int(input("Enter the Number  Biology:"))

phy_pri = int(input("Enter the Number phy_p:"))

chem_pri = int(input("Enter the Number che_p:"))

Bio_pri = int(input("Enter the Number Bio_p:"))


print("\t\t\t\t\t\t\tJNCT PROFESSIONAL UNIVERSITY BHOPAL")

print("\t\t\t\t\t\t Marksheet & Progress report of MID SEM TEST-2")

print("\t\t\t\t\t\t\t\t\t  BCA-AIML")


print("\t\t\t\t\t\t\t\t\tDEC-2026")

print("-------------------------------------------------------------------------------------------------------------------------------------------------------")

print("NAME :\t\t",Name,"\t\t\t\t\t\t\t\t\t\t\t ENROLLMENT NO. :\t",enrol)

print("ROLL NO. :\t",roll,"\t\t\t\t\t\t\t\t\t\t\t\t SEMESTER :\t\t",sem)

print("SECTION :\t",sec,"\t\t\t\t\t\t\t\t\t\t\t\t SCOLLOR NO. :\t\t",scol)

print("-------------------------------------------------------------------------------------------------------------------------------------------------------")

print("SUBJECT\t\t\t","TOTAL THEORY\t\t","TOTAL PRACTICAL\t\t","THEORY\t\t","INTERNAL PRACTICAL\t\t","TOTAL\t\t\t","Grade\t\t")

if hindi > 28:
    print("HINDI\t\t\t\t","100\t\t\t","--\t\t\t",hindi,"\t\t\t","--\t\t\t",hindi,"\t\t\t","PASS")
else:
    print("HINDI\t\t\t\t","100\t\t\t","--\t\t\t",hindi,"\t\t\t","--\t\t\t",hindi,"\t\t\t","FAIL")

if english > 28:
    print("ENGLISH\t\t\t\t","100\t\t\t","--\t\t\t",english,"\t\t\t","--\t\t\t",english,"\t\t\t","PASS")
else:
        print("ENGLISH\t\t\t\t","100\t\t\t","--\t\t\t",english,"\t\t\t","--\t\t\t",english,"\t\t\t","FAIL")


if physics + phy_pri > 33:
    print("PHYSICS\t\t\t\t","70\t\t\t","30\t\t\t",physics,"\t\t\t",phy_pri,"\t\t\t",physics + phy_pri,"\t\t\t","PASS")
else :
    print("PHYSICS\t\t\t\t","70\t\t\t","30\t\t\t",physics,"\t\t\t",phy_pri,"\t\t\t",physics + phy_pri,"\t\t\t","FAIL")

if chemistry + chem_pri > 33:
    print("CHEMISTRY\t\t\t","70\t\t\t","30\t\t\t",chemistry,"\t\t\t",chem_pri,"\t\t\t",chemistry + chem_pri,"\t\t\t","PASS")
else:
    print("CHEMISTRY\t\t\t","70\t\t\t","30\t\t\t",chemistry,"\t\t\t",chem_pri,"\t\t\t",chemistry + chem_pri,"\t\t\t","FAIL")

if biology + Bio_pri > 33:
    print("BIOLOGY\t\t\t\t","70\t\t\t","30\t\t\t",biology,"\t\t\t",Bio_pri,"\t\t\t",biology + Bio_pri,"\t\t\t","PASS")
else:
    print("BIOLOGY\t\t\t\t","70\t\t\t","30\t\t\t",biology,"\t\t\t",Bio_pri,"\t\t\t",biology + Bio_pri,"\t\t\t","FAIL")

