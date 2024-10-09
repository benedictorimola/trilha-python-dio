class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # Verifica se o objeto passado é uma instância da classe Venda.
        if isinstance(venda, Venda):
            self.vendas.append(venda)

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # Calcula o total de vendas multiplicando quantidade pelo valor.
            total += venda.quantidade * venda.valor
        return total

def formatar_valor(valor):
    return f"R$ {valor:.2f}"

def main():
    relatorio = Relatorio()
    
    for _ in range(3):
        produto = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        valor = float(input("Valor: "))
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # Exibe o total de vendas usando o método calcular_total_vendas.
    total_vendas = relatorio.calcular_total_vendas()

    total_vendas
    print(f"Total de Vendas: {formatar_valor(total_vendas)}")
    
if __name__ == "__main__":
    main()
