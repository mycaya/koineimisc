import json

# Text data with abbreviations and their meanings
text_data = """
мр, жр, ср - мужской, женский, средний род;
од, но - одушевленность, неодушевленность;
ед, мн - единственное, множественное число;
им, рд, дт, вн, тв, пр, зв - падежи: именительный, родительный, дательный, винительный, творительный, предложный, звательный;
2 - обозначает второй родительный или второй предложный падежи;
св, нс - совершенный, несовершенный вид;
пе, нп - переходный, непереходный глагол;
дст, стр - действительный, страдательный залог;
нст, прш, буд - настоящее, прошедшее, будущее время;
пвл - повелительная форма глагола;
1л, 2л, 3л - первое, второе, третье лицо;
0 - неизменяемое.
кр - краткость (для прилагательных и причастий).
сравн - сравнительная форма (для прилагательных).
имя, фам, отч - имя, фамилия, отчество.
лок, орг - локативность, организация.
кач - качественное прилагательное.
вопр,относ - вопросительность и относительность (для наречий).
дфст - слово обычно не имеет множественного числа.
опч - частая опечатка или ошибка.
жарг, арх, проф - жаргонизм, архаизм, профессионализм.
аббр - аббревиатура.
безл - безличный глагол.
"""

# Mapping of Russian words to English translations
translations = {
    "мужской": "masculine",
    "женский": "feminine",
    "средний": "neuter",
    "одушевленность": "animacy",
    "неодушевленность": "inanimacy",
    "единственное": "singular",
    "множественное": "plural",
    "именительный": "nominative",
    "родительный": "genitive",
    "дательный": "dative",
    "винительный": "accusative",
    "творительный": "instrumental",
    "предложный": "prepositional",
    "звательный": "vocative",
    "второй родительный": "second genitive",
    "второй предложный": "second prepositional",
    "совершенный": "perfective",
    "несовершенный": "imperfective",
    "переходный": "transitive",
    "непереходный": "intransitive",
    "действительный": "active",
    "страдательный": "passive",
    "настоящее": "present",
    "прошедшее": "past",
    "будущее": "future",
    "повелительная форма": "imperative",
    "первое": "first person",
    "второе": "second person",
    "третье": "third person",
    "неизменяемое": "unchangeable",
    "краткость": "brevity",
    "сравнительная форма": "comparative",
    "имя": "name",
    "фамилия": "surname",
    "отчество": "patronymic",
    "локативность": "locativity",
    "организация": "organization",
    "качественное прилагательное": "qualitative adjective",
    "вопросительность": "interrogative",
    "относительность": "relative",
    "слово обычно не имеет множественного числа": "word usually has no plural",
    "частая опечатка или ошибка": "common typo or mistake",
    "жаргонизм": "jargon",
    "архаизм": "archaism",
    "профессионализм": "professionalism",
    "аббревиатура": "abbreviation",
    "безличный глагол": "impersonal verb"
}

# Parse the text data
rubrik_list = []
for line in text_data.strip().split('\n'):
    parts = line.split(' - ')
    if len(parts) == 2:
        abbreviations = parts[0].split(', ')
        meanings = parts[1].split(', ')
        for abbr, meaning in zip(abbreviations, meanings):
            english_translation = translations.get(meaning.strip(), "")
            rubrik_list.append({
                "abbreviation": abbr.strip(),
                "english": english_translation
            })

# Save to JSON file
with open('rubrik.json', 'w', encoding='utf-8') as f:
    json.dump(rubrik_list, f, ensure_ascii=False, indent=4)
