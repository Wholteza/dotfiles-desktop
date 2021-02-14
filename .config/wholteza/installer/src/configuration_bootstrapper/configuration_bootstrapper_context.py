from pathlib import Path
from configuration_bootstrapper.enums.configuration_bootstrap_type import ConfigurationBootstrapType
from exceptions.strategy_not_found_error import StrategyNotFoundError
from src.configuration_bootstrapper.strategies.ensure_file_contains_section_strategy import bootstrap as file_contains_sections_strategy


strategies = {
    ConfigurationBootstrapType.ENSURE_FILE_CONTAINS_SECTION: None
}


def bootstrap(file_to_bootstrap_into: Path, file_with_bootstrap_code: Path, strategy: ConfigurationBootstrapType):
    if strategy not in strategies:
        raise StrategyNotFoundError(strategy)
    strategies[strategy](file_with_bootstrap_code, file_to_bootstrap_into)
