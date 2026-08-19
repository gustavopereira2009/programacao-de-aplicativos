def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    
    elif media >= 4:
        return "Recuperacao"
    
    return "Reprovado"


assert situacao_aluno(8) == "Aprovado", "Deveria ser Aprovado para nota 8"
assert situacao_aluno(6) == "Aprovado", "Deveria ser aprovado para nota 6"
assert situacao_aluno(5.9) == "Recuperacao", "Deveria ser recuperacao para nota 5.9"
assert situacao_aluno(4) == "Recuperacao", "Deveria ser recuperacao para nota 4"
assert situacao_aluno(2) == "Reprovado", "Deveria ser reprovado para nota 2"