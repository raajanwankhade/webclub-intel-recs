# Task 2B : Developing a Translation Model for Cross-Language Communication

I have tried to use two methods to accomplish the required translation task:
- Tweaking the hyperparameters of the baseline model, trying to use LSTMs (didn't make it better), then ended up tweaking the hyperparameters like learning rate, number of layers, number of neurons in each layer, etc. and got a better translation than the baseline, but still not realistic and convincing.
- I then ended up using the MBart pretrained model from HuggingFace's transformer library for the translation task as it provided more convincing results in both English to French and also French to English translation.
