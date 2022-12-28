#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Сообщения
"""

# ######################################################################################################################
# Импорт необходимых инструментов
# ######################################################################################################################
# Подавление Warning
import warnings
for warn in [UserWarning, FutureWarning]: warnings.filterwarnings('ignore', category = warn)

from dataclasses import dataclass # Класс данных

from typing import List # Типы данных

# Персональные
from oceanai.modules.core.language import Language # Определение языка

# ######################################################################################################################
# Сообщения
# ######################################################################################################################
@dataclass
class Messages(Language):
    """Класс для сообщений

    Args:
        lang (str): Смотреть :attr:`~oceanai.modules.core.language.Language.lang`
    """

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __post_init__(self):
        super().__post_init__() # Выполнение конструктора из суперкласса

        self._metadata: List[str] = [
            self._('OCEANAI - персональные качества личности человека'),
            self._('Авторы'), self._('Сопровождающие'), self._('Версия'), self._('Лицензия')
        ]

        self._format_time: str = '%Y-%m-%d %H:%M:%S' # Формат времени

        self._invalid_arguments: str = self._('Неверные типы или значения аргументов в "{}" ...')
        self._invalid_arguments_empty: str = self._('Неверные типы или значения аргументов ...')

        self._oh: str = self._('Что-то пошло не так ... ')
        self._trouble: str = self._('Прям беда! ')

        self._unknown_err: str = self._trouble + self._('Не обработанную ошибку необходимо проанализировать и выявить '
                                                        'причину ...')

        self._som_ww: str = self._oh + self._('смотрите настройки ядра и цепочку выполнения действий ...')

        self._lock_user: str = self._('Выполнение заблокировано пользователем ...')

        self._text_runtime: str = self._('Время выполнения')

        self._download_precent: str = ' ({}%) ...'

        self._from_precent: str = self._('из')

        self._logs_save_true: str = self._('Лог файл успешно сохранен ...')
        self._logs_saves_true: str = self._('Лог файлы успешно сохранены ...')

        self._formation_model_hc: str = self._('Формирование нейросетевой архитектуры модели для получения оценок по '
                                               'экспертным признакам')
        self._load_model_weights_hc: str = self._('Загрузка весов нейросетевой модели для получения оценок по '
                                                  'экспертным признакам')
        self._load_model_weights_error: str = self._oh + self._('не удалось загрузить веса нейросетевой модели ...')
        self._model_hc_not_formation: str = self._oh + self._('нейросетевая архитектура модели для получения '
                                                              'оценок по экспертным признакам не сформирована')
        self._model_nn_not_formation: str = self._oh + self._('нейросетевая архитектура модели для получения '
                                                              'оценок по нейросетевым признакам не сформирована')
        self._models_not_formation: str = self._oh + self._('нейросетевые архитектуры моделей для получения '
                                                            'оценок по экспертным и нейросетевым признакам не '
                                                            'сформированы')
        self._formation_model_nn: str = self._('Формирование нейросетевой архитектуры для получения оценок по '
                                               'нейросетевым признакам')
        self._load_model_weights_nn: str = self._('Загрузка весов нейросетевой модели для получения оценок по '
                                                  'нейросетевым признакам')
        self._formation_models_b5: str = self._('Формирование нейросетевых архитектур моделей для получения результатов'
                                                ' оценки персональных качеств')
        self._load_models_weights_b5: str = self._('Загрузка весов нейросетевых моделей для получения результатов '
                                                   'оценки персональных качеств')

        self._concat_pred_error: str = self._oh + self._('конкатенация оценок по экспертным и нейросетевым признакам '
                                                         'не произведена')
        self._norm_pred_error: str = self._oh + self._('нормализация оценок по экспертным и нейросетевым признакам '
                                                       'не произведена')

        self._get_union_predictions_info: str = self._('Получение прогнозов')
        self._get_accuracy_info: str = self._(' и вычисление точности')

        self._load_data_true_traits_error: str = self._oh + self._('не удалось загрузить файл с верными '
                                                                   'предсказаниями для подсчета точности ...')

        self._wrong_ext: str = self._oh + self._('не указано минимум одно расширение искомых файлов ...')

        self._expert_values_not_found: str = self._oh + self._('отсутствуют экспертные оценки ...')

        self._get_union_predictions_result: str = self._('Точность по отдельным персональным качествам личности '
                                                         'человека ...')
        self._get_union_predictions_results_mean: str = self._('Средняя средних абсолютных ошибок: {}, '
                                                               'средняя точность: {} ...')

    # ------------------------------------------------------------------------------------------------------------------
    # Документация
    # ------------------------------------------------------------------------------------------------------------------

    # __doc__ = Language.__doc__