#!/usr/local/bin/python3
#
# 
#
# SeekTruth.py : Classify text objects into two categories
#
# Names and userIDs - Vedika Shinde (vshinde), Gayatri Gattani (ggattani), & Rishikesh Kakde (rkakde)
#

import sys
from collections import defaultdict
import re

def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(parsed[1] if len(parsed)>1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}

def classifier(train_data, test_data):
    # Extract data from the input dictionaries
    train_obj, train_lbls = train_data["objects"], train_data["labels"]
    classes, cls_priors = train_data["classes"], {}

    # Creating defaultdicts to store word frequencies and class counts values
    word_classes, class_counts = defaultdict(lambda: defaultdict(int)), defaultdict(int)

    # to Calculate class priors and word counts
    i = 0
    while i < len(train_obj):
        all_words = re.findall(r'\w+', train_obj[i].lower())
        cur_class = train_lbls[i]
        class_counts[cur_class] = class_counts[cur_class] +1
        j = 0
        while j < len(all_words):
            word_classes[all_words[j]][cur_class] += 1
            j += 1
        i += 1

    total_documents = len(train_obj)
    for each_class in classes:
        # here we calculate and store class priors
        x = class_counts[each_class] / total_documents
        cls_priors[each_class] = x

    # apply the Naive Bayes classifier
    res_predictions = list()
    i = 0
    while i < len(test_data["objects"]):
        test_object = test_data["objects"][i]
        words_in_test_obj = re.findall(r'\w+', test_object.lower())
        class_scores = {cls: cls_priors[cls] for cls in classes}
        j = 0
        while j < len(words_in_test_obj):
            word = words_in_test_obj[j]
            for cls in classes:

                y = (word_classes[word][cls] + 1) / (class_counts[cls] + len(word_classes))   # Compute likelihood
                class_scores[cls] *= y
            j += 1

        # update pred_class with the class with maximum score
        pred_class = max(class_scores, key=class_scores.get)
        res_predictions.append(pred_class)
        i += 1

    return res_predictions


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)
    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"], "classes": test_data["classes"]}

    results= classifier(train_data, test_data_sanitized)

    # calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))
