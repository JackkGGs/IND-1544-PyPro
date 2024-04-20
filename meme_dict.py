import time
meme_dict = {
    "nga or hard r": "a phrase for racism towards black people",
    "erm what the sigma": "other way to say erm what the fuck",
    "kys": "a short sentence for kill yourself",
}

while True:
    word = input("word? all lowercase: ")
    if word in meme_dict.keys():
        print([(word, meme_dict[word])])
        time.sleep(1)
    else:
        print("Word not found in meme dictionary.")
        time.sleep(1)
