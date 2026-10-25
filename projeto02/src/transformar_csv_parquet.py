
import duckdb

con = duckdb.connect()

# 1. Gerar os arquivos Parquet
con.execute("""
    COPY (
        SELECT
            CAST(id_transacao AS INTEGER) AS id_transacao,
            CAST(id_conta AS INTEGER) AS id_conta,
            CAST(data_hora AS TIMESTAMP) AS data_hora,
            CAST(tipo AS VARCHAR) AS tipo,
            CAST(valor AS DECIMAL(18,2)) AS valor,
            CAST(data_hora AS DATE) AS data_ref
        FROM read_csv_auto(
            'data/raw/transacoes/data_transacoes.csv'
        )
    )
    TO 'data/curated/transacoes'
    (
        FORMAT PARQUET,
        PARTITION_BY (data_ref)
    )
""")

print("Arquivos Parquet gerados!")

# 2. Consultar os arquivos Parquet
resultado = con.execute("""
    SELECT *
    FROM read_parquet(
        'data/curated/transacoes/**/*.parquet',
        hive_partitioning = true
    )
    LIMIT 10
""").fetchdf()

# 3. Exibir o resultado no terminal
print(resultado)

con.close()
