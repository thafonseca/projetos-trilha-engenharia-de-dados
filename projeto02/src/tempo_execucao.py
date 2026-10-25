
import duckdb
import time
import statistics

con = duckdb.connect()

consultas = {
    "CSV": """
        SELECT
            COUNT(*) AS quantidade_transacoes,
            SUM(valor) AS valor_total
        FROM read_csv_auto(
            'projeto02/data/raw/transacoes/data_transacoes.csv'
        )
        WHERE CAST(data_hora AS DATE) = DATE '2026-10-01'
    """,

    "Parquet": """
        SELECT
            COUNT(*) AS quantidade_transacoes,
            SUM(valor) AS valor_total
        FROM read_parquet(
            'projeto02/data/curated/transacoes/**/*.parquet',
            hive_partitioning = true
        )
        WHERE data_ref = DATE '2026-10-01'
    """
}

for formato, sql in consultas.items():
    # Aquecimento: não entra no cálculo da mediana
    con.execute(sql).fetchall()

    tempos = []

    # 7 execuções medidas
    for i in range(7):
        inicio = time.perf_counter()

        resultado = con.execute(sql).fetchall()

        fim = time.perf_counter()
        tempos.append(fim - inicio)

    mediana = statistics.median(tempos)

    print(f"\nFormato: {formato}")
    print(f"Quantidade de transações: {resultado[0][0]}")
    print(f"Valor total: {resultado[0][1]}")
    print(f"Tempos (segundos): {[round(t, 5) for t in tempos]}")
    print(f"Tempo mediano: {mediana:.5f} segundos")

con.close()
