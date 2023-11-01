import re

def read_first_sentence_and_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            # Знаходимо перше речення за допомогою регулярних виразів
            first_sentence_match = re.search(r'[^.!?]*[.!?]', text)
            if first_sentence_match:
                first_sentence = first_sentence_match.group().strip()
                print("Перше речення:")
                print(first_sentence)

            # Витягаємо всі слова з тексту та видаляємо знаки пунктуації
            words = re.findall(r'\b\w+\b', text)
            words = [word for word in words if word.isalpha()]

            # Розділяємо слова на українські та англійські
            ukrainian_words = []
            english_words = []
            for word in words:
                if re.match(r'[а-яА-ЯіїєІЇЄґҐ]', word):
                    ukrainian_words.append(word)
                else:
                    english_words.append(word)

            # Виводимо українські слова в алфавітному порядку
            print("\nУкраїнські слова:")
            for word in sorted(ukrainian_words):
                print(word)

            # Виводимо англійські слова в алфавітному порядку
            print("\nАнглійські слова:")
            for word in sorted(english_words):
                print(word)

            # Виводимо кількість слів
            print("\nКількість слів у тексті:", len(words))
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

# Запускаємо функцію з вашим файлом
read_first_sentence_and_words('text_file.txt')