# example module
dictionary_list = {"kitap": "book",
                   "bilgisayar": "computer",
                   "programlama": "programming"}


def find(word):
    err = "{} not found in dictionary!"
    return dictionary_list.get(word, err.format(word))


def add(word, anlam):
    info = "{} added to dictionary!"
    dictionary_list[word] = anlam
    print(info.format(word))


def delete(word):
    try:
        dictionary_list.pop(word)
    except KeyError as err:
        print(err, "word not found!")
    else:
        print("{} deleted from dictionary!".format(word))
