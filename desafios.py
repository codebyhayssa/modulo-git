import re
"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Beeem-vindo ao Desafio de Git!"
    """
    
    mensagem = "Sejam bem-vindos"
    return mensagem
    


def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    """
    return ["git init", "git add", "git commit", "git status", "git push"]

def criar_mensagem_commit(lista_comandos):
    """
    Recebe uma lista de comandos e retorna mensagens de commit padronizadas.
    """
    mensagens = [f"Comando básico a seguir : {comando}" for comando in lista_comandos]
    return mensagens

# Teste das funções
comandos = listar_comandos_git_basicos()
mensagens = criar_mensagem_commit(comandos)

for mensagem in mensagens:
    print(mensagem)

def verificar_tag_valida(tag):
    """Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False."""
    return bool(re.fullmatch(r"v\d+\.\d+", tag))

print(verificar_tag_valida("v2.1")) 
print(verificar_tag_valida("v10.5")) 
print(verificar_tag_valida("v1")) 
print(verificar_tag_valida("1.0"))



