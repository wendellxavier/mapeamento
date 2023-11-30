from lista import produtos, pessoas, lista

def aumentar_preco(p):
    p['preco'] = round (p['preco'] * 1.05, 2)
    return p

novo_preco = map(aumentar_preco, produtos)

for produto in novo_preco:
    print(produto)

print()

def aumentar_idade(p):
    p['nova_idade'] = round (p['idade'] + 1)
    return p
idade = map(aumentar_idade, pessoas)

for pessoa in idade:
    print(pessoa)

