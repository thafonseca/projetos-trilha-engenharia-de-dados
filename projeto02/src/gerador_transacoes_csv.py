#!/usr/bin/env python3
"""
Script para gerar linhas sintéticas de transações baseadas no modelo.
"""

import argparse
import random
from datetime import datetime, timedelta

# Configurações
CONTAS = [101, 102, 201]
TIPOS = ['credito', 'debito']
# Valores típicos de transação (baseados no modelo)
VALORES = [
    100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0,
    750.0, 800.0, 1000.0, 1200.0, 1500.0, 2000.0, 3000.0
]


def gerar_id_transacao(sequencial):
    """Gera ID da transação de forma sequencial."""
    return str(sequencial)


def gerar_id_conta():
    """Escolhe conta aleatoriamente entre as disponíveis."""
    return random.choice(CONTAS)


def gerar_data_hora(dias_atras_aleatorio, horas_dia, minutos):
    """Gera data e hora aleatória nos últimos dias."""
    # Data: atual - dias_atras_aleatorio
    data = datetime.now() - timedelta(days=dias_atras_aleatorio)
    
    # Hora: horas_dia + alguns minutos adicionais aleatórios
    hora_total = horas_dia + minutos
    if hora_total > 23:
        data += timedelta(hours=hora_total - 23, minutes=minutos % (24 - horas_dia))
    else:
        data += timedelta(hours=horas_dia, minutes=minutos)
    
    return data.strftime('%Y-%m-%d %H:%M:%S')


def gerar_tipo_transacao():
    """Escolhe tipo da transação aleatoriamente."""
    return random.choice(TIPOS)


def gerar_valor():
    """Escolhe valor aleatório da lista de valores típicos."""
    return random.choice(VALORES)


def gerar_linha_transacao(sequencial):
    """Gera uma linha completa de transação sintética."""
    dias_atras = random.randint(1, 30)  # Últimos 30 dias
    
    # Horas típicas de transação (evitando muito madrugada)
    horas_turisticas = [9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
    hora_escolhida = random.choice(horas_turisticas)
    minuto_escolhido = random.randint(0, 59)
    
    return (
        gerar_id_transacao(sequencial),
        str(gerar_id_conta()),  # Converter para string
        gerar_data_hora(dias_atras, hora_escolhida, minuto_escolhido),
        gerar_tipo_transacao(),
        f"{gerar_valor():.1f}"  # Formato decimal com 1 casa após ponto
    )


def main():
    """Função principal do script."""
    parser = argparse.ArgumentParser(
        description='Gerar linhas sintéticas de transações CSV.',
        usage='python gerador_transacoes.py --num_linhas 50'
    )
    
    parser.add_argument(
        '--num_linhas', '-n',
        type=int,
        default=10,
        help='Número de linhas a gerar (padrão: 10)'
    )
    
    args = parser.parse_args()
    
    if args.num_linhas <= 0:
        print("Erro: --num_linhas deve ser um número positivo.")
        return
    
    # Cabeçalho do CSV
    cabecalho = 'id_transacao,id_conta,data_hora,tipo,valor'
    
    # Gerar linhas
    linhas = []
    for i in range(1, args.num_linhas + 1):
        linha = ','.join(gerar_linha_transacao(i))
        linhas.append(linha)
    
    # Construir o CSV completo
    conteudo = cabecalho + '\n' + '\n'.join(linhas)
    
    # Definir nome do arquivo com timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f'data_geracao_{timestamp}.csv'
    
    # Salvar na pasta data/raw
    caminho_saida = '/Users/thaisfonseca/projetos/mentoria-dados/projeto02/data/raw/' + nome_arquivo
    
    # Salvar arquivo
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    print(f'Geradas {args.num_linhas} linhas sintéticas.')
    print(f'Salvas em: {caminho_saida}')


if __name__ == '__main__':
    main()
