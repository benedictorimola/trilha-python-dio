class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        """Adiciona uma venda à lista de vendas da categoria."""
        self.vendas.append(venda)

    def total_vendas(self):
        """Calcula e retorna o total das vendas para esta categoria."""
        total = sum(venda.valor for venda in self.vendas)
        return total

def formatar_valor(valor):
    return f"R$ {valor:.2f}"

def main():
    categorias = []

    while True:
        nome_categoria = input("Nome da Categoria (ou 'sair' para encerrar): ")
        if nome_categoria.lower() == 'sair':
            break
        categoria = Categoria(nome_categoria)

        for _ in range(2): 
            entrada_venda = input("Venda (Produto, Quantidade, Valor): ")
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        total = categoria.total_vendas()
        print(f"Vendas em {categoria.nome}: {formatar_valor(total):.1f}")
        
if __name__ == "__main__":
    main()
