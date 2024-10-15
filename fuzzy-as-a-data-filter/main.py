import pandas as pd
from rapidfuzz import process, fuzz

# Frameworks populares
FRAMEWORKS_POPULARES = [
    'Django', 'Flask', 'React', 'Angular', 'Vue', 'Spring', 'Ruby on Rails', 
    'Laravel', 'TensorFlow', 'PyTorch', 'Keras', 'ASP.NET', 'Express', 
    'Svelte', 'Next.js', 'Nuxt.js', 'Ember.js', 'Bootstrap', 'jQuery', 
    'Backbone.js', 'FastAPI', 'Hug', 'Tornado', 'Bottle', 'CakePHP', 
    'CodeIgniter', 'Symfony', 'Meteor', 'Gatsby', 'Masonite', 'Phoenix', 
    'Play', 'Struts', 'Zope', 'Web2py', 'Turbogears', 'Falcon', 'Pyramid', 
    'Quasar', 'Flask-RESTful', 'Chalice', 'Scikit-Learn'
]

# Correções comuns
CORRECOES_COMUNS = {
    'falsk': 'Flask',
    'djanjo': 'Django',
    'pytroch': 'PyTorch',
    'tensoflow': 'TensorFlow',
    'angula': 'Angular',
    'vue.js': 'Vue',
    'react.js': 'React'
}

def corrigir_frameworks_dos_usuarios(linha):
    """Esta função corrige os frameworks dos usuários utilizando correspondência aproximada de texto e substituições 
    para erros comuns utilizando a lógica fuzzy como método de comparação e extração.""" 

    frameworks_corrigidos = []    
    for erro, correto in CORRECOES_COMUNS.items():
        linha = linha.replace(erro, correto).replace(erro.lower(), correto)

    linha_lower = linha.lower()
    palavras = linha_lower.split()
    for palavra in palavras:
        resultado = process.extractOne(palavra, [f.lower() for f in FRAMEWORKS_POPULARES], scorer=fuzz.ratio)
        if resultado and resultado[1] >= 60:
            frameworks_corrigidos.append(FRAMEWORKS_POPULARES[[f.lower() for f in FRAMEWORKS_POPULARES].index(resultado[0])])
    frameworks_ordenados = sorted(set(frameworks_corrigidos))
    return ', '.join(frameworks_ordenados)

data = {
    'comentarios': [
        'estou aprendendo Flask',
        'React e Django',
        'trabalho com PyTorch e TensorFlow',
        'adoro falsk e React',
        'estou estudando o framework Expres',
        'FastAPI, Flask',
        'minha biblioteca favorita é a Scikit-Learn',
        'Angular e Vue.js em projetos recentes',
        'gosto muito de Laravel e Ruby on Rails',
        'recentemente comecei a usar o framework Spring',
        'estou explorando o que o Djanjo pode fazer',
        'gosto de trabalhar com Pytorch, mas também com tensoflow',
        'minhas ferramentas preferidas são flask e express',
        'ultimamente tenho estudado a biblioteca Keras',
        'adoro a simplicidade do Angula',
        'uso React e outras bibliotecas para front-end'
    ]
}

df = pd.DataFrame(data)
df['frameworks_corrigidos'] = df['comentarios'].apply(corrigir_frameworks_dos_usuarios)
print(df)

# Saída
"""                                       comentarios frameworks_corrigidos
0                              estou aprendendo Flask                 Flask
1                                      React e Django         Django, React
2                   trabalho com PyTorch e TensorFlow   PyTorch, TensorFlow
3                                 adoro falsk e React          Flask, React
4                  estou estudando o framework Expres               Express
5                                      FastAPI, Flask        FastAPI, Flask
6          minha biblioteca favorita é a Scikit-Learn          Scikit-Learn
7               Angular e Vue.js em projetos recentes   Angular, React, Vue
8              gosto muito de Laravel e Ruby on Rails        Keras, Laravel
9      recentemente comecei a usar o framework Spring        Quasar, Spring
10         estou explorando o que o Djanjo pode fazer           Django, Vue
11  gosto de trabalhar com Pytorch, mas também com...   PyTorch, TensorFlow
12  minhas ferramentas preferidas são flask e express        Express, Flask
13      ultimamente tenho estudado a biblioteca Keras                 Keras
14                     adoro a simplicidade do Angula               Angular
15      uso React e outras bibliotecas para front-end                 React
"""