import os

PRE_PROCESS_ORIGINAL_SENTENCES = False
ORIG_SENT_FILE_NAME = "original_but_sentences"
CLEAN_SENT_FILE_NAME = "clean_sentences"
ORIGINAL_BUT_SENTENCES_PATH = os.path.join(os.getcwd(), ORIG_SENT_FILE_NAME)
CLEAN_SENT_FILE_LOCATION = os.path.join(os.getcwd(), CLEAN_SENT_FILE_NAME)
SENTENCE_TYPE_DELIMITER = "####$$$$####%%%%%#####|||||"

LOG = True
