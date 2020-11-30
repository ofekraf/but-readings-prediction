from env import *
import re

def log(msg):
    if LOG:
        print(msg)


def should_use_sentence(sentence):
    return "but" in sentence and sentence[0].isalpha()

def clean_original_sentences():
    clean_sentences_to_write = []
    with open(ORIGINAL_BUT_SENTENCES_PATH) as reader:
        for line in reader:
            splitted = re.split('[.!]',line)
            for sentence in splitted:
                sentence = sentence.strip("\n").strip(" ").strip("but")
                if should_use_sentence(sentence):
                    clean_sentences_to_write.append(sentence)

    with open(CLEAN_SENT_FILE_LOCATION, 'w') as writer:
        for sentence in clean_sentences_to_write:
            if sentence:
                writer.write(sentence+SENTENCE_TYPE_DELIMITER+"\n")



def main():
    if PRE_PROCESS_ORIGINAL_SENTENCES:
        clean_original_sentences()



if __name__ == '__main__':
    main()