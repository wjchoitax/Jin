import pickle

favorite_colors = ['red', 'blue', 'pink', 'brown']

with open('colors.pickle', 'wb') as file:
    pickle.dump(favorite_colors, file)

print('save as pickle')