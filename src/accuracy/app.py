
def _build_dict_of_words(paragraph):

    wordslist = paragraph.split(' ')

    unique_words_list = list(set(wordslist))

    dict_of_words = {word: 0 for word in unique_words_list}

    for word in wordslist:
        dict_of_words[word] += 1

    return dict_of_words


def _compute_dict_accuracy(correct_words_dict, dictated_words_dict):
    number_of_errors = 0
    for word in correct_words_dict:
        try:
            number_of_errors += abs(
                correct_words_dict[word] - dictated_words_dict[word]
            )
        except KeyError:
            number_of_errors += correct_words_dict[word]

    correct_words_count = sum(correct_words_dict.values())
    return 100.0 * (1 - (number_of_errors / correct_words_count))


def compute_paragraph_accuracy(dictated, correct):
    return _compute_dict_accuracy(
        _build_dict_of_words(correct), _build_dict_of_words(dictated)
    )


def compute_file_accuracy(dictated_file, correct_file):
    return compute_paragraph_accuracy(dictated_file.read(), correct_file.read())






