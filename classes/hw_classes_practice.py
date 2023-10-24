"""Модуль для анализа текстов"""
# Округляю числа в методах, чтобы результат соответствовал примерам в задании
from math import log
from typing import List


class CountVectorizer:
    """
    Класс для преобразования текстов в терм-матрицу слов
    :param lowercase: преобразовывать ли текст к нижнему регистру
    :param stop_words: список стоп-слов, не участвующих в анализе
    """

    def __init__(
        self,
        lowercase: bool = True,
        stop_words: List[str] = None,
    ) -> None:
        self.lowercase = lowercase
        self.stop_words = stop_words
        self.vocabulary = []

    def _check_vocabulary(self) -> None:
        """Проверка аттрибута vocabulary (существует, обучение выполнялось)"""
        if not self.vocabulary:
            raise AttributeError('Vocabulary is empty, try to fit/check data')

    @staticmethod
    def _check_params(texts) -> None:
        """Проверка параметров fit_transform"""
        if not isinstance(texts, list):
            raise ValueError('First param for fit_transform should be list')

        if not all(isinstance(text, str) for text in texts):
            raise ValueError('Texts list should contain only strings')

    def get_feature_names(self) -> List[str]:
        """
        Функция, возвращающая список слов
        return: список слов
        """
        self._check_vocabulary()
        return list(self.vocabulary)

    def fit_transform(self, texts: List[str]) -> List[List[int]]:
        """
        Функция, возвращающая терм-матрицу для полученных текстов
        :param texts: список текстов для анализа
        return: терм-матрица
        """
        self._check_params(texts)
        texts_count = len(texts)
        words_dict = {}
        for ind, text in enumerate(texts):
            if self.lowercase:
                text = text.lower()
            words = text.split()
            inique_words = set(words)
            if self.stop_words:
                inique_words.difference_update(set(self.stop_words))

            for word in inique_words:
                words_dict.setdefault(word, [0] * texts_count)
                words_dict[word][ind] = words.count(word)

        sorted_words_dict = dict(sorted(words_dict.items()))
        self.vocabulary = sorted_words_dict.keys()

        words_count = sorted_words_dict.values()
        term_matrix = [[x[i] for x in words_count] for i in range(texts_count)]
        return term_matrix


class TfidfTransformer:
    """Класс для преобразования матриц частот в tfidf-матрицу"""

    def tf_transform(self, term_matrix: List[List[int]]) -> List[List[float]]:
        """
        Функция для вывода матрицы относительных частот для слов
        :param term_matrix: терм-матрица (nxm) частот повторений слов
        :return: матрица (nxm) относительных частот
        """
        result = []
        for count_list in term_matrix:
            sum_count = sum(count_list)
            result.append([round(x/sum_count, 3) for x in count_list])

        return result

    def idf_transform(self, term_matrix: List[List[int]]) -> List[List[float]]:
        """
        Функция для вывода списка частот появления слов в документах
        :param term_matrix: терм-матрица (nxm) частот повторений слов
        :return: вектор (1xm) частот появления слов в документах
        """
        count_doc = len(term_matrix)
        idf_matrix = []
        for word_docs in zip(*term_matrix):
            docs_with_word = sum([bool(count > 0) for count in word_docs])
            idf_matrix.append(
                round(log((count_doc + 1) / (docs_with_word + 1)) + 1, 3)
            )

        return idf_matrix

    def fit_transform(self, term_matrix: List[str]) -> List[List[int]]:
        """
        Функция, возвращающая tfidf-матрицу для полученных текстов
        :param matrix: матрица частот слов
        return: tfidf-матрица
        """
        tf_matrix = self.tf_transform(term_matrix)
        idf_matrix = self.idf_transform(term_matrix)
        len_range = range(len(idf_matrix))
        tfidf_matrix = []
        for tf_row in tf_matrix:
            tfidf_matrix.append(
                [round(tf_row[i] * idf_matrix[i], 3) for i in len_range]
            )
        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    """Класс для преобразования текстов в tfidf-матрицу"""

    def __init__(self) -> None:
        super().__init__()
        self.tfid_transformer = TfidfTransformer()

    def fit_transform(self, texts: List[str]) -> List[List[int]]:
        term_matrix = super().fit_transform(texts)
        return self.tfid_transformer.fit_transform(term_matrix)


if __name__ == '__main__':
    # Задание 1
    # Реализуйте класс CountVectorizer, имеющий метод fit_transform
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print('\nЗадание 1. CountVectorizer')
    print(vectorizer.get_feature_names())
    print(count_matrix)

    # Задание 2
    # Реализуйте функцию tf_transform
    transformer = TfidfTransformer()
    print('\nЗадание 2. tf_transform')
    print(transformer.tf_transform(count_matrix))

    # Задание 3
    # Реализуйте функцию idf_transform
    print('\nЗадание 3. idf_transform')
    print(transformer.idf_transform(count_matrix))

    # Задание 4
    # Реализуйте класс TfidfTransformer, имеющий метод fit_transform
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print('\nЗадание 4. TfidfTransformer')
    print(tfidf_matrix)

    # Задание 5
    # Реализуйте класс TfidfVectorizer, имеющий метод fit_transform
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print('\nЗадание 5. TfidfVectorizer')
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
