import subprocess

print("Installation de transformateurs.")
subprocess.run(["pip", "install", "transformers", "--quiet"])
subprocess.run(["pip", "install", "sentencepiece", "--quiet"])

print("Importation des packages requis.")
from transformers import DistilBertTokenizer, TFDistilBertForQuestionAnswering, MBartForConditionalGeneration, MBart50TokenizerFast
import pandas as pd
import numpy as np
import tensorflow as tf

print("Initialisation du modèle.")
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad")
model = TFDistilBertForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")
transla_tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
transla_model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

def translate(text, src_lang, tgt_lang):
    # Set the source and target languages for the tokenizer
    transla_tokenizer.src_lang = src_lang
    transla_tokenizer.tgt_lang = tgt_lang

    # Encode the input text
    encoded_text = transla_tokenizer(text, return_tensors="pt")

    # Generate the translation
    generated_tokens = transla_model.generate(**encoded_text, forced_bos_token_id=transla_tokenizer.lang_code_to_id[tgt_lang])

    # Decode the generated translation and skip special tokens
    translation = transla_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    return translation

print("Welcome to OUIOUIBAGUETTE. Your context-based, and also unfortunately French QnA Assistant :)")
print("As a French assistant, I really do not care if you know French or not.\nThis is the final English sentence you'll see from me.")

stopnow = False
while not stopnow:
    context = input("Entrez le contexte: ")
    stopques = False
    while not stopques:
        question = input("Entrez votre question: ")
        inputs = tokenizer(question, context, return_tensors="tf")
        outputs = model(**inputs)

        answer_start_index = int(tf.math.argmax(outputs.start_logits, axis=-1)[0])
        answer_end_index = int(tf.math.argmax(outputs.end_logits, axis=-1)[0])
        predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
        answer = tokenizer.decode(predict_answer_tokens)
        src_lang = "en_XX"
        tgt_lang = "fr_XX"
        translated_sentence = translate(answer, src_lang, tgt_lang)
        print(translated_sentence[0])
        choice = input("Voulez-vous poser d'autres questions? [y/n]:")
        if choice == 'n':
            stopques = True
    choice2 = input("Souhaitez-vous utiliser un autre contexte pour les questions? [y/n]:")
    if choice2 == 'n':
        stopnow = True
        print("Merci de m'avoir utilisé!")




