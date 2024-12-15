import random
from wonderwords import RandomSentence

random_sentence_generator = RandomSentence()

def random_sentences():
    predefined_sentences = ["Hello", "How are you?", "I am HD"]
    generated_sentence = random_sentence_generator.sentence()
    all_sentences = predefined_sentences + [generated_sentence]
    return random.choice(all_sentences)