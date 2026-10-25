import duckdb

con = duckdb.connect()

# Consulta no arquivo CSV
consulta_csv = con.execute("""
    SELECT
        COUNT(*) AS quantidade_transacoes,
        SUM(valor) AS valor_total
    FROM read_csv_auto(
        'projeto02/data/raw/transacoes/data_transacoes.csv'
    )
    WHERE CAST(data_hora AS DATE) = DATE '2026-10-01'
""").fetchdf()

print("\nResultado CSV:")
print(consulta_csv)

con.close()