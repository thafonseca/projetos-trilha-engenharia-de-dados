import duckdb

con = duckdb.connect()

# Consulta nos arquivos Parquet
consulta_parquet = con.execute("""
    SELECT
        COUNT(*) AS quantidade_transacoes,
        SUM(valor) AS valor_total
    FROM read_parquet(
        'projeto02/data/curated/transacoes',
        hive_partitioning = true
    )
    WHERE data_ref = DATE '2026-10-01'
""").fetchdf()

print("Resultado Parquet:")
print(consulta_parquet)


