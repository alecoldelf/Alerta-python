import os
os.system("cls")

# Alerta+ - Sistema de Monitoramento de Enchentes
# Desenvolvido por: [SEU NOME AQUI]
# RM: [SEU RM AQUI]

import pandas as pd
import os

def mostrar_rota_de_fuga(cidade):
    rotas = {
        "Rio De Janeiro": "Dirija-se ao ponto de apoio mais próximo indicado pela Defesa Civil.",
        "São Paulo": "Procure os abrigos temporários listados no site da prefeitura.",
        "Belo Horizonte": "Suba para regiões mais altas e procure centros comunitários.",
        "Salvador": "Vá até escolas municipais designadas como ponto seguro.",
        "Porto Alegre": "Siga para os ginásios públicos sinalizados como abrigos.",
        "Brasília": "Procure os centros comunitários designados no plano distrital.",
        "Curitiba": "Desloque-se até unidades de abrigo em colégios estaduais.",
        "Recife": "Evacue para os pontos elevados sinalizados pela prefeitura.",
        "Fortaleza": "Dirija-se aos postos de apoio da Defesa Civil local.",
        "Manaus": "Siga para os centros municipais nas zonas mais altas.",
        "Belém": "Busque os pontos de apoio nas escolas públicas.",
        "Goiânia": "Vá até os ginásios esportivos sinalizados como abrigo.",
        "São Luís": "Refugie-se em escolas estaduais de emergência.",
        "Maceió": "Suba para áreas não alagadas e abrigos da prefeitura.",
        "Natal": "Siga para pontos comunitários nos bairros mais altos.",
        "Aracaju": "Busque abrigo nos colégios estaduais de apoio.",
        "João Pessoa": "Evacue até as zonas seguras indicadas.",
        "Palmas": "Refugie-se em prédios públicos sinalizados.",
        "Cuiabá": "Procure os abrigos temporários da cidade.",
        "Campo Grande": "Busque locais seguros nas escolas públicas.",
        "Teresina": "Vá até pontos de apoio nos centros comunitários.",
        "Boa Vista": "Siga até o abrigo central ou escolas estaduais.",
        "Macapá": "Evacue até áreas mais altas nos bairros centrais.",
        "Porto Velho": "Procure as escolas de abrigo em zonas elevadas.",
        "Rio Branco": "Refugie-se em colégios municipais seguros.",
        "Florianópolis": "Vá para pontos turísticos mais altos designados como abrigo.",
        "Vitória": "Dirija-se aos ginásios e escolas designadas para emergência."
    }
    return rotas.get(cidade.title(), "⚠️ Rota de fuga não cadastrada para esta cidade. Siga as orientações locais.")

def registrar_em_arquivos(registro, caminho_txt, caminho_excel):
    with open(caminho_txt, "a", encoding="utf-8") as txt_file:
        txt_file.write(
            f"{registro['Cidade']} - {registro['Bairro']} | "
            f"Temperatura: {registro['Temperatura']} ºC | "
            f"Umidade: {registro['Umidade']}% | "
            f"Risco: {registro['Risco de Alagamento']} | "
            f"Rota: {registro['Rota de Fuga']}\n"
        )

    try:
        df_existente = pd.read_excel(caminho_excel)
        df_novo = pd.DataFrame([registro])
        df_atualizado = pd.concat([df_existente, df_novo], ignore_index=True)
    except FileNotFoundError:
        df_atualizado = pd.DataFrame([registro])

    df_atualizado.to_excel(caminho_excel, index=False)

def main():
    print("=== Alerta+ - Verificador Rápido de Enchentes ===")
    cidade = input("Digite o nome da sua cidade (ex: Recife): ").strip().title()
    bairro = input("Digite o nome do seu bairro: ").strip().title()

    try:
        temperatura = float(input("Informe a temperatura atual (ºC): "))
        umidade = float(input("Informe a umidade atual (%): "))
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos.")
        return

    risco = "Sim" if temperatura > 33 and umidade > 90 else "Não"
    rota = mostrar_rota_de_fuga(cidade)

    print(f"\n📍 {bairro}, {cidade}")
    print(f"🌡️ Temperatura: {temperatura} ºC")
    print(f"💧 Umidade: {umidade} %")
    print(f"⚠️ Risco de Alagamento: {risco}")
    print(f"🚨 Rota de Fuga: {rota}")

    registro = {
        "Cidade": cidade,
        "Bairro": bairro,
        "Temperatura": temperatura,
        "Umidade": umidade,
        "Risco de Alagamento": risco,
        "Rota de Fuga": rota
    }

    registrar_em_arquivos(
        registro,
        "registro_alerta.txt",
        "registro_alerta.xlsx"
    )

if __name__ == "__main__":
    main()
