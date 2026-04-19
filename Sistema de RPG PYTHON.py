import random

def rolar_dados(qtd, lados):
    return sum(random.randint(1, lados) for _ in range(qtd))

def turno_inimigo(inimigo):
    if inimigo["vida"] <= 15 and inimigo["mana"] >= 3:
        acao = random.choice(["cura", "cura", "ataque", "regenerar mana"])
    else:
        acao = random.choice(["ataque", "cura", "regenerar mana"])

    if acao == "ataque":
        dano = rolar_dados(3, 8)
        print(f"{inimigo['nome']} atacou e causou {dano} de dano!")
        return ("ataque", dano)

    elif acao == "cura" and inimigo["mana"] >= 3:
        cura = rolar_dados(2, 6)
        inimigo["vida"] += cura
        inimigo["mana"] -= 3
        print(f"{inimigo['nome']} se curou em {cura} PV!")
        return ("cura", cura)
    
    elif acao == "regenerar mana":
        
        mana = rolar_dados(2, 4)
        inimigo["mana"] += mana
        print(f"{inimigo['nome']} regenerou {mana} Mana!")
        return ("mana", mana)



    else:
        dano = rolar_dados(3, 8)
        print(f"{inimigo['nome']} não tinha mana e atacou causando {dano} de dano!")
        return ("ataque", dano)


# MODELOS DE PERSONAGEM
mago = {
    "nome": "Mago",
    "vida": 30,
    "vida_max": 30,
    "mana": 50,
    "mana_max": 50,
    "atk_dados": 3,
    "atk_lados": 8,
    "atk_mana": 8,
    "cura_dados": 2,
    "cura_lados": 6,
    "cura_mana": 6
}

combatente = {
    "nome": "Combatente",
    "vida": 50,
    "vida_max": 50,
    "mana": 4,
    "mana_max": 20,
    "atk_dados": 3,
    "atk_lados": 10,
    "atk_mana": 0,
    "cura_dados": 6,
    "cura_lados": 6,
    "cura_mana": 7
}

assassino = {
    "nome": "Assassino",
    "vida": 40,
    "vida_max": 40,
    "mana": 25,
    "mana_max": 25,
    "atk_dados": 2,
    "atk_lados": 12,
    "atk_mana": 12,
    "cura_dados": 2,
    "cura_lados": 6,
    "cura_mana": 2
}

personagem = {}
inimigo = {}

while True:
    print("\n1 - selecione seu personagem")
    print("2 - selecione seu inimigo")
    print("3 - combate")
    print("4 - sair")

    escolha = input("Digite a opção desejada: ")

    # ✅ CORREÇÃO PRINCIPAL AQUI
    if escolha == "1":
        print("1 - Mago")
        print("2 - Combatente")
        print("3 - Assassino")

        selecao = input("Digite o número do personagem escolhido: ")

        if selecao == "1":
            personagem = mago.copy()
        elif selecao == "2":
            personagem = combatente.copy()
        elif selecao == "3":
            personagem = assassino.copy()
        else:
            print("Opção inválida!")
            continue

        print(f"{personagem['nome']} foi selecionado!")

    elif escolha == "2":
        print("1 - Goblin")
        print("2 - Esqueleto")
        print("3 - Slime")

        selecao = input("Digite o número do inimigo escolhido: ")

        if selecao == "1":
            inimigo = {"nome": "Goblin", "vida": 40, "mana": 10}
        elif selecao == "2":
            inimigo = {"nome": "Esqueleto", "vida": 30, "mana": 10}
        elif selecao == "3":
            inimigo = {"nome": "Slime", "vida": 50, "mana": 15}
        else:
            print("Opção inválida!")
            continue

        print(f"{inimigo['nome']} foi selecionado!")

    elif escolha == "3":
        if not personagem or not inimigo:
            print("Escolha personagem e inimigo primeiro!")
            continue

        print("⚔ Combate iniciado!")

        while personagem["vida"] > 0 and inimigo["vida"] > 0:
            print("\n---------------------")
            print(f"{personagem['nome']} - PV: {personagem['vida']} | Mana: {personagem['mana']}")
            print(f"{inimigo['nome']} - PV: {inimigo['vida']} | Mana: {inimigo['mana']}")

            acao = input("Escolha ataque , cura ou regenerar mana: ").lower()

            if acao == "ataque":
                if personagem["mana"] < personagem["atk_mana"]:
                    print("Mana insuficiente!")
                    continue

                dano = rolar_dados(personagem["atk_dados"], personagem["atk_lados"])
                inimigo["vida"] -= dano
                print(f"Você causou {dano} de dano!")

            elif acao == "cura":
                if personagem["mana"] < personagem["cura_mana"] :
                    print("Mana esgotada")
                    continue
                else:
                    cura = rolar_dados(personagem["cura_dados"], personagem["cura_lados"])
                    personagem["vida"] += cura
                    personagem["vida"] = min(personagem["vida"], personagem["vida_max"])
                    personagem["mana"] -= personagem["cura_mana"]
                    print(f"Você se curou em {cura} PV!")

            elif acao == "regenerar mana":
                if personagem["mana"] > personagem["mana_max"]:
                    personagem["mana"] = personagem["mana_max"]
                    continue
                
                mana = rolar_dados(2, 4)
                personagem["mana"] += mana
                print(f"{personagem['nome']} regenerou {mana} Mana!")

                
                personagem["mana"] = min(personagem["mana"], personagem["mana_max"])
                
            if inimigo["vida"] <= 0:
                break

            print("\n➡ Turno do inimigo!")
            acao_inimigo, valor = turno_inimigo(inimigo)

            if acao_inimigo == "ataque":
                personagem["vida"] -= valor

        if personagem["vida"] <= 0:
            print("\n💀 Você foi derrotado!")
        else:
            print("\n🏆 Você venceu!")

    elif escolha == "4":
        break
