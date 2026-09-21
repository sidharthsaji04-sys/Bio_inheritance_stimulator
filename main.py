#Aim- Investigate how parental genotype and population allele frequency influence the simulated probability of an autosomal-recessive disorder across successive generations
#Disease - Cystic Fibrosis
import random as rd
def crossing(parent1,parent2,q):
   #Hardy-Weinberg calculation
   p=1-q
   AA=p**2
   Aa=2*p*q
   aa=q**2

   offspring=[]
   possible_genos=['AA','Aa','aa']
   for allele1 in parent1:
       for allele2 in parent2:
        genotype1 = ''.join(sorted(allele1 + allele2))
        offspring.append(genotype1)

   f2_offsprings=[]
   normal2=0
   carrier2=0
   affected2=0
   print('F2 generation')
   for off in offspring:
    partner=rd.choices(possible_genos,weights=[AA,Aa,aa])[0]
    print(f'{off} - {partner}')
    for allele1 in off:
      for allele2 in partner:
        f2 = ''.join(sorted(allele1 + allele2))
        f2_offsprings.append(f2)
        
        if f2== 'AA':
           normal2+=1
           print(f2, '-normal')
        elif f2=='Aa' or f2=='aA':
          carrier2+=1
          print(f2, '-carrier')
        else:
           affected2+=1
           print(f2, '-affected')
   print("Total analysis: ")
   total = normal2 + carrier2 + affected2
   print(f'Total normal- {normal2/total*100:.1f}%',)
   print(f'Total carrier- {carrier2/total*100:.1f}%')
   print(f'Total affected- {affected2/total*100:.1f}%')

   print('F3 generations')
   normal3=0
   carrier3=0
   affected3=0
   for off in f2_offsprings:
     partner=rd.choices(possible_genos,weights=[AA,Aa,aa])[0]
     for allele1 in off:
       for allele2 in partner:
         f3=allele1 + allele2
         if f3== 'AA':
               normal3+=1
               print(f3, '-normal')
         elif f3=='Aa' or f3=='aA':
               carrier3+=1
               print(f3, '-carrier')
         else:
               affected3+=1
               print(f3, '-affected')

   print("Total analysis: ")
   total3 = normal3 + carrier3 + affected3
   print('Offsprings- ', total3)
   print(f'Total normal- {normal3/total3*100:.1f}%',)
   print(f'Total carrier- {carrier3/total3*100:.1f}%')
   print(f'Total affected- {affected3/total3*100:.1f}%')


crossing('AA','Aa',0.02)
