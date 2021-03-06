import pickle

__author__ = 'user'


def save_to_file(var, filename='response.json'):
    file = open("output/" + filename, 'w')
    pickle.dump(var, file)
    file.close()


def extract_from_file(filename="response.json"):
    file = open("output/" + filename, 'r')
    var = pickle.load(file)
    return var