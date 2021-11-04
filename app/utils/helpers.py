# algumas queries só suportam até 10 valores de comparação, então fazemos a query repetidamente até pegar todos os valores desejados
def executar_query_extentida(referencia_colecao, ids: list[str], parametro_query: str, operacao_query: str) -> list:
    QUANTIDADE_MAXIMA = 10
    documentos = []
    quantidade_IDs = len(ids)
    comeco = 0
    fim = min(QUANTIDADE_MAXIMA, quantidade_IDs)

    while fim <= quantidade_IDs and comeco != fim:
        referenciaQuery = referencia_colecao.where(parametro_query, operacao_query, ids[comeco:fim])
        documentos.extend(referenciaQuery.stream())

        comeco = fim
        fim = min(fim + QUANTIDADE_MAXIMA, quantidade_IDs)

    return documentos
