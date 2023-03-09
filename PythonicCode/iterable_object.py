from datetime import timedelta, date


class DateRangeIterable:
    """An iterable that contains its own iterator object."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return DateRangeIterable(self.start_date, self.end_date)

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class DateRangeContainerIterable:
    """An iterable that contains its own iterator object."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


if __name__ == '__main__':
    start = date(2023, 1, 1)
    end = date(2023, 1, 10)
    iterable = DateRangeIterable(start, end)
    print("First loop")
    for day in iterable:
        print(day)
    print("Second loop")
    for day in iterable:
        print(day)
    print("-------------------")
    iterable_with_generators = DateRangeContainerIterable(start, end)
    print("First loop")
    for day in iterable_with_generators:
        print(day)
    print("Second loop")
    for day in iterable_with_generators:
        print(day)

