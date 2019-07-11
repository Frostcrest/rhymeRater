# rhymeRater
rhymeRater is a lightweight rhyme analyzer. Text can be input and analyzed to determine if it rhymes.



~==Architecture==~

The foundation of rhymeRater is the phonetic dictionary. If a word has the same phonetic value based on the position in the text input, then a positive value will be assigned to that match. 


~==Roadmap==~

The following features are planned:

GUI input
Text file import
Rhyme Style classification 
  * for instance, analyzing a song for similarity with "Rhyme Style of Eminem" would analyze the input to see how similar the rhyme style is to the trained neural network
Emotional Disposition
  * For each key item in the dictionary (yes, I realize, big undertaking) an emotion will be assigned. This will be ultimately used to find a synonymn for a certain word that has a different emotional meaning
Synonymn Optimization
  * For a given text input, optimize it in order to maximize the rhymeScore. This will use a combination Synonymn Dictionary and Phonetic Dictionary to cycle through all given Synonymns for a certain word and select one that has the highest rhymeScore
