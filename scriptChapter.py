
# SCRIPT PYTHON


nota_ide = float(input("Informe a nota do IDE: "))
nota_ficha_avalicao = float(input("Informe a nota da ficha de avaliação: "))
nota_de_defesa_tcc = float(input("Informe a nota de defesa do TCC: "))

nota_total = (0.3 * nota_ide + 0.5 * nota_ficha_avalicao + 0.2 * nota_de_defesa_tcc) / 3

print(f"Nota total: {nota_total}")
