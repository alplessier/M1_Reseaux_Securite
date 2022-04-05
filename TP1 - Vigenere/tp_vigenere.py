from math import *

# String sans char speciaux
from cgitb import text


def lowerAndChar(var):
   var = var.lower()

   for i in var:
      if((ord(i) < 97) or ord(i) > 122):
         var = var.replace(i,"")
   
   return var

# Vigenere 2 char
def vigenere(a,b):
   return chr(((ord(a)-97 + ord(b)-97)%26)+97)

# Vigenre 2 mots
def codeVigenere(s1,s2):

   res = []

   if(len(s1) <= len(s2)):
      for i in range(len(s1)):
         res.append(vigenere(s1[i],s2[i]))
   else:
      for i in range(len(s1)):
         res.append(vigenere(s1[i],s2[(i)%len(s2)]))

   return "".join(res)
      

def partie1():

   res = []
   # Texte -> Texte lowercase et sans char speciaux
   txt = input("Entrez un texte à chiffrer : ")
   cle = input("Entrez une clé de chiffrement : ")
   txt_LC = lowerAndChar(txt)
   StrTxt = "".join(txt_LC)
   res.append(StrTxt)

   cle_LC = lowerAndChar(cle)
   StrCle = "".join(cle_LC)
   res.append(StrCle)

   print("Le texte :",txt_LC," avec le clé :",cle_LC," donne le résultat :",codeVigenere(txt_LC,cle_LC))
   
   StrVig = "".join(codeVigenere(txt_LC,cle_LC))
   res.append(StrVig)
   print()
   return res


############ LONGUEUR CLE ############

#Prends une sequence et un mot et renvoie l'indice d'apparition de la sequence dans le mot
def indiceOccurence(occ,mot):
   tab = []
   for i in range(len(mot)+1):
      for j in range(len(mot)+1):
         if(mot[i:j] == occ):
            tab.append(i)
   return tab


# PGCD de a et b
def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)


#Etablie la liste de toutes les occurences possibles de k+ chr présent plus d'une fois
def KeyLenDistances(s,k):

   if(len(s)<3):
      print("Longueur de la clé trop petite (infèrieur à 3 !)")
      return 

   # res prends toutes les combinaisons de k char possibles
   res = []
 
   for i in range (len(s)-k+1):
      for j in range(k+i,len(s)+1):
         res.append(s[i:j])

   res = list(set(res))

   # dico prends toutes les combinaisons et leur nombre d'apparition
   dico ={}

   for i in range(len(res)):
      if(s.count(res[i])>1):
         dico[res[i]] = s.count(res[i])

   # Ici, le dico est pret
   #10% de la liste à l'unité superieur, comme ca on est sur de supprimer 1 occurence minimum
   ten_percent = ceil(len(dico)/10)
 
   # Trie le dictionnaire
   dicoSorted = sorted(dico.items(), key=lambda t: t[1])
   
   #Retire les 10% occurence plus petites du dicitonnaire
   for i in range(ten_percent):
      del dico[dicoSorted[i][0]]

   print("Pour le mot :\n",s)
   print()
   # Trie le dictionnaire
   dicoSorted = sorted(dico.items(), key=lambda t: t[1])
   print("Occurences après amelioration (10%) :")
   print(dicoSorted)
   
   # ind prend les index des sequences redondantes
   ind = []

   for d in dico:
      ind.append(indiceOccurence(d,s))

   # dis prend les distances de toutes les sequances redondantes
   dis = []

   for i in range(len(ind)):
      for j in range(len(ind[i])-1):
         dis.append(ind[i][j+1] - ind[i][j])

   fin = dis[0]

   # Calcul du PGCD de toutes les distances
   for c in dis[1::]:
      fin = pgcd(fin , c)

   return fin


def partie2_1():
   print("============ LONGUEUR CLEe ============")
   print("La clé a pour longueur :",KeyLenDistances(lowerAndChar("zmlivwrunnwqguecksryezysafeihdrxemdozmli"),3))

############ TEST DE FRIEDMAN ############

def friedman(texte):
   res = 0

   for i in range(26):
      tmp = 0
      for j in range(len(texte)):
         if(texte[j] == chr(97+i)): 
            tmp +=1
         
      res += (tmp*(tmp-1))/((len(texte)*(len(texte)-1)))


   return res


def keyLen(texte):
   res = (0.067-0.0385)/(friedman(texte)-0.0385)

   # Si la valeur decimale est >0.5, unité+1
   if(res%1 >=0.5):
      return int(res)+1
   else:
      return int(res)

def partie2_2():
   print("============ TEST DE FRIEDMAN ============")
   print("Friedman sur texte anglais :",friedman(lowerAndChar("The U.S. Embassy recognizes that knowledge of the English language offers opportunities to improve job prospects for Serbia’s citizens, expand access to information and knowledge, and promote critical thinking and media literacy.  Proposals should use English to address problems or challenges faced by your community, such as brain drain, limited job opportunities, or the spread of disinformation.  Proposals may also utilize English as a bridge for increased communication and cooperation among neighbors within the Western Balkans, between citizens of Serbia and the United States, or between people from Serbia and EU member states.Grant activities may take any number of forms, including English language camps, academic competitions, cross-border exchanges, conferences, workshops, courses, exhibits, app development, hackathons, online projects, simulations, role-playing activities, performances, or other activities.Grant activities may take any number of forms, including English language camps, academic competitions, cross-border exchanges, conferences, workshops, courses, exhibits, app development, hackathons, online projects, simulations, role-playing activities, performances, or other activities.The Public Diplomacy Section (PDS) of the U.S. Embassy in Belgrade announces an open competition for individuals and organizations from Serbia or the U.S. to submit applications for the English Language Small Grants Program. Please check for information on other PAS funding opportunities here.Strengthen critical thinking and/or media literacy skills of students through English language activities; prepare students for participation in international academic competitions conducted in English, e.g., Model UN (Model United Nations), moot court, etc.; or explain American society, culture, and values to students through English language activities.Improve Serbian officials’ English language skills to communicate with EU counterparts and accelerate Serbia’s progress toward EU membership and western integration.Establish or strengthen connections among English language teaching professionals and institutions from countries of the Western Balkans to promote cooperation in strengthening English language instruction within the region.nform and educate audiences in Serbia about historical and cultural Serbian-U.S. ties, common attitudes and values, cooperation in different sectors (economic, political, security, health, science), and the intersection of national interests.Help Serbian civil society organizations engage with EU counterparts to make progress toward EU membership and western integration, including in the areas of human rights protection, media freedom, environmental issues, rule of law, combating corruption, etc.")))
   print("Longueur de la clé par le test de Friedman :",keyLen(lowerAndChar("Ysi O.J. Jxfujxj vyttrrcqjd xbry vrinqphav tq xbv Jykfzxs puelfeav tqjyix ztjfweyhzytim kt tqjitgi dfg avijupgnj kzv Mvwmmu’j htxcqjyw, youlrx rhnimj yz mhwtcquknzr uei vrinqphav, fyh jitxsnv hcmnzhlp nynyocel lrx djomu cneilrhj.  Tlfuzwucx dlilqo ymv Jykfzxs xi riovyjx avisqpqm fw nlucqpravx qewvi mc sfzc gidrfrckd, dywy fd flrny hlrny, pcdneix atm sjgtcxoenemyj, tc xbv xavyri zj xzxtrzfwxenzty.  Tlfuzwucx xes rqds oknwmtv Jykfzxs em r gcmxxj qsl zsnvyrxph wfrxyhzhlxcfs lrx ttztyifemie fxshx spmaygzvm nnelce ysi Qvxeile Glpersd, fykbpih tnemtvsd sz Jjcfcr fyh nyj Frckjo Wnrypw, ii gpxqvjy tyfuwi zitx Wyigte uei PY gvrmil jylxyj.Lcehk fnxcmnemyj rlc nrpp ehp sfqvvw zj zfwxw, cehwyxzsr Ihxqtwb cfykorlp gudud, ewripqct hzqjvytxcfsd, glfxd-fiiipv yohsehxjd, giekpvyehpw, qfwvwbfud, gilwdim, vcsmvzyd, ejg ipzyctaqyey, sewbfeliex, zrfzsp tlfopgnj, xtqocfemiex, csfv-uweszsr ewkngmnzjd, tyikzvgrsnim, fw zxbvw lgnzatxcvx.Rvuey lgnzatxcvx xes kfvi ued yygsjc sz wtcqm, zsnpounyk Yelwmmy qlralfri wrraw, utfoigzh nsggjemnztyw, witdw-vfwoil vcnluelpw, wfsqilvsnim, ntcomytaw, wfzcwyj, jilcsnew, ugu oipvqztgvse, lutplxbfsd, shcnyi jituiwkx, dmglqlxcfsd, vicj-apupnyk utytzcknpw, jvwqsldfygyj, tc snyjc ewkngmnzjd.Xbv Ufffzh Omjctxewp Xpgnzty (TXJ) tq xbv Z.D. Igsfdws zs Mifxwlhy rsysoehpw ue taih ttxtyknemie kzv ceitzcuzlpm rso slxfymtrytshj kcsg Jjcfcr tc xbv Z.D. xi jzmqck fatfzhlxcfsd jii ysi Yelwmmy Qlralfri Mdfwp Aifyxm Gwzklrr. Apyrxp gbvhv jii nyjiirlxcfs zr ikmpv JRX qyhunyk iguzvnlstxcvx silv.Xevyelelye hcmnzhlp nynyocel lrx/fw xixzf wmnvwlgs jptpfj tq wnliprnj ysvills Ihxqtwb cfykorlp ewkngmnzjd; tlvulvy jyfhyeyd jii ulvnzhttuknzr ce nyxyislxcfslp utfoigzh nsggjemnztyw wfsoywkjo mh Vsrpcjm, p.k., Gfipp OE (Rzhyc Zymnvi Yenztyw), gfte gilwe, int.; tc irgqlmh Rrpvctfy witnpxs, tzwxoij, lrx mfwyyj yz wnliprnj ysvills Ihxqtwb cfykorlp ewkngmnzjd.Mggwzzy Jjcfcrs zjzzhtefj’ Jykfzxs puelfeav xvmfcx es wfrxyhzhlxy nnel YL hzyhkjctuiyd ehu fngycjcenv Xpvvzf’d tlflcimj yzauii PY gvrmiljmtt uei himkjcr ceypklrytsh.Vxeevcndl ii xevyelelye hzrhvhemiex lqiel Pracndl frsryuxj eiutmtra gwzjyjxtshrqd ehu nywnzyfxcfsd jlfr nsoeycmyj tq xbv Bpwnvwy Fucplrm kt avidtei wftailrytsh zs dxlvsrxbvstra Vsrpcjm wehxzlky zsdxllhemie btxbzs ely ijrmie.sqsld fyh yuznenv ffhcvsnim zs Dilsnl evfze lcjyzvctfw ehu hfpnlwlp Mvwmmue-Z.D. xcvx, nsgdty enkneyxvx lrx mfwyyj, hzsjvwlxcfs tr xzkqilvse wytyzvm (vhzridnn, ticnemwrq, diwlwtxs, yjlpny, xnmyehp), ehu ysi ceypvmvhemie tq ruknzruc nyxyijdxm.Yjwt Mvwmmue htzcc xzgcvyj slxfymtrytshj jykuxj hmny JF gilseilgfcxm kt xeev ucsaijdw nfblvx VZ xigsjcwbzu lrx njdxyis trnvlcenzty, mhtqfhcel tr nyj lvyrx zj blrlr lzlsxm gwzxytytsh, djomu wwpixfr, prpzwzrgvseef zxdyyj, wfpy fk weq, ttxfuknyk wfwcyjknzr, ykh.")))
   
############ ANALYSE FREQUENTIELLE ############

#texte : texte chiffre & l: longueur de la clé
def analyse_frequentielle(texte,l):

   alpha = "".join([ chr(97+i) for i in range(0,26) ])
   cle = ""

   for i in range (0, l) :
      nombre = [ 0 for a in alpha] # Tableau de 26 zeros
      sous   = texte[i:len (texte):l]  # Extrait les lettres aux i,i+l,i+2l, ... possitions
      
      # Compte les occurences de chaque lettres dans le sous-texte
      for k in sous : nombre[alpha.find(k)] += 1

      #Recherche la lettre qui apparait le plus de fois
      p = 0
      for k in range (0, len(nombre)) :
         if(nombre[k] > nombre[p]): 
            p = k
      # On considere que E est la lettre la plus frequente 
      # donc on ajoute la lettre qui a codé e en alpha[p]
      cle += alpha[(p - 4) %26 ]

   return cle

def partie2_3():
   print("============ ANALYSE FREQUENTIELLE ============")
   res = partie1()
   print()
   print("Clé probable :",analyse_frequentielle(res[2],4))

############ MOT PROBABLE ############

def Occurences(s,k):
   
   if(len(s)<3):
      print("Longueur de la clé trop petite (infèrieur à 3 !)")
      return 

   # res prends toutes les combinaisons de k char possibles
   res = []
 
   for i in range (len(s)-k+1):
      for j in range(k+i,len(s)+1):
         res.append(s[i:j])

   res = list(set(res))

   # dico prends toutes les combinaisons et leur nombre d'apparition
   dico ={}

   for i in range(len(res)):
      if(s.count(res[i])>1):
         dico[res[i]] = s.count(res[i])

   if len(dico) == 0:
      return

   # Trie le dictionnaire
   # Ici, le dico est prêt 
   dicoSorted = sorted(dico.items(), key=lambda t: t[1])

   #Return la première clé
   return list(dicoSorted)[0][0]



def motProbable(txtChiffre,motProbable,pos):
   
   cle =""
   res =[]
   # Difference entre chaque lettre du mot chiffré et du mot probable
   for i in range(len(motProbable)):
      cle += chr(((((ord(txtChiffre[pos+i]))-97) - (ord(motProbable[i])-97)) %26)+97)


   p = cle[0]
   indice = []

   #Construit un tableau qui renvoie les indices des letrtes similaiers à la lettre à l'indice 0
   for i in range(1,len(cle)):
      if cle[i] == p:
         indice.append(i)

   # Coupe ce tableau pour sortir deux mots possiblement similaire
   for i in range(len(indice)):
      res.append(cle[0:indice[i]])
      res.append(cle[indice[i]:indice[i]+(len(cle)-indice[i])])

   if Occurences(str(cle),3):
      return Occurences(str(cle),3)


def partie3():

   txtChiffre = lowerAndChar(input("Entrez un texte chiffré : "))
   mot = lowerAndChar(input("Entrez un mot probable : "))
   fin =[]

   for i in range(len(txtChiffre)-len(mot)):
      fin.append(motProbable(txtChiffre,mot,i))

   for i in range(len(fin)):
      if(fin[i]):
         print("cle possible : ",fin[i])


############ MAIN ############

def main():
   print("============ CHIFFREMENT ============")
   print()
   partie1()
   partie2_1()
   partie2_2()


   # 2_3 testé avec : The U.S. Embassy recognizes that knowledge of the English language offers opportunities to improve job prospects for Serbia’s citizens, expand access to information and knowledge, and promote critical thinking and media literacy.  Proposals should use English to address problems or challenges faced by your community, such as brain drain, limited job opportunities, or the spread of disinformation.  Proposals may also utilize English as a bridge for increased communication and cooperation among neighbors within the Western Balkans, between citizens of Serbia and the United States, or between people from Serbia and EU member states.Grant activities may take any number of forms, including English language camps, academic competitions, cross-border exchanges, conferences, workshops, courses, exhibits, app development, hackathons, online projects, simulations, role-playing activities, performances, or other activities.Grant activities may take any number of forms, including English language camps, academic competitions, cross-border exchanges, conferences, workshops, courses, exhibits, app development, hackathons, online projects, simulations, role-playing activities, performances, or other activities.The Public Diplomacy Section (PDS) of the U.S. Embassy in Belgrade announces an open competition for individuals and organizations from Serbia or the U.S. to submit applications for the English Language Small Grants Program. Please check for information on other PAS funding opportunities here.Strengthen critical thinking and/or media literacy skills of students through English language activities; prepare students for participation in international academic competitions conducted in English, e.g., Model UN (Model United Nations), moot court, etc.; or explain American society, culture, and values to students through English language activities.Improve Serbian officials’ English language skills to communicate with EU counterparts and accelerate Serbia’s progress toward EU membership and western integration.Establish or strengthen connections among English language teaching professionals and institutions from countries of the Western Balkans to promote cooperation in strengthening English language instruction within the region.nform and educate audiences in Serbia about historical and cultural Serbian-U.S. ties, common attitudes and values, cooperation in different sectors (economic, political, security, health, science), and the intersection of national interests.Help Serbian civil society organizations engage with EU counterparts to make progress toward EU membership and western integration, including in the areas of human rights protection, media freedom, environmental issues, rule of law, combating corruption, etc.
   # et une clé de longueur 4 (ex : fort)
   partie2_3()


   print("============ MOT PROBABLE ============")
   # 3 testé avec : BILKO PFFGM LTWOE WJCFD SHKWO NKSEO VUSGR LWHGW FNVKW GGGFN RFHYJ VSGRF RIEKD CCGBH RYSXV KDIJA HCFFG YEFSG ZWG
   # mot probable : violente 
   partie3()
  

main()