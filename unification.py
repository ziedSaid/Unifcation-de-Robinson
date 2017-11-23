

def isAtom(e):
    return len(e)==1



# modifier la chaine entre a une list 
def expression(e):
    # list contient l'expression 
  
    listofelements=[]
 
    expr=e[e.find("(")+1:e.rfind(")")]

  
    while not expr=="":
       
        if not ',' in expr:
            listofelements.append(expr)
            expr=""
        else:
        
            if not '(' in expr[:expr.find(',')]:
                listofelements.append(expr[:expr.find(',')])
                expr=expr[expr.find(',')+1:]
            else:
               
                begin=0
                end=0
                nb_of_opening_par=0
                nb_of_closing_par=0
                end_of_elements=False
                i=0
                while not end_of_elements:
                    c=expr[i]
                    if c=='(':
                        if begin==0:
                            begin=i
                        nb_of_opening_par+=1
                    else:
                        if c==')':
                            nb_of_closing_par+=1
                            if nb_of_opening_par==nb_of_closing_par and nb_of_opening_par>0:
                                end=i
                                end_of_elements=True
                                i=0
                    i+=1
                listofelements.append(expr[begin-1:end+1])
              
                if end==len(expr)-1:
                    expr=""
                else:
                    expr=expr[end+2:]
    return  listofelements


# unifier deux  expressions 
def unify(expr1,expr2):
 
    if isAtom(expr1) or isAtom(expr2):
        return unifyAtoms(expr1,expr2)

    f1=expr1[0]
 
    del expr1[0]
    t1=expr1

    
    f2=expr2[0]
  
    del expr2[0]
    t2=expr2
    
    e1=[f1]
    e2=[f2]
  
    z1=unify(e1,e2)

    
    if z1=="Echec":
        return "Echec"

    #apply substitution on the rest of expr1 and expr2
    g1=substitute(t1,z1)
    g2=substitute(t2,z1)
    #unify the rest
    z2=unify(g1,g2)
    if z2=="Echec":
        return "Echec"
    return z1+" "+z2


#substitution of t1 by the unifier z1
def substitute(t1,z1):
    chg=z1.strip().split()
    tmp=[]
    for i in chg:
        tmp.append(i.split('/'))
    b=[]
    for i in tmp:
        for j in i:
            b.append(j)

    if not z1=="":
        for i in range(0,len(t1)):
            for j in range(0,len(b),2):
                t1[i]=t1[i].replace(b[j],b[j+1])
    return t1



#unify 2 atoms
def unifyAtoms(ex1,ex2):
    e1=ex1[0]
    e2=ex2[0]
    
    if e1==e2:
        return ""
    
    if e1[0]=='?':
       
        if e1 in e2:
            return "Echec"
        
        return e1+"/"+e2
  
    if e2[0]=='?':
        return e2+"/"+e1
   
    if (('(' in e1) and ('(' in e2)):
        l1=expression(e1)
        l2=expression(e2)
        return unify(l1,l2)
  
    return "Echec"







#------- test & trace ---------
def readTC(filename):
    expressions=[]
    file=open(filename,"r")
    for testcase in file.read().split('\n'):
        expressions.append(testcase)
    return expressions
tracefile=open("trace.txt","w")
testcases=readTC("cases.txt")
i=1
for testcase in testcases:
   

    exprs=testcase.split(':')
    if( len(exprs)==1):
        break
    tracefile.write("_______________test_______________N°"+str(i)+"\n")
    print("______________________test__________________N°",i)
    expr1=exprs[0]
    expr2=exprs[1]
    tracefile.write("Expression 1: "+expr1+"\n")
    print("Expression1   => ",expr1)
    tracefile.write("Expression 2: "+expr2+"\n")
    print("Expression2   =>",expr2)
    print("__________________________________________")
    print("**************Unification*****************")
    print("___________________________________________")
    tracefile.write("------- UNIFICATION -------- \n")
    tracefile.write(unify(expression(expr1),expression(expr2)))
    print("=========List==========>",expression(expr1))
    print(unify(expression(expr1),expression(expr2)))
    print("")
   
    tracefile.write("\n\n")
    i+=1
    

