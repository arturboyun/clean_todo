from typing import Callable, TypeVar

InputDTO = TypeVar("InputDTO")
OutputDTO = TypeVar("OutputDTO")


class Interactor[InputDTO, OutputDTO]:
    def __call__(self, data: InputDTO) -> OutputDTO:
        raise NotImplementedError


InteractorT = TypeVar("InteractorT")
InteractorFactory = Callable[[], InteractorT]
