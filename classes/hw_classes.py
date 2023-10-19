"""Модуль для анализа текстов"""
# Первоначально поняла запрет на использование библиотек, как полный запрет
# даже на стандартные, поэтому написала код в самом простом исполнении без
# использования Counter, re и прочих библиотек
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


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
