import pandas as pd

# Caminho do arquivo original
caminho_arquivo_original = 'microdados_ed_basica_2024.csv'
dados = pd.read_csv(caminho_arquivo_original, encoding='latin1', delimiter=';')

dados_filtrados_regiao = dados[dados['NO_REGIAO'] == 'Nordeste'] 
colunas_selecionadas = [
    'CO_ENTIDADE',
    'NO_ENTIDADE',
    'CO_REGIAO',
    'NO_REGIAO',
    'CO_UF',
    'NO_UF',
    'CO_MUNICIPIO',
    'NO_MUNICIPIO',
    'QT_MAT_BAS',
    'QT_MAT_FUND',
    'QT_MAT_MED',
    'CO_MESORREGIAO',
    'NO_MESORREGIAO',
    'CO_MICRORREGIAO',
    'NO_MICRORREGIAO'
]

# Aplicar seleção
dados_filtrados = dados_filtrados_regiao[colunas_selecionadas]

# Exportar para JSON
caminho_arquivo_filtrado = 'censo_escolar_2024_filtrado.json'
dados_filtrados.to_json(caminho_arquivo_filtrado, orient='records', force_ascii=False, indent=2)

print(f"Arquivo filtrado salvo com sucesso em: {caminho_arquivo_filtrado}")
