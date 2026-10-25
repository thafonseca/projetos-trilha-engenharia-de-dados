"""
Script para consultar as tabelas do banco de dados DuckDB - PROJETO 01.
Utiliza Pandas e DuckDB para visualizar os dados.
"""

import duckdb
import pandas as pd

# Caminho para o arquivo do banco de dados do projeto01
BANKO_DUCKDB = '/Users/thaisfonseca/projetos/mentoria-dados/projeto01/data/banco.duckdb'

print("🔌 Conectando ao banco DuckDB...")
con = duckdb.connect(BANKO_DUCKDB)

# Consultar e converter para DataFrame do Pandas
print('\n📊 Consultando tabela clientes:')
df_clientes = con.sql("SELECT * FROM clientes").fetchdf()
print(df_clientes.to_string())

print('\n📊 Consultando tabela contas:')
df_contas = con.sql("SELECT * FROM contas").fetchdf()
print(df_contas.to_string())

print('\n📊 Consultando tabela transacoes:')
df_transacoes = con.sql("SELECT * FROM transacoes").fetchdf()
print(df_transacoes.to_string())
