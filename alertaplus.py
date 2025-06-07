#1ESPR
#Alexandre Delfino...: RM560059
#Enzo Luciano........: RM559557
#livia Pereira Dias..: RM559414

import os
import pandas as pd

# Limpa o terminal (somente para Windows)
os.system("cls")

# === Funções ===

def obter_rota(cidade):
    """
    Retorna a rota de fuga para a cidade informada.
    Se não estiver cadastrada, retorna um aviso genérico.
    """
    rotas = {
        "Rio De Janeiro": "Ponto de apoio mais próximo (Defesa Civil).",
        "São Paulo": "Abrigos temporários (site da prefeitura).",
        "Belo Horizonte": "Regiões altas ou centros comunitários.",
        "Salvador": "Escolas municipais designadas.",
        "Porto Alegre": "Ginásios públicos sinalizados.",
        "Brasília": "Centros comunitários do plano distrital.",
        "Curitiba": "Colégios estaduais como abrigo.",
        "Recife": "Pontos elevados da prefeitura.",
        "Fortaleza": "Postos de apoio (Defesa Civil).",
        "Manaus": "Centros municipais em zonas altas.",
        "Belém": "Escolas públicas de apoio.",
        "Goiânia": "Ginásios esportivos sinalizados.",
        "São Luís": "Escolas estaduais de emergência.",
        "Maceió": "Áreas não alagadas e abrigos.",
        "Natal": "Bairros mais altos e centros.",
        "Aracaju": "Colégios estaduais de apoio.",
        "João Pessoa": "Zonas seguras indicadas.",
        "Palmas": "Prédios públicos sinalizados.",
        "Cuiabá": "Abrigos temporários.",
        "Campo Grande": "Escolas públicas seguras.",
        "Teresina": "Centros comunitários.",
        "Boa Vista": "Abrigo central ou escolas.",
        "Macapá": "Bairros centrais elevados.",
        "Porto Velho": "Escolas em zonas altas.",
        "Rio Branco": "Colégios municipais seguros.",
        "Florianópolis": "Pontos turísticos altos.",
        "Vitória": "Ginásios e escolas emergenciais."
    }

    return rotas.get(cidade.title(), "⚠️ Cidade não cadastrada. Siga orientações locais.")

def salvar_dados(dados, arq_txt, arq_xlsx):
    """
    Salva os dados de alerta em arquivo .txt e Excel (.xlsx).
    """
    # Grava no .txt
    with open(arq_txt, "a", encoding="utf-8") as txt:
        txt.write(
            f"{dados['Cidade']} - {dados['Bairro']} | "
            f"Temp: {dados['Temp']} ºC | "
            f"Umid: {dados['Umid']}% | "
            f"Risco: {dados['Risco']} | "
            f"Rota: {dados['Rota']}\n"
        )

    # Tenta ler o Excel, senão cria um novo
    try:
        df_antigo = pd.read_excel(arq_xlsx)
        df_novo = pd.DataFrame([dados])
        df_final = pd.concat([df_antigo, df_novo], ignore_index=True)
    except FileNotFoundError:
        df_final = pd.DataFrame([dados])

    df_final.to_excel(arq_xlsx, index=False)

def main():
    """
    Coleta dados do usuário, calcula risco e salva registros.
    """
    print("=== Alerta+ | Verificador de Enchentes ===")

    # Entrada do usuário
    cid = input("Cidade: ").strip().title()
    bai = input("Bairro: ").strip().title()

    try:
        temp = float(input("Temperatura (ºC): "))
        umid = float(input("Umidade (%): "))
    except ValueError:
        print("❌ Erro: Insira valores numéricos válidos.")
        return

    # Define risco
    risco = "Sim" if temp > 30 and umid > 90 else "Não"
    rota = obter_rota(cid)

    # Exibe os dados
    print(f"\n📍 {bai}, {cid}")
    print(f"🌡️ Temp: {temp} ºC")
    print(f"💧 Umidade: {umid} %")
    print(f"⚠️ Risco: {risco}")
    print(f"🚨 Rota: {rota}")

    # Registra dados
    dados = {
        "Cidade": cid,
        "Bairro": bai,
        "Temp": temp,
        "Umid": umid,
        "Risco": risco,
        "Rota": rota
    }

    salvar_dados(dados, "alerta.txt", "alerta.xlsx")

# Roda o programa
if __name__ == "__main__":
    main()
