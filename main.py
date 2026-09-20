#Aim- Investigate how parental genotype and population allele frequency influence the simulated probability of an autosomal-recessive disorder across successive generations

import random as rd
def autosomal_recessive(parent1,parent2):
   offspring=[]
   possible_genos=['AA','Aa','aa']
   for allele1 in parent1:
       for allele2 in parent2:
        offspring.append(allele1 + allele2)
   f2_offsprings=[]
   normal=0
   carrier=0
   affected=0
   for off in offspring:
    partner=rd.choice(possible_genos)
    print(f'{off} - {partner}')
    for allele1 in off:
      for allele2 in partner:
        f2=allele1 + allele2
        f2_offsprings.append(f2)
        
        if f2== 'AA':
           normal+=1
           print(f2, '-normal😀')
        elif f2=='Aa' or f2=='aA':
          carrier+=1
          print(f2, '-carrier😕')
        else:
           affected+=1
           print(f2, '-affected😷')
   print("Total analysis: ")
   total = normal + carrier + affected
   print(f'Total normal- {normal/total*100:.1f}%',)
   print(f'Total carrier- {carrier/total*100:.1f}%')
   print(f'Total affected- {affected/total*100:.1f}%')

autosomal_recessive('AA','Aa')
