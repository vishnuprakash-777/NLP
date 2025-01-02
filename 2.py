import re

morph_rules=[
   (r'(.*)s$',lambda root : f'{root}+N+P1'),
   (r'(.*)ed$',lambda root : f'{root}+V+Past'),
   (r'(.*)ing$',lambda root : f'{root}+V+Prog'),
   (r'(.*)er$',lambda root: f'{root}+N+Comp'),
   (r'(.*)est$',lambda root: f'{root}+N+Sup'),
]
default_rule = lambda word : f'{word}+Base'

def morphological_parse(word):
    for pattern,action in morph_rules:
        match = re.match(pattern,word)
        if match:
            root = match.group(1)
            return f'{word} --- {action(root)}'
    return f'{word} -- {default_rule(word)}'
    

    
test_words=['cats','cheaper','greatest','folded']
for word in test_words:
    print(morphological_parse(word))


    
