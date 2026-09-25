#Aim- Investigate how parental genotype and population allele frequency influence the simulated probability of an autosomal-recessive disorder across successive generations
#Disease - Cystic Fibrosis
import random as rd
import pandas as pd

class Cross:
   @staticmethod
   def parent_cross(parent1, parent2):
      offspring=[]
      for allele1 in parent1:
         for allele2 in parent2:
            genotype = ''.join(sorted(allele1 + allele2))
            offspring.append(genotype)
      return offspring

   @staticmethod
   def partner_selection(q):
      #Hardy-Weinberg calculation
      p=1-q
      AA=p**2
      Aa=2*p*q
      aa=q**2
      partner=rd.choices(['AA','Aa','aa'],weights=[AA,Aa,aa])[0]
      return partner

   @staticmethod
   def gens_cross(offspring, q):
      generation=[]
      for off in offspring:
         partner=Cross.partner_selection(q)
         for allele1 in off:
            for allele2 in partner:
               gen=''.join(sorted(allele1 + allele2))
               generation.append(gen)
      return generation


class Calculation:
   @staticmethod
   def percent_calculation(generation,gen_name):
      normal=0
      carrier=0
      affected=0
      for gen in generation:
         if gen=='AA':
            normal+=1
         elif gen=='Aa':
            carrier+=1
         elif gen=='aa':
            affected+=1
         else:
            print('Genotype not found')
      total=normal+carrier+affected
      print(f'Percentage assesment of {gen_name}:')
      print('Normal= ',normal/total*100,'%')
      print('carrier= ',carrier/total*100,'%')
      print('Affected= ',affected/total*100,'%')

   @staticmethod
   def save_data(generations):
    data = []
    for gen_name, generation in generations:
        for genotype in generation:
            data.append({
                'Generation': gen_name,
                'Genotype': genotype
            })
    df = pd.DataFrame(data)
    df.to_csv('gen_data.csv', index=False)

f1= Cross.parent_cross("Aa", "Aa")
f2 = Cross.gens_cross(f1, 0.02)
f3 = Cross.gens_cross(f2, 0.02)
f4 = Cross.gens_cross(f3, 0.02)


f1_percent=Calculation.percent_calculation(f1,'F1')
f2_percent=Calculation.percent_calculation(f2,'F2')
f3_percent=Calculation.percent_calculation(f3,'F3')
f4_percent=Calculation.percent_calculation(f4,'F4')

generations = [
    ('F1', f1),
    ('F2', f2),
    ('F3', f3),
    ('F4', f4)
]
Calculation.save_data(generations)
