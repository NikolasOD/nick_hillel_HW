class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        if start < end:
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start

        if current is not None:
            if current < start:
                raise Exception('Current value must be greater than start value')
            elif self.current > self.end:
                raise Exception('Current value must be less than end value')

        if current is None:
            self.current = self.start
        else:
            self.current = current

    # Увеличение счётчика на 1
    def increase(self):
        if self.current < self.end:
            self.current += 1
        else:
            self.current = self.start

    # Вывод текущего значения счётчика в терминал
    def get_current_value(self):
        return self.current
