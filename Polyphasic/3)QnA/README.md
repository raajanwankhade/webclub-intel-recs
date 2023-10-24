# Task 2C : Building a Closed and Extractive Question and Answer Language model based on provided Context

## Notebook Description
1. <big>WECREC_distilbert_qna.ipynb</big>
- This notebook is an attempt at fine-tuning distilbert on squad. Which has been successful, but had to train on a smaller subset of the original squad dataset due to resources and time contraints. The answers were correct in some cases but in some complex cases, the start and end indices were not predicted properly (i.e. we just got wrong answers).

2. <big>WECREC_distilbert_squad.ipynb</big>
- In this notebook I perform the QnA using distilbert model which has been finetuned already on the squad dataset.
- I had then decided to continue with this model in the final ML system as it provided better results and seemed to be working well even in some slightly complex questions/cases.
