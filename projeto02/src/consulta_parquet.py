import duckdb

con = duckdb.connect()

resultado = con.execute("""
    SELECT *
    FROM read_parquet(
        'projeto02/data/curated/transacoes',
        hive_partitioning = true
    )
    LIMIT 10
""").fetchdf()

print(resultado)

con.close()