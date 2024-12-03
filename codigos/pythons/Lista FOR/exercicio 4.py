populacao_a = 80000
taxa_crescimento_a = 3 
populacao_b = 200000
taxa_crescimento_b = 1.5  
anos_max = 100  # Limite máximo de anos para evitar loops infinitos

historico_a = [populacao_a]
historico_b = [populacao_b]

for ano in range(1, anos_max + 1):

    nova_pop_a = historico_a[-1] * (1 + taxa_crescimento_a / 100)
    nova_pop_b = historico_b[-1] * (1 + taxa_crescimento_b / 100)
    

    historico_a.append(nova_pop_a)
    historico_b.append(nova_pop_b)
    
    if nova_pop_a >= nova_pop_b:
        print(f"Serão necessários {ano} anos para que a população do país A ultrapasse ou iguale a população do país B.")
        break

