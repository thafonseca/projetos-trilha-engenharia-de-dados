import duckdb

con = duckdb.connect("projeto02/banco.duckdb")


print(con.execute("SELECT * FROM transacoes").fetchdf())

con.close()