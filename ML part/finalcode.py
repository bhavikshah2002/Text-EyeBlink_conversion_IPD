from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import pickle
modelapna = load_model('model.h5')
tokenizerapna = pickle.load(open('finaltoken.pkl', 'rb'))
vocab_array = np.array(list(tokenizerapna.word_index.keys()))
def make_predictions(text, n_words):
    for i in range(n_words):
        text_tokenize = tokenizerapna.texts_to_sequences([text])
        text_padding  = tf.keras.preprocessing.sequence.pad_sequences(text_tokenize, maxlen = 49)
        prediction = np.squeeze(np.argmax(modelapna.predict(text_padding), axis = -1))
        prediction = str(vocab_array[prediction - 1])
        text += " " + prediction
    return text

print(make_predictions('crime',2))
