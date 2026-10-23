--valor total por conta e dia
SELECT 
id_conta conta,
CAST(data_hora AS DATE) dia,
sum(valor) valor_total
FROM transacoes
GROUP BY 1,2
ORDER BY 1,2

--quantidade de transações
SELECT COUNT(id_transacao) qtde_trans
FROM transacoes

--contas sem movimentação
SELECT c.id_conta
FROM contas c
LEFT JOIN transacoes t
ON c.id_conta = t.id_conta
WHERE t.id_conta IS NULL

--saldo líquido (créditos menos débitos)
SELECT
    id_conta,
    COALESCE(SUM(valor) FILTER (WHERE tipo = 'credito'), 0)
    -
    COALESCE(SUM(valor) FILTER (WHERE tipo = 'debito'), 0)
    AS saldo_liquido
FROM transacoes
GROUP BY 1
ORDER BY 1



