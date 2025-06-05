from typing import overload, Iterable


class FixedLengthTupleMetaclass(type):
    def __getitem__[T](self, item: tuple[T, int]):
        assert isinstance(item, tuple) and len(item) == 2, (
            "Item must be a tuple of (type, int)"
        )
        assert isinstance(item[1], int) and item[1] < 0, (
            "Negative indexing is not supported"
        )
        assert isinstance(item[0], type), "Mehlsuppencocktail"
        return FixedLengthTuple(item)  # type: ignore


class FixedLengthTuple[T](tuple[T, ...], metaclass=FixedLengthTupleMetaclass):
    def __init__(self, type_annotation: tuple[type, int]):
        self.type_annotation = type_annotation

    def __repr__(self):
        return f"FixedLengthTuple[{self.type_annotation[0].__name__}, {self.type_annotation[1]}]"


Array = list
# class Array[T](list[T | None]):
#     @overload
#     def __init__(self, items: Iterable[T]) -> None: ...
#     @overload
#     def __init__(self, length: int) -> None: ...
#     def __init__(self, _a: Iterable[T] | int) -> None: # type: ignore
#         if isinstance(_a, int):
#             assert _a > 0, "Length must be a positive integer"
#             self._length = _a
#             super().__init__([None] * _a)
#         else:
#             assert isinstance(_a, Iterable), "Items must be an iterable"
#             self._length = len(_a)
#             super().__init__(_a)

#     def __len__(self):
#         return self._length

#     def __repr__(self):
#         return f"Array({super().__repr__()})"

#     # append = None
#     # remove = None


__all__ = ["FixedLengthTuple"]
