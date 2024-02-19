import spacy


# PRACTICAL TASK 1

# code from the pdf file
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f'{sentence} - {similarity}')

'''
What I noticed about the similarities between cat, monkey and banana and think of an example of your own:

Cat and Monkey - similarity: 0.59
This number indicates a certain semantic similarity between "cat" and "monkey". 
Perhaps this is due to the fact that both of these animals are mammals.

Cat and Banana - similarity: 0.22
Low similarity indicates that, from the point of view of semantics, 
the words "cat" and "banana" do not have much in common. 
This is due to the fact that one word refers to an animal, and the other to a fruit.

Monkey and Banana - similarity: 0.40
This number may indicate that there is some association between the monkey and the banana, 
perhaps due to traditional depictions of monkeys holding bananas. 
However, the similarity is less than in the case of "cat" and "monkey", 
which may indicate a less close connection between these concepts.
'''

# my example
word4 = nlp("car")
word5 = nlp("airplane")
word6 = nlp("tree")

print(f'Similarity between {word4} and {word5} {word4.similarity(word5)}')
print(f'Similarity between {word5} and {word6} {word5.similarity(word6)}')
print(f'Similarity between {word6} and {word4} {word6.similarity(word4)}')

'''
Run the example file on with the simpler language model 'en_core_web_sm'
and write a note on what you notice may be different from the model 'en_core_web_md'

After running the example file on with the 'en_core_web_sm' language model, I got UserWarning: [W007] error. 
This error indicates that this model does not have word vectors loaded. 
Vector representations of words are numerical representations of words in space 
that allow to measure the semantic similarity between them.
The message states that the Doc.similarity method will be based on the tagger, parser, 
and Named Entity Recognition (NER) rather than vector representations of words. 
So, for performing the given task, which is measuring semantic similarity between words,
the model 'en_core_web_md' is more effective because it contains vector representations of words.
'''

# PRACTICAL TASK 2
'''
Create a function to return which movies a user would watch next if they have watched Planet Hulk with the description
The function should take in the description as a parameter and return the title of the most similar movie.
'''

from pathlib import Path


def what_to_watch_next(description):

    rating = {}
    token = nlp(description)

    for key, value in movies.items():
        token_ = nlp(value)
        rating.update({key: float(token.similarity(token_))})

    return max(rating, key=rating.get)


# I assume that the movies.txt file is in the current directory
path = Path.cwd()
file_name = 'movies.txt'
file_path = path / file_name

movies = {} # dictionary with the movies and their descriptions to choose

# read the file movies.txt
with open(file_path, 'r') as fh:
    while True:
        line = fh.readline()
        if not line:
            break

        line = line.replace('\n', '').replace("isn\'t", "is not").split(' :')
        dictionary = {line[0]: line[1]}
        movies.update(dictionary)

if __name__ == "__main__":
    planet_hulk = '''Will he save their world or destroy it?
    When the Hulk becomes too dangerous for the Earth,
    the Illuminati trick Hulk into a shuttle and launch him into space to a
    planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
    planet Sakaar where he is sold into slavery and trained as a gladiator.'''

    next_movie = what_to_watch_next(planet_hulk)

    print('\n---------------TASK 2----------------')
    print('The user would watch next:', next_movie)