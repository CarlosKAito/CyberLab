
import csv
from collections import Counter  # importando a Biblioteca
from pathlib import Path

# Localização dos arquivos
pasta = Path(__file__).parent
arquivos_logs = pasta / "Dados" / "logs.csv"
pasta_relatorios = pasta / "Relatorios"

pasta_relatorios.mkdir(exist_ok=True)

# Contadores
total = 0
falhas = 0
usuarios_com_falhas = Counter()

# Leitura dos logs
with open(arquivos_logs, "r", encoding="utf-8") as arquivos:
    leitor = csv.DictReader(arquivos)

    for registro in leitor:
        total += 1

        if registro["status"].strip().lower() == "falha":
            falhas += 1
            usuario = registro["usuario"]
            usuarios_com_falhas[usuario] += 1

# Geração de relatórios
relatorio = [
    "RELATORIO DE ANALISE DE LOGS",
    "============================",
    f"Total de eventos: {total}",
    f"Falhas de login: {falhas}",
    "",
    "FALHAS POR USUARIOS:"
]

for usuario, quantidade in usuarios_com_falhas.items():
    relatorio.append(f"{usuario}: {quantidade} falhas")

# Identificação de usuários com 3 ou mais falhas
relatorio.append("")
relatorio.append("ALERTAS DE SEGURANCA:")
relatorio.append("=====================")

alertas = 0

for usuario, quantidade in usuarios_com_falhas.items():
    if quantidade >= 3:
        relatorio.append(
            f"ALERTA: {usuario} teve {quantidade} falhas de login!"
        )
        alertas += 1

if alertas == 0:
    relatorio.append("Nenhum alerta encontrado.")

# Criando o arquivo de relatório
texto = "\n".join(relatorio)

arquivo_saida = pasta_relatorios / "relatorio.txt"
arquivo_saida.write_text(texto, encoding="utf-8")

print(texto)
print("\nRelatorio salvo na pasta Relatorios.")
