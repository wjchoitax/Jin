import pickle

with open('colors.pickle', 'rb') as file:
    favorite_colors = pickle.load(file)
    print(favorite_colors)
    print(type(favorite_colors))