#include <stdio.h>
#include <stdlib.h>

#define X 100
#define N 88088


char * initialiser0(int taille);
char * initialiser1(int taille);
void afficheTab(char* tab, int taille);
void libererNombre(char * n);
void afficher(int n, int taille ,char * tab);
int comparer(char * tab1,char * tab2);
int estPair(char * tab);
void divisePar2(char * tab);
void reduireDe1(char * tab);
void multiplierPar2(char * tab);
char * ajouter(char * tab1, char * tab2);
char * multiplier(char * tab1, char * tab2);
char * exponentiationRapideSansModulo(char * tab1,char * tab2);
char * soustraire(char * a, char *b);
int aPlusGrandb(char * a,char *b);
char * ApproxSup(char * a);
char * ApproxInf(char * a);
char * modulo(char * a,char * n);
void ajoute1(char * a);
char * exponentiationRapide(char * a, char * b, char * n);
void inverseTab(char * tab);
char * txtToBin(char * file);
char * decoupeEtModulo(char * tab,char * e,char * n);

int main()
{
   // Tableaux de char
   char *nKey; 
   char *p;
   char *q;
   char *e;
   char *phi;
   char d[100] = "1000010110111";
   char * txtBin;
   char * test;
   
   //Initialisation 
   p = initialiser0(X);
   e = initialiser0(X);
   q = initialiser0(X);
   nKey = initialiser0(X);
   phi = initialiser0(X);
   txtBin = initialiser0(X);
   test = initialiser0(X);

   //afficheTab(c,X);

   //afficher(N,X,c);
   afficher(7,X,e);
   afficher(53,X,p);
   afficher(97,X,q);

   // Calcul de n
   printf("\nn -> (p*q) = ");
   nKey = multiplier(p,q);
   afficheTab(nKey,X);

   //calcul de phi
   reduireDe1(p);
   reduireDe1(q);

   phi = multiplier(p,q);
   printf("\nPhi -> (p-1)*(q-1) = ");
   afficheTab(phi,X);

   //Affiche d
   printf("\nAffcihage de d : ");
   inverseTab(d);
   afficheTab(d,X);

   //Lecture Fichier
   printf("\nLecture du message m avec les lettres : ");
   txtBin = txtToBin("mot.txt");
   afficheTab(txtBin,X);

   // m^e [n]
   //exponentiationRapide(txtBin,e,nKey);

   //Test
   test = decoupeEtModulo(txtBin,e,nKey);
   afficheTab(test,X);
   

   libererNombre(e);
   libererNombre(p);
   libererNombre(q);
   libererNombre(nKey);
   libererNombre(phi);

   return 0;
}


char * initialiser0(int taille)
{
    
   char * tab = malloc(taille*sizeof(char*));
        
   for(int i=0;i<taille;i++)
   {
      tab[i] = '0';
   }
    
   return tab;
    
}

char * initialiser1(int taille)
{
    
   char * tab = malloc(taille*sizeof(char*));
        
   for(int i=0;i<taille;i++)
   {
      if(i == taille-1)
         tab[i] = '1';
      else 
         tab[i] = '0';
   }
    
   return tab;
    
}

void afficheTab(char* tab, int taille)
{
   printf("\n");
   for(int i=0;i<taille;i++)
   {
      printf("%c",tab[i]);
   }
   printf("\n");
}

void libererNombre(char *n)
{
   free(n);
}


void afficher(int n, int taille ,char * tab)
{
   int i;
   int * a = malloc(taille*sizeof(int*));


   for(i=0;n>0;i++)    
   {    
      a[i]=n%2;    
      n=n/2;    
   }

   for(i-=1;i>=0;i--)    
   {    
      if(a[i] == 0)
         tab[taille-1-i] = '0';
      else
         tab[taille-1-i] = '1';   
   }

   afficheTab(tab,taille);

   printf("\n");
}

// 1 si egaux, 0 sinon
int comparer(char * tab1,char * tab2)
{
   for(int i=0;i<X;i++)
   {
      if(tab1[i] != tab2[i])
         return 0;
   }

   return 1;
}

int estPair(char * tab)
{
   if(tab[X-1] == '0')
      return 1;
   else  
      return 0;
}

void divisePar2(char * tab)
{
   for(int i=X-1;i>1;i--)
   {
      tab[i]=tab[i-1];
   }
}

void reduireDe1(char * tab)
{
   int i = X-1;

   while(tab[i] != '1')
   {
      i--;
   }

   tab[i] = '0';
   i++;

   for(i;i<X+1;i++)
   {
      tab[i] = '1';
   }
}

void multiplierPar2(char * tab)
{
   for(int i=0;i<X;i++)
   {
      tab[i] = tab[i+1];
   }
   tab[X-1] = '0';
}

char * ajouter(char * tab1, char * tab2)
{
   int retenue = 0;
   char * tab = malloc(X*sizeof(char*));

   //Init tab
   for(int i=0;i<X;i++)
   {
      tab[i] = '0';
   }
        
   for(int i=X-1;i>0;i--)
   {
      //Cas 1-1
      if(tab1[i]== '1' && tab2[i]== '1' && retenue == 0)
      {
         tab[i] = '0';
         retenue++;
      }

      else if(tab1[i]== '1' && tab2[i]== '1' && retenue == 1)
      {
         tab[i] = '1';
      }

      //Cas 0-1 et 1-0
      else if((tab1[i]== '0' && tab2[i]== '1' && retenue == 0) || (tab1[i]== '1' && tab2[i]== '0' && retenue == 0))
         tab[i] = '1';

      else if((tab1[i]== '0' && tab2[i]== '1' && retenue == 1) || (tab1[i]== '1' && tab2[i]== '0' && retenue == 1))
      {
         tab[i] = '0';
         retenue;
      }

      //Cas 0-0
      else if(tab1[i]== '0' && tab2[i]== '0' && retenue == 0)
         tab[i] = '0';
      else
      {
         tab[i] = '1';
         retenue--;
      }

   }

   if(retenue == 1)
   {
      printf("OVERFLOW !");
   }


   return tab;
    
}

char * multiplier(char * tab1, char * tab2)
{
   char * tab = malloc(X*sizeof(char*));
   tab = initialiser0(X);

   char * tmp = malloc(X*sizeof(char*));


   int cpt = 0;
   int cpt1 = 0;

   //Trouver le moins long 
   for(int i=0;tab1[i] !='1';i++)
      cpt++;

   for(int i=0;tab2[i] !='1';i++)
      cpt1++;

   //tab2 plus petit que tab1
   if(cpt<=cpt1)
   {
      for(int i = X-1;i>cpt1-1;i--)
      {
         if(tab2[i] == '1')
         {
            tmp = initialiser0(X);
            for(int j = X-1;j>cpt-1;j--)
            {

               tmp[j-((X-1)-i)] = tab1[j];
            }
            tab = ajouter(tab,tmp);
         }
      }
   }

   //tab1 plus petit que tab2
   else{
      for(int i = X-1;i>cpt-1;i--)
      {
         if(tab1[i] == '1')
         {
            tmp = initialiser0(X);
            for(int j = X-1;j>cpt1-1;j--)
            {
               tmp[j-((X-1)-i)] = tab2[j];
            }
            tab = ajouter(tab,tmp);
         }
      }
   }

   return tab;
}

// a^b -> tab1^tab2
char * exponentiationRapideSansModulo(char * tab1,char * tab2)
{
   char * tab = malloc(X*sizeof(char*));
   char * tmp = malloc(X*sizeof(char*));
   char * copieTab1 = malloc(X*sizeof(char*));
   char * copieTab2 = malloc(X*sizeof(char*));
   tab = initialiser1(X);
   tmp = initialiser0(X);

   //Copies
   for(int i =0;i<X;i++)
   {
      copieTab1[i] = tab1[i];
   }

   for(int i =0;i<X;i++)
   {
      copieTab2[i] = tab2[i];
   }

   //Si tab2 est égal à 1, retourner tab1
   if(comparer(copieTab2,tab))
   {
      return copieTab1;
   }

   //Si b est pair
   else if(estPair(copieTab2))
   {
      copieTab1 = multiplier(copieTab1,copieTab1);
      divisePar2(copieTab2);

      return exponentiationRapideSansModulo(copieTab1,copieTab2);
   }

   //Si b est impair
   else
   {
      tmp = copieTab1;
      copieTab1 = multiplier(copieTab1,copieTab1);
      reduireDe1(copieTab2);
      divisePar2(copieTab2);
      return multiplier(tmp,exponentiationRapideSansModulo(copieTab1,copieTab2));
   }

}


char * soustraire(char * a, char *b)
{
   char * tab = malloc(X*sizeof(char*));
   char * copieA = malloc(X*sizeof(char*));

   for(int i=0;i<X;i++)
   {
      copieA[i] = a[i];
   }
   int cpt =  0;

   for(int i=X-1;i>=0;i--)
   {
      if((copieA[i] == '0' && b[i] == '0') || (copieA[i] == '1' && b[i] == '1'))
         tab[i] = '0';

      else if((copieA[i] == '1' && b[i] == '0'))
         tab[i] = '1';

      else if(copieA[i] == '0' && b[i] == '1')
      {
         for(int j=i;copieA[j] != '1';j--)
         {
            cpt++;
            copieA[j] = '1';
         }
         copieA[i-cpt] = '0';
         tab[i] = '1';
         cpt = 0; 
      }
   }

   return tab;
}

//1 si A>B, 0 sinon
int aPlusGrandb(char * a,char *b)
{
   
   if(comparer(a,b) == 0)
   {
      for(int i = 0; i <X ;i++)
      {
         if(a[i] == '1' && b[i] == '0')
            return 1;
         else if(a[i] == '0' && b[i] == '1')
            return 0;
      }
      return 1;
      
   }

   else if(comparer(a,b) == 1)
      return 1;
   
   
   
}


// Approximation a la puissance de 2 supérieure
char * ApproxSup(char * a)
{
   char * tab = malloc(X*sizeof(char*));

   int indice = 0;
   for(int i=X-1;i>=0;i--)
   {
      if(a[i] == '1')
      indice = i;
   }

   if(indice == 0)
      tab = initialiser1(X);

   else
   {
      for(int i = 0;i<X;i++)
      {
         if(i == indice-1)
            tab[i] = '1';
         else
            tab[i] = '0';
      }
   }

   return tab;

}


// Approximation a la puissance de 2 inferieur
char * ApproxInf(char * a)
{
   char * tab = malloc(X*sizeof(char*));

   int indice = 0;
   for(int i=X-1;i>=0;i--)
   {
      if(a[i] == '1')
      indice = i;
   }

   if(indice == 0)
      tab = initialiser0(X);

   else
   {
      for(int i = 0;i<X;i++)
      {
         if(i >= indice+1)
            tab[i] = '1';
         else
            tab[i] = '0';
      }
   }

   return tab;

}

char * modulo(char * a,char * n)
{
   char * tab = malloc(X*sizeof(char*));
   char * approxS = malloc(X*sizeof(char*));
   char * approxI = malloc(X*sizeof(char*));
   char * multi = malloc(X*sizeof(char*));
   char * multiRes = malloc(X*sizeof(char*));

   //Tab est la copie de A pour ne pas modifier directement A
   for(int i =0;i<X;i++)
   {
      tab[i] = a[i];
   }

   //Approximation de n
   approxS = ApproxSup(n);

   while(aPlusGrandb(tab,n))
   {
      multi = initialiser1(X);
      multiRes = multiplier(approxS,multi);      
      
      while(aPlusGrandb(tab,multiRes))
      {
         multiplierPar2(multi);
         multiRes = multiplier(approxS,multi);
      }
      
      divisePar2(multi);
      
      multiRes = multiplier(n,multi);
      tab = soustraire(tab,multiRes);
      
      if(!aPlusGrandb(tab,n))
         return tab;

      approxI = ApproxInf(tab);

      while(aPlusGrandb(tab,approxI))
      {
         tab = soustraire(tab,n);
      }
   }
   return tab;

}

void ajoute1(char * a)
{
   int i = X-1;

   while(a[i] == '1')
   {
      
      a[i] = '0';
      i--;
   }
   a[i] = '1';
}

//Exponentiation avec Modulo -> a^b [n]
char * exponentiationRapide(char * a, char * b, char * n)
{
   char * tab = malloc(X*sizeof(char*));
   char * bIncr = malloc(X*sizeof(char*));
   char * copieRes = malloc(X*sizeof(char*));

   bIncr = initialiser0(X);
   copieRes = initialiser1(X);
   reduireDe1(b);

   printf("Exponentiation rapide : \n");

   while(aPlusGrandb(b,bIncr))
   {
      ajoute1(bIncr);

      tab = modulo(multiplier(a,copieRes),n);      

      for(int i = 0;i<X;i++)
      {
         copieRes[i] = tab[i];
      }

      // Affichage de chaque modulo à chaque étapes
      
   }
   afficheTab(tab,X);
   return tab;
}

void inverseTab(char * tab)
{
   // Remplir de 0 si possible
   int c = 0;
   for(int i =0;i<X;i++)
   {
      if(tab[i] == '1' || tab[i] == '0')
         c++;
   }

   for(int i =c;i>=0;i--)
   {
      tab[i+(X-c)] = tab[i];
      tab[i] = '0';
   }

}

char * txtToBin(char * file)
{
   int caractereActuel = 0;
   int cpt = 0;

   char * tab = malloc(X*sizeof(char*));
   tab = initialiser0(X);

   char * tmp = malloc(8*sizeof(char*));
   tmp = initialiser0(8);
 
   FILE * fichier = fopen(file, "r");
   if (fichier != NULL)
   {
      while (caractereActuel != -1)
      {
         caractereActuel = fgetc(fichier); // On lit le caractère
         afficher((int)caractereActuel,8,tmp);

         for(int i =0;i<8;i++)
         {
            tab[i+8*cpt] = tmp[i];
         }
         cpt++;
      }
 
      fclose(fichier);
   }

   for(int i =(cpt-1)*8;i>=0;i--)
   {
      tab[i+(X-(cpt-1)*8)] = tab[i];
      tab[i] = '0';
   }
   return tab;
}

char * decoupeEtModulo(char * tab,char * e,char * n)
{  
   // cpt compte le nombre de tours (et donc de blocs de 3)
   int cpt = 0;
   int j = 0;
   int taille = 0;

   char * res = malloc(X*sizeof(char*));
   res = initialiser0(X);

   char * tmp = malloc(X*sizeof(char*));
   tmp = initialiser0(X);

   char * tmp2 = malloc(X*sizeof(char*));
   tmp2 = initialiser0(X);

   while(j<X)
   {
      //Recupere les 3 bits dans tmp
      for(int i=0;i<3;i++)
      {
         tmp[X-3+i] = tab[i+3*cpt];
      }

      printf("3 BITS");
      afficheTab(tmp,X);
      printf("\n");

      //Expo Rapide modulaire
      tmp2 = exponentiationRapide(tmp,e,n);

      //Rempli res, le tab final
      for(int k=4*cpt;k<4*cpt+4;k++)
      {
         res[k] = tmp[k%4];
      }

      cpt++;
      j = j*3;
   }

   return res;
}