def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()  # переводимо текст у нижній регістр

    for word in spam_words:
        word = word.lower()  # переводимо кожне заборонене слово у нижній регістр
        if space_around:
            # Перевіряємо наявність слова з пробілами або на початку/кінці рядка
            if text.startswith(word + ' ') or text.endswith(' ' + word) or text.endswith(' ' + word + '.') or (' ' + word + ' ') in text or (' ' + word + '.') in text:
                return True
        else:
            # Перевіряємо наявність слова в тексті без додаткових умов
            if word in text:
                return True

    return False  # якщо жодне зі слів не знайдено
