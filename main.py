def karatsuba(x, y):
    """
    Implementação do algoritmo de Karatsuba para multiplicação eficiente
    de números inteiros grandes.
    
    Args:
        x (int): Primeiro número inteiro
        y (int): Segundo número inteiro
    
    Returns:
        int: Produto de x e y
    """
    # 1. Início da função
    
    # 2. Verificação do caso base (x < 10 ou y < 10)
    if x < 10 or y < 10:
        # 3. Multiplicação direta (return x * y)
        return x * y
    
    # 4. Cálculo de n e m
    n = max(len(str(x)), len(str(y)))  
    m = n // 2                        
    divisor = 10 ** m
    
    # 5. Divisão dos números (a, b, c, d)
    a = x // divisor
    b = x % divisor
    c = y // divisor
    d = y % divisor
    
    # 6. Primeira chamada recursiva (ac = karatsuba(a, c))
    z2 = karatsuba(a, c)
    
    # 7. Segunda chamada recursiva (bd = karatsuba(b, d))
    z0 = karatsuba(b, d)
    
    # 8. Terceira chamada recursiva ((a+b)(c+d))
    z1 = karatsuba(a + b, c + d)
    
    # 9. Combinação dos resultados
    resultado_intermediario = (z1 - z2 - z0)
    
    # 10. Retorno do resultado
    return z2 * (10 ** (2 * m)) + resultado_intermediario * (10 ** m) + z0
    
    # 11. Fim da função


def main():
    """
    Função principal que executa exemplos do algoritmo de Karatsuba.
    """
    print("Algoritmo de Karatsuba - Multiplicação Eficiente")
    print("=" * 50)

    # Melhor Caso - Números pequenos
    print("Melhor Caso:")
    x1, y1 = 7, 8
    resultado1 = karatsuba(x1, y1)
    print(f"{x1} × {y1} = {resultado1}")
    print("-" * 50)

    # Caso Médio - Números de tamanho moderado
    print("Caso Médio:")
    x2, y2 = 1234, 5678
    resultado2 = karatsuba(x2, y2)
    print(f"{x2} × {y2} = {resultado2}")
    print("-" * 50)

    # Pior Caso - Números gigantes
    print("Pior Caso:")
    x3 = 12345678901234567890123456789012345678901234567890
    y3 = 98765432109876543210987654321098765432109876543210
    resultado3 = karatsuba(x3, y3)
    print(f"{x3} × {y3} = {resultado3}")
    print("-" * 50)


if __name__ == "__main__":
    main()