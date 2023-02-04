<h1 align="center">
<br>
  <img src="https://www.efficy.com/wp-content/uploads/2018/12/chatbot-et-centre-appel.jpg" alt="Front-End Checklist" >
  <br>
    <br>
  Chatbot with Pytoch and Tkinter
  <br>
</h1>
#### Author: Salma OUARDI

---
As an AI Engineer intern I was able to leverage my NLP and Deep Learning skills to create an NLP-powered chatbot for the company's website.

---
#### Tasks / Achievements
* Designed and built a Chatbot for the company's website with the help of NLP And Deep Learning.
* Conducted extensive data preprocessing utilizing the Natural Language Toolkit (NLTK) to format and prepare data for input into the neural network.
* Constructed a comprehensive knowledge base, incorporating information sourced from company databases for integration into the chatbot's intents file.
* Implemented a multi-layer feed-forward neural network using PyTorch, trained the model to achieve optimal performance, and created a user-friendly graphical interface for the chatbot using Tkinter.

---

## Installation

### Create an environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activate it
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
```
### Install PyTorch and dependencies

For Installation of PyTorch see [official website](https://pytorch.org/).

You also need `nltk`:
 ```console
pip install nltk
 ```

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python chat.py
```