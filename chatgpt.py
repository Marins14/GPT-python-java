import openai

def criar_pergunta(
        OPENAI_API_KEY,
        assunto,
        tipo,
        dificuldade,
        pergunta_exemplo = None
):
    openai.api_key = OPENAI_API_KEY
    assunto = f'Elabore uma pergunta sobre: {assunto}'
    tipo = f'Ela deve ser {tipo}' + ' com 4 alternativas ' if tipo == 'Alternativa' else ''
    dificuldade = f'Seu nível de dificuldade deve ser {dificuldade}' 
    pergunta_exemplo = f'Utilize esta pergunta como exemplo: {pergunta_exemplo}' if pergunta_exemplo != None and pergunta_exemplo != '\n' else ''
    prompt = f'{assunto}.{tipo}.{dificuldade}.{pergunta_exemplo}'
    

#criar_pergunta('','java','Alternativa','dificil','\n')

