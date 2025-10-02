import json
import pymorphy2

def get_word_info(words):
    morph = pymorphy2.MorphAnalyzer()
    word_info_list = []

    for word in words:
        parsed_word = morph.parse(word)[0]
        word_info = {
            "word": word,
            "normal_form": parsed_word.normal_form,
            "tag": str(parsed_word.tag),
            "methods_stack": [str(method) for method in parsed_word.methods_stack],
            "lexeme": [{"word": lex.word, "tag": str(lex.tag)} for lex in parsed_word.lexeme]
        }
        word_info_list.append(word_info)

    return word_info_list

words = ["чуждается", "чечевицы", "чесотку"]
word_info_list = get_word_info(words)

with open('pymorphy2.json', 'w', encoding='utf-8') as file:
    json.dump(word_info_list, file, ensure_ascii=False, indent=4)
