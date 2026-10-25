import duckdb

con = duckdb.connect("projeto02/banco.duckdb")

df = con.execute("SELECT * FROM transacoes").fetchdf()

df.to_csv("projeto02/transacoes.csv", index=False)

print("Arquivo CSV exportado com sucesso!")

con.close()