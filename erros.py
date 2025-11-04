x = 5

try:
    print(x)
except NameError:
    print("X is not defined!")
except:
    print("Ocorreu um erro")
else:
    print("Nada deu errado") # Código a ser executado casa não haja erros
finally:
    print("Saída ao final do try, independente de erros") # Código a ser executado ao fim do try

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") # Para o programa e retorna e mensagem através do console

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed") # 

# ValueError	Valor inválido, mas tipo correto (ex: converter texto não numérico para número)
# TypeError	Operação com tipos incompatíveis (ex: somar número com string)
# IndexError	Índice fora dos limites em listas/tuplas
# KeyError	Chave não encontrada em dicionário
# FileNotFoundError	Arquivo não existe no caminho passado
# IOError / OSError	Problemas gerais com arquivos e sistema
# ZeroDivisionError	Divisão por zero
# NameError	Variável não declarada ou não acessível
# AttributeError	Atributo/método não existe no objeto
# ImportError / ModuleNotFoundError	Falha ao importar módulo
# RuntimeError	Erros de execução genéricos
# PermissionError	Sem permissão para acessar algo