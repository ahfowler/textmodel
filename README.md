# TextModel
TextModel is a Python class that determines the author of a given piece of text by using dictionaries.

### Prerequisites

You must have at least Python 3 installed. If you do not, you can download the latest [version](https://www.python.org/downloads/release/python-370/).

You also need access to the command line such as Terminal for Mac OS or Command Prompt for Windows
or an Python IDE capable of running Python 3.

---

### How to Use
The follow instructions assume you are using the Python 3 Shell. For Terminal or Command Prompt isntructions, please refer to Python's instructions on running programs.

In order for TextModel to determine the author of arbitrary text, you must upload examples of their work from the author as text files. 

```
author_name = TextModel("Author Name")
author_name.add_file('author_source_text.txt')
```

Now, create a TextModel for the arbitrary text, and run it's classify() method. The parameters are any choice of two TextModel authors you previously created.

```
arbitrary_text = TextModel("Arbitrary Text")
arbitrary_text.add_file('arbitrarytext_source_text.txt')

arbitrary_text.classify(author_name1, author_name2)
```

The program will then print the similarity scores calculated by the arbitrary's TextModel for the given authors' TextModel respectively, and print out the determined author of arbitrary text.

---

## Running the tests
When using the Terminal, make sure you are not in the directory where finalproject.py is in. The directories are in this order: project > source_texts. project should contain both textmodel.py and the directory source_texts, and source_texts should contain all the text files.

In the Terminal or Command Prompt, you can run the tests as such:

```
python3 -c "import project.textmodel; project.textmodel.run_tests()"
```

### Explanation of the tests

#### Test 1: Determining the author of Barack Obama's speech.

```
scores for Barack Obama : [-27144.08, -40555.6, -27172.42, -877.56, 1284.6]
scores for Donald Trump : [-27651.06, -40136.96, -27610.36, -892.13, 1284.6]
More Obama is more likely to have come from  Barack Obama
```

#### Test 2: Determining the author of Donald Trumps's speech.

```
scores for Barack Obama : [-31056.96, -45873.88, -30738.95, -1005.24, 1284.6]
scores for Donald Trump : [-30743.24, -45400.34, -30626.4, -988.69, 1284.6]
More Trump is more likely to have come from  Donald Trump
```

#### Test 3: Determining the author of Gucci Gang by Lil Pump.

```
scores for Barack Obama : [-3278.94, -3733.69, -3284.3, -45.95, 1284.6]
scores for Donald Trump : [-3243.05, -3695.15, -3197.95, -49.21, 1284.6]
Gucci Gang by Lil Pump is more likely to have come from  Donald Trump
```

#### Test 4: Determining the author of Spongebob Squarepants Episode 1 Season 1 transcript.

```
scores for Barack Obama : [-34500.67, -45933.3, -34118.91, -2885.08, 1284.6]
scores for Donald Trump : [-34371.77, -45459.15, -33865.09, -2609.06, 1284.6]
Spongebob Transcripts is more likely to have come from  Donald Trump
```

---

## Authors

* **Azaria Fowler** - *Original Author* - fowler.azaria@gmail.com


## Acknowledgments

* This project was assigned to me by Dr. Dave Sullivan at Boston University.
