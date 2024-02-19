import spacy


gardenpathSentences = ['The bird flew into the window and broke.',
                       'The chef cooking dinner in the restaurant is known for his expertise.']

# Add more sentences to the list
gardenpathSentences.extend(['Mary gave the child a Band-Aid.',
                            'That Jill is never here hurts.',
                            'The cotton clothing is made of grows in Mississippi.'])

nlp = spacy.load('en_core_web_sm')

# Tokenize each sentence in the list
list_of_tokenized_sentences = [nlp(sentence) for sentence in gardenpathSentences]

# Perform named entity recognition
named_entities = [(ent.text, ent.start_char, ent.end_char, ent.label_) 
                  for sentence in list_of_tokenized_sentences 
                  for ent in sentence.ents]

# Examine how spaCy has categorised each sentence
for entity in named_entities:
    print(entity)

print(spacy.explain("GPE"))
print(spacy.explain("PERSON"))

'''
What was the entity and its explanation that you looked up?
1. Searched for the entity "GPE" and its explanation is "Countries, cities, states"
2. Searched for the entity "PERSON" and its explanation is "People, including fictional"

Did the entity make sense in terms of the word associated with it?
1. Yes, it refers to geopolitical entities such as countries, cities, or states.
2. Yes, it refers to named persons, including real people and fictional characters.
'''