import abc


class BaseFormatter:
    @property
    @abc.abstractmethod
    def label(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def importable(self) -> bool:
        pass

    @abc.abstractmethod
    def format_code(self, code: str, **options) -> str:
        pass


class BlackFormatter(BaseFormatter):

    label = "Apply Black Formatter"

    @property
    def importable(self) -> bool:
        try:
            import black

            return True
        except ImportError:
            return False

    def format_code(self, code: str, **options) -> str:
        from black import format_str

        return format_str(code, **options)


class Autopep8Formatter(BaseFormatter):

    label = "Apply Autopep8 Formatter"

    @property
    def importable(self) -> bool:
        try:
            import autopep8

            return True
        except ImportError:
            return False

    def format_code(self, code: str, **options) -> str:
        from autopep8 import fix_code

        return fix_code(code, **options)


class YapfFormatter(BaseFormatter):

    label = "Apply YAPF Formatter"

    @property
    def importable(self) -> bool:
        try:
            import yapf

            return True
        except ImportError:
            return False

    def format_code(self, code: str, **options) -> str:
        from yapf.yapflib.yapf_api import FormatCode

        return FormatCode(code, **options)[0]


SERVER_FORMATTERS = {
    "black": BlackFormatter(),
    "autopep8": Autopep8Formatter(),
    "yapf": YapfFormatter(),
}
