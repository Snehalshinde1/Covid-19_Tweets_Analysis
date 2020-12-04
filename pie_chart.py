import pandas as pd
import ast

def percentage(filtered_data):

    hashtags=filtered_data["hashtags"]
    hashtags_list = list(hashtags)

    preprocessed_hashtags = [x for x in hashtags_list if str(x) != 'nan']
    intermediate_hastags=[]
    for  each_hastags in preprocessed_hashtags:
        each_hastags = ast.literal_eval(each_hastags)
        intermediate_hastags.append(each_hastags)


    final_hashtags=[]
    for each_hashtags in intermediate_hastags:
        for hashtag in each_hashtags:
            final_hashtags.append(hashtag)
    dict_count_occurences_of_letters = {}

    for letter in final_hashtags:
        if letter in dict_count_occurences_of_letters:
            dict_count_occurences_of_letters[letter] += 1
        else:
            dict_count_occurences_of_letters[letter] = 1



    hastags = list(dict_count_occurences_of_letters.keys())
    hastags_count = list(dict_count_occurences_of_letters.values())

    return hastags, hastags_count




