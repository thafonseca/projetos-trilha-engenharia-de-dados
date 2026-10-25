import duckdb

con = duckdb.connect("projeto02/banco.duckdb")

# Inserindo dados na tabela clientes
con.execute("""
INSERT INTO clientes (id_cliente, nome_ficticio)
VALUES
    (1, 'Ana Silva'),
    (2, 'José'),
    (3, 'Carla Souza');
""")

# Inserindo dados na tabela contas
con.execute("""
INSERT INTO contas (id_conta, id_cliente, status)
VALUES
    (101, 1, 'ativa'),
    (102, 1, 'ativa'),
    (201, 2, 'ativa'),
    (301, 3, 'ativa');
""")

# Inserindo dados na tabela transacoes
con.execute("""
INSERT INTO transacoes (
    id_transacao,
    id_conta,
    data_hora,
    tipo,
    valor
)
VALUES
    (1, 101, '2026-10-01 09:00:00', 'credito', 1500.00),
    (2, 101, '2026-10-01 10:30:00', 'debito', 200.00),
    (3, 101, '2026-10-02 11:00:00', 'credito', 350.00),
    (4, 102, '2026-10-02 12:00:00', 'credito', 2000.00),
    (5, 102, '2026-10-03 13:00:00', 'debito', 500.00),
    (6, 102, '2026-10-03 14:00:00', 'debito', 100.00),
    (7, 201, '2026-10-01 08:00:00', 'credito', 3000.00),
    (8, 201, '2026-10-02 15:00:00', 'debito', 750.00),
    (9, 201, '2026-10-04 16:00:00', 'credito', 400.00),
    (10, 101, '2026-10-05 09:00:00', 'credito', 800.00),
    (11, 102, '2026-10-05 10:30:00', 'debito', 250.00),
    (12, 201, '2026-10-06 14:00:00', 'credito', 1200.00);
""")

# Consultando os dados inseridos
print("Consultando tabela clientes:")
print(con.execute("SELECT * FROM clientes").fetchdf())

print("\nConsultando tabela contas:")
print(con.execute("SELECT * FROM contas").fetchdf())

print("\nConsultando tabela transacoes:")
print(con.execute("SELECT * FROM transacoes").fetchdf())

# Consultando quantidade de transações por tipo
print("\nQuantidade de transações por tipo:")
print(con.execute("""
    SELECT * AS quantidade
    FROM transacoes
""").fetchdf())

con.close()