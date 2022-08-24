class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.start = start
        self.end = end
        self.current = current
        # Проверка текущего значения,
        # должно быть в диапазоне между start и end
        if self.current is not None:
            if self.current < self.start:
                raise Exception('Current value must be greater than start value')
            elif self.current > self.end:
                raise Exception('Current value must be less than end value')

    # Увеличение счётчика на 1
    def increase(self):
        if self.current is None:
            self.current = self.start + 1
            return
        if self.current < self.end:
            self.current += 1
            return
        else:
            # На случай если необходимо обнулять счётчик,
            # когда он доходит до максимума
            # self.current = self.start
            return f'We get max count: {self.end}'

    # Вывод текущего значения счётчика в терминал
    def get_current_value(self):
        # Я предположил что если текущее значение не задано,
        # то следует выводить начальное
        if self.current is None:
            return self.start
        return self.current
