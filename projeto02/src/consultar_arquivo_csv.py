import duckdb

con = duckdb.connect("projeto02")


print(con.execute("""
    SELECT *
    FROM read_csv_auto('data_geracao_20261024_181802.csv')
""").fetchdf())