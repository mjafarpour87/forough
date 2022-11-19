# forough

An interface to interact with NLP-based chat bot

## Project Overview
The ChatterBot library combines language corpora, text processing, machine learning algorithms, and data storage and retrieval to allow you to build flexible chatbots.
You can build an industry-specific chatbot by training it with relevant data. Additionally, the chatbot will remember user responses and continue building its internal graph structure to improve the responses that it can give.
### Attention

While ChatterBot is still a popular open source solution for building a chatbot in Python, it hasn’t been actively maintained for a while and has therefore accumulated a significant number of issues.

There are multiple forks of the project that implement fixes and updates to the existing codebase, but you’ll have to personally pick the fork that implements the solution you’re looking for and then install it directly from GitHub. A fork might also come with additional installation instructions.

To get started, however, you won’t use a fork. Instead, you’ll use a specific pinned version of the library, as distributed on PyPI. You’ll find more information about installing ChatterBot in step one.


## Prerequsites

Before you get started, make sure that you have a Python version available that works for this ChatterBot project. What version of Python you need depends on your operating system:

### Windows
  You need to use a Python version below 3.8 to successfully work with the recommended version of ChatterBot in this tutorial. You can install Python 3.7.9 using pyenv-win.
### Linux
  You should be able to run the project on Ubuntu Linux with a variety of Python versions. However, if you bump into any issues, then you can try to install Python 3.7.9, for example using pyenv.
### Mac OS
  You can run the project with a variety of Python versions. The chatbot was built and tested with Python 3.10.7 but should also run with older Python versions.

If you’ve installed the right Python version for your operating system, then you’re ready to get started.

## Step 1: Create a Chatbot Using Python ChatterBot
In this step, you’ll set up a virtual environment and install the necessary dependencies. You’ll also create a working command-line chatbot that can reply to you—but it won’t have very interesting replies for you yet.

To get started with your chatbot project, create and activate a virtual environment, then install chatterbot and pytz:
### Windows

  ```
  PS> python -m venv venv
  PS> venv\Scripts\activate
 (venv) PS> python -m pip install chatterbot==1.0.4 pytz
 ```
 ### Linux & Mac OS
 ```
 $ python -m venv venv
 $ source venv/bin/activate
 (venv) $ python -m pip install chatterbot==1.0.4 pytz
```
 
 Running these commands in your terminal application installs ChatterBot and its dependencies into a new Python virtual environment.
 After the installation is complete, running <code>python -m pip freeze </code> should bring up list of installed dependencies that’s similar to what you can find in the provided code’s <code>requirements.txt</code> file.
 
 With the installation out of the way, and ignoring some of the issues that the library currently has, you’re ready to get started! Create a new Python file, call it bot.py, and add the code that you need to get a basic chatbot up and running:
 ```
 # bot.py
from chatterbot import ChatBot
chatbot = ChatBot("Chatpot")
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
```
After importing ChatBot in line 3, you create an instance of ChatBot in line 5. The only required argument is a name, and you call this one "Chatpot". No, that’s not a typo—you’ll actually build a chatty flowerpot chatbot in this tutorial! You’ll soon notice that pots may not be the best conversation partners after all.
In line 8, you create a <code>while</code> loop that’ll keep looping unless you enter one of the exit conditions defined in line 7. Finally, in line 13, you call <code>.get_response()</code> on the ChatBot instance that you created earlier and pass it the user input that you collected in line 9 and assigned to <code>query</code>.
When you run this script, ChatterBot might download some data and language models associated with the [NLTK project](https://realpython.com/python-nltk-sentiment-analysis/). It’ll print some information about that to your console. Python won’t download this data again during subsequent runs.
### Note

The NLTK project installs the data that ChatterBot uses into a default location on your operating system:
```
    Windows: C:\nltk_data\
    Linux: /usr/share/nltk_data/
    macOS: /Users/<username>/nltk_data/
```

NLTK will automatically create the directory during the first run of your chatbot.
If you’re ready to communicate with your freshly homegrown Chatbot, then you can go ahead and run the Python file:

```
$ python bot.py
```
fter the language models are set up, you’ll see the greater than sign (>) that you defined in bot.py as your input prompt. You can now start to interact with your chat bot.
Even if your chat bot doesn’t have much to say yet, it’s already learning and growing. To test this out, stop the current session. You can do this by typing one of the exit conditions—":q", "quit", or "exit". Then start the chatbot another time. Enter a different message, and you’ll notice that the chatbot remembers what you typed during the previous run.

During the first run, ChatterBot created a SQLite database file where it stored all your inputs and connected them with possible responses. There should be three new files that have popped up in your working directory:
```
./
├── bot.py
├── db.sqlite3
├── db.sqlite3-shm
└── db.sqlite3-wal
```
ChatterBot uses the default <code>SQLStorageAdapter</code> and creates a [SQLite file database](https://github.com/gunthercox/ChatterBot/blob/1.0/chatterbot/storage/sql_storage.py#L31) unless you specify a different [storage adapter](https://chatterbot.readthedocs.io/en/stable/storage/index.html).

### Note
The main database file is <code>db.sqlite3</code>, while the other two, ending with <code>-wal</code> and <code>-shm</code>, are temporary support files.

Because you said both hello and hi at the beginning of the chat, your chat-pot learned that it can use these messages interchangeably. That means if you chat a lot with your new chatbot, it’ll gradually have better replies for you. But improving its responses manually sounds like a long process!

Now that you’ve created a working command-line chatbot, you’ll learn how to train it so you can have slightly more interesting conversations.

## Step 2: Begin Training Your Chatbot
In the previous step, you built a chatbot that you could interact with from your command line. The chatbot started from a clean slate and wasn’t very interesting to talk to.

In this step, you’ll train your chatbot using <code>ListTrainer</code> to make it a little smarter from the start. You’ll also learn about built-in trainers that come with ChatterBot, including their limitations.

Your chatbot doesn’t have to start from scratch, and ChatterBot provides you with a quick way to train your bot. You’ll use [ChatterBot’s ListTrainer](https://chatterbot.readthedocs.io/en/stable/training.html#training-via-list-data) to provide some conversation samples that’ll give your chatbot more room to grow:
```
# bot.py
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Chatpot")
trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
```
In line 4, you import <code>ListTrainer</code>, to which you pass your <code>chatbot</code> on line 8 to create <code>trainer</code>.

In lines 9 to 12, you set up the first training round, where you pass a list of two strings to <code>trainer.train()</code>. Using <code>.train()</code> injects entries into your database to build upon the graph structure that ChatterBot uses to choose possible replies.

### Note
If you pass an iterable with exactly two items to <code>ListTrainer.train()</code>, then ChatterBot considers the first item a statement and the second item an acceptable response.

You can run more than one training session, so in lines 13 to 16, you add another statement and another reply to your chatbot’s database.

If you now run the interactive chatbot once again using <code>python bot.py</code>, you can elicit somewhat different responses from it than before.

The conversation isn’t yet fluent enough that you’d like to go on a second date, but there’s additional context that you didn’t have before! When you train your chatbot with more data, it’ll get better at responding to user inputs.

The ChatterBot library comes with [some corpora](https://github.com/gunthercox/chatterbot-corpus) that you can use to train your chatbot. However, at the time of writing, there are some issues if you try to use these resources straight out of the box.

### Note

The issues come from mismatches between versions of the dependencies, as well as the Python version that you use. You can work around them, but it’ll require some fiddling on your end.

Alternatively, you could parse the corpus files yourself using [pyYAML](https://realpython.com/python-yaml/) because they’re stored as [YAML files](https://github.com/gunthercox/chatterbot-corpus/blob/master/chatterbot_corpus/data/english/computers.yml).

While the provided corpora might be enough for you, in this tutorial you’ll skip them entirely and instead learn how to adapt your own conversational input data for training with ChatterBot’s <code>ListTrainer</code>.

To train your chatbot to respond to industry-relevant questions, you’ll probably need to work with custom data, for example from existing support requests or chat logs from your company.

## Step 3: Create a shell on Chatbot training Engine

## Step 4: Installation Guide

## Conclusion

## Next Steps

## References
<ol>
  <li> [ChatterBot: Build a Chatbot With Python](https://realpython.com/build-a-chatbot-python-chatterbot/#project-overview)
  </li>
  </ol>
