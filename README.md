# T5-NLG-Demo

 A demo of Natural Language Generation using T5 Model

# Requirements

* [Pytorch](https://pytorch.org/) v1.6.0 or more

# Dataset

* [WebNLG 2020](https://gitlab.com/shimorina/webnlg-dataset/-/tree/master/release_v3.0) 


# How to run

* Download the dataset and run preprocess.py.

* Open train_t5_nlg_demo.ipynb in Google colab and run with GPU enabled.

* Download the generated model

* Run main.py to run the model. Pass few words to get a generated sentence.

# Example
```
Input: Arthur Morgan | born | 22nd june | 1843 | good man | help | people
Output: Arthur Morgan was born on 22nd June 1843 and was a man who helped people
```
