from exceptions.strategy_not_found_error import StrategyNotFoundError
from file_reader.strategies.enums.file_structure_type import FileStructureType
from pathlib import Path
from file_reader.strategies.line_by_line_strategy import read as line_by_line_strategy
from file_reader.strategies.sections_strategy import read as sections_strategy

strategies = {
    FileStructureType.LINE_BY_LINE: line_by_line_strategy,
    FileStructureType.SECTIONS: sections_strategy
}


def read(file: Path, strategy: FileStructureType):
    if not strategy in strategies:
        raise StrategyNotFoundError(strategy)
    return strategies[strategy](file)
