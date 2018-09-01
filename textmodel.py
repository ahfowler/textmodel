import math

def clean_text(txt):
    """ Removes conclusive punctuaction and converts characters to lowercase. """

    cleaned_txt = ''
    for character in txt:
        if character not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXWY ': #punctuation
            character = ''
            cleaned_txt += character
        elif character == character.upper(): #uppercase
            character = character.lower()
            cleaned_txt += character
        else:
            cleaned_txt += character
    return cleaned_txt

def stem(s):
        """ Returns the stem of string s. """
        #special words
        double_cons = ['see', 'off', 'egg'] 

        vowels = ['a','e', 'i', 'o', 'u']

        suffix = [['s', 'y'],
                 ['ly', 'ic', 'er', 'or', 'ed', 'al', 'ny'],
                 ['ial', 'ful', 'ing', 'ion', 'ity', 'ive', 'ous', 'ies', 'ier', 'ily',
                  'ish', 'ism', 'dom', 'ist', 'ate', 'men'],
                 ['able', 'ible', 'tion', 'less', 'ment', 'ness', 'eous', 'ious', 'ical', 'ship']]

        if len(s) <= 4:
            return s

        #last four
        if len(s) > 5 and s[-4:] in suffix[3]:
            if s[-5] == s[-6]:
                if s[-5] == 's': #"ss"
                    return s[:-4]
                return s[:-5]
            else:
                s = s[:-4]
                return s
            
       #last three
        elif s[-3:] in suffix[2]:
            if s[-4] == s[-5]:
                if s[-4] in ['s', 'l', 'z', 'f']:
                    return s[:-3]
                elif s[:-3] in double_cons:
                    return s[:-3]
                return s[:-4]
            else:
                return s[:-3]
        #last two
        elif s[-2:] in suffix[1]:
            if s[-3] == s[-4]:
                if s[-3] in ['s', 'l', 'z', 'f']:
                    return s[:-2]
                return s[:-3]
            else:
                return s[:-2]

        #plurals and y
        if s[-1] in suffix[0]:
            if s[-2:] == 'es':
                return s[:-2]
            if s[-2] == 's':
                return s
            if s[-2] in vowels: #y
                return s
            elif s[-1] == 's':
                s = stem(s[:-1])
                return s

        return s

def sentence_length(paragraph):
    """ Figures out a sentence lengths. """
    paragraph = paragraph.replace("!", ".")
    paragraph = paragraph.replace("?", ".")
    paragraph = paragraph.replace('"', "")
    paragraph = paragraph.replace("-", "")
    final = paragraph.split(".")
    lengths = []
    for sentence in final[:-1]:
        sentence = sentence.split(" ")
        lengths += [len(sentence)]
    return lengths
              
class TextModel:
    """ Makes a TextModel. """

    def __init__(self, model_name):
        """ List of style sigatures for TextModel. """
        self.name = str(model_name)
        self.numwords = 0
        self.words = {} #how many types of words
        self.word_lengths = {} #how many word lengths
        self.stems = {} #how many stems
        self.sentence_lengths = {} #how many sentence lengths
        self.common_word = [] #top ten most common words

    
    def __repr__(self):
        """ Return a string representation of the TextModel. """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  most common words: ' + str(self.common_word) + '\n'

        return s

    def add_string(self, s):
        """ Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model. """

        #sent_lengths
        sent_len = sentence_length(s)
        for sentences in sent_len:
            if sentences not in self.sentence_lengths:
                self.sentence_lengths[sentences] = 1
            elif sentences in self.sentence_lengths:
                self.sentence_lengths[sentences] += 1
 
        s = clean_text(s)
        word_list = s.split(' ')

        for w in word_list:
            self.numwords += 1
            # frequency of words
            if w not in self.words:
                self.words[w] = 1
            elif w in self.words:
                self.words[w] += 1
            # freqency of length of words
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            elif len(w) in self.word_lengths:
                self.word_lengths[len(w)] += 1
            #word stemming
            word_stem = stem(w)
            if word_stem not in self.stems:
                self.stems[word_stem] = 1
            elif word_stem in self.stems:
                self.stems[word_stem] += 1

        # ten most common words
        a = list(self.words)
        maximum_count = self.words[a[0]] 
        for word in a:
            if self.words[word] > maximum_count:
                maximum_count = self.words[word]
        count = 1
        cw_list = []
        while count <= maximum_count:
            for word in a:
                if self.words[word] == count:
                    cw_list = [word] + cw_list
            count += 1

        self.common_word = cw_list[:10]
                
        #simplify stemlist
        a = list(self.stems)
        for x in range(len(a)):
            for y in a[x+1:]:
                if y[:4] == a[x][:4]:
                    self.stems[a[x]] += self.stems[y]
                    del self.stems[y]
                    a.remove(y)

    def add_file(self, filename):
        """ Adds all text of a file. """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        
        self.add_string(text)

    def save_model(self):
        """ This saves the TextModel object to a textfile with its style signatures. """
        # words dictionary
        filename = self.name + "_words"
        f = open(filename, 'w')
        f.write(str(self.words))
        f.close()

        # word_lengths dictionary
        filename = self.name + "_word_lengths"
        f = open(filename, 'w')
        f.write(str(self.word_lengths))
        f.close()

        # stems dictionary
        filename = self.name + "_stems"
        f = open(filename, 'w')
        f.write(str(self.stems))
        f.close()

        # sentence_lengths dictionary
        filename = self.name + "_sentence_lengths"
        f = open(filename, 'w')
        f.write(str(self.sentence_lengths))
        f.close()

        # ten most common words
        filename = self.name + "_common_word"
        f = open(filename, 'w')
        f.write(str(self.common_word))
        f.close()

    def read_model(self):
        """ Converts files with dictionaries to actual dictionaries. """
        
        # words dictionary
        f = open(self.name + "_words", 'r') 
        d_str = f.read()
        f.close()
        
        d = dict(eval(d_str))
        self.words = d

        # word_lengths dictionary
        f = open(self.name + "_word_lengths", 'r') 
        d_str = f.read()
        f.close()
        
        d = dict(eval(d_str))
        self.word_lengths = d

        # stems dictionary
        f = open(self.name + "_stems", 'r') 
        d_str = f.read()
        f.close()
        
        d = dict(eval(d_str))
        self.stems = d

        # sentence_lengths dictionary
        f = open(self.name + "_sentence_lengths", 'r') 
        d_str = f.read()
        f.close()
        
        d = dict(eval(d_str))
        self.sentence_lengths = d

        # ten most common words
        f = open(self.name + "_common_word", 'r') 
        d_str = f.read()
        f.close()
        
        d = list(eval(d_str))
        self.common_word = d

    def similarity_scores(self, other):
        """ Computes are returns a list of log similarity scores of self and other. """
        word_score = compare_dictionaries(other.words, self.words)
        word_length_score = compare_dictionaries(other.word_lengths, self.words)
        stem_score = compare_dictionaries(other.stems, self.stems)
        sentence_length_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        common_word_score = compare_lists(other.common_word, self.common_word)

        return [word_score, word_length_score, stem_score, sentence_length_score, common_word_score]

    def classify(self, source1, source2):
        """ Determines which source is more like self. """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)

        print("scores for", source1.name, ":", [round(number, 2) for number in scores1])
        print("scores for", source2.name, ":", [round(number, 2) for number in scores2])

        s1 = 0
        s2 = 0
        for x in range(len(scores1)):
            if scores1[x] >= scores2[x]:
                s1 += 1
            else:
                s2 += 1
        
        if s1 > s2:
            print(self.name, "is more likely to have come from ", source1.name)
            print()
        else:
            print(self.name, "is more likely to have come from ", source2.name)
            print()
        

                
def compare_dictionaries(d1, d2):
    """ Compares the similarity scores of two dictionaries. """
    score = 0
    total = 0

    for element in d1:
        total += d1[element]

    for item in d2:
        if item in d1:
            score += math.log(d1[item]/total) * (d2[item])
        else:
            score += math.log(0.5/total) * (d2[item])
    return score

def compare_lists(l1, l2):
    """ Compares similarity scores of two lists. """
    score = 0
    total = len(l1)
    weight = 110

    for item in range(len(l2)):
        if item in range(len(l1)):
            score += math.log(weight/total) * (weight)
        else:
            score += math.log(0.5/total) * (1)
        weight -=  10
    return score


def run_tests():
    """ This compares texts to Barack Obama and Donald Trump. """
    source1 = TextModel("Barack Obama")
    source1.add_file('source_texts/barackobama_source_text.txt')

    source2 = TextModel('Donald Trump')
    source2.add_file('source_texts/donaldtrump_source_text.txt')

    new1 = TextModel('More Obama')
    new1.add_file('source_texts/moreobama_source_text.txt')
    new1.classify(source1, source2)

    new2 = TextModel('More Trump')
    new2.add_file('source_texts/moretrump_source_text.txt')
    new2.classify(source1, source2)

    new1 = TextModel('Gucci Gang by Lil Pump')
    new1.add_file('source_texts/guccigang_source_text.txt')
    new1.classify(source1, source2)

    new1 = TextModel("Spongebob Transcripts")
    new1.add_file('source_texts/spongebobeps_source_text.txt')
    new1.classify(source1, source2)
