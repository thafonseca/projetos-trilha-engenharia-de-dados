CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome_ficticio VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS contas (
    id_conta INTEGER PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    status VARCHAR NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE IF NOT EXISTS transacoes (
    id_transacao INTEGER PRIMARY KEY,
    id_conta INTEGER NOT NULL,
    data_hora TIMESTAMP NOT NULL,
    tipo VARCHAR NOT NULL,
    valor DECIMAL(18,2) NOT NULL,
    FOREIGN KEY (id_conta) REFERENCES contas(id_conta)
);
