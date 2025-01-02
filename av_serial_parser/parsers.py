import re
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SerialInfo:
    maker: str
    serial: str
    cd: str = ""
    ch: str = ""

    @property
    def number(self) -> str:
        return f"{self.maker.upper()}-{self.serial}"

    @property
    def filename(self) -> str:
        return f"{self.maker.upper()}-{self.serial}{'-' + self.cd.upper() if self.cd else ''}{'-C' if self.ch else ''}"

    def __str__(self):
        return f"{self.maker.upper()}-{self.serial}"


class SerialParser(ABC):
    @abstractmethod
    def parse(self, input_text: str) -> SerialInfo:
        pass

    def _preprocess(self, input_text: str) -> str:
        input_text = input_text.replace("/", "").lower()

        patterns = [
            (r"(h265|h264)", ""),
            (r"(fhd|fhdc|fhdcj|hd)", ""),
            (
                r"^\w+\.(cc|com|net|me|club|jp|tv|xyz|biz|wiki|info|tw|us|de)@|^22-sht\.me|",
                "",
            ),
            (r"(1080p|720p|4k|x264|x265|uncensored|leak)", ""),
            (r"(\[|\]|\】\【)", ""),
            (r"\[\d{4}-\d{1,2}-\d{1,2}\] - ", ""),
            (r"_", "-"),
        ]

        for pattern, replacement in patterns:
            input_text = re.sub(pattern, replacement, input_text, flags=re.IGNORECASE)

        return input_text


class FC2Parser(SerialParser):
    def parse(self, input_text: str) -> SerialInfo:
        input_text = self._preprocess(input_text)

        if "cd" in input_text:
            cd_pattern = r"\d{3,}-(cd\d+)?"
            cd_match = re.search(cd_pattern, input_text)
            cd = cd_match.group(1).upper() if cd_match else ""
        else:
            cd_pattern = r"\d{3,}-(\d+)+"
            cd_match = re.search(cd_pattern, input_text)
            cd = f"CD{cd_match.group(1)}" if cd_match else ""

        number_pattern = r"(\d{3,})"
        match = re.search(number_pattern, input_text)
        if match:
            serial = match.group(1)
            return SerialInfo(maker="FC2-PPV", serial=serial, cd=cd)
        return SerialInfo(maker="", serial="", cd="")


class OnePonDoParser(SerialParser):
    def parse(self, input_text: str) -> SerialInfo:
        input_text = self._preprocess(input_text)

        if "cd" in input_text:
            cd_pattern = r"1pon-(cd\d+)?"
            cd_match = re.search(cd_pattern, input_text)
            cd = cd_match.group(1).upper() if cd_match else ""
        else:
            cd_pattern = r"1pon-\d+-\d+-(\d{1,2})+"
            cd_match = re.search(cd_pattern, input_text)
            cd = f"CD{cd_match.group(1)}" if cd_match else ""

        number_pattern = r"(\d{3,}-\d{3,})"
        match = re.search(number_pattern, input_text)
        if match:
            serial = match.group(1)
            return SerialInfo(maker="1PON", serial=serial, cd=cd)
        return SerialInfo(maker="", serial="", cd="")


class CaribParser(SerialParser):
    def parse(self, input_text: str) -> SerialInfo:
        input_text = self._preprocess(input_text)

        if "cd" in input_text:
            cd_pattern = r"carib-(cd\d+)?"
            cd_match = re.search(cd_pattern, input_text)
            cd = cd_match.group(1).upper() if cd_match else ""
        else:
            cd_pattern = r"carib-\d+-\d+-(\d{1,2})+"
            cd_match = re.search(cd_pattern, input_text)
            cd = f"CD{cd_match.group(1)}" if cd_match else ""

        number_pattern = r"(\d{3,}-\d{3,})"
        match = re.search(number_pattern, input_text)
        if match:
            serial = match.group(1)
            return SerialInfo(maker="CARIB", serial=serial, cd=cd)
        return SerialInfo(maker="", serial="", cd="")


class MuParser(SerialParser):
    def parse(self, input_text: str) -> SerialInfo:
        input_text = self._preprocess(input_text)

        if "cd" in input_text:
            cd_pattern = r"10mu-(cd\d+)?"
            cd_match = re.search(cd_pattern, input_text)
            cd = cd_match.group(1).upper() if cd_match else ""
        else:
            cd_pattern = r"10mu-\d+-\d+-(\d{1,2})+"
            cd_match = re.search(cd_pattern, input_text)
            cd = f"CD{cd_match.group(1)}" if cd_match else ""

        number_pattern = r"(\d{3,}-\d{2,})"
        match = re.search(number_pattern, input_text)
        if match:
            serial = match.group(1)
            return SerialInfo(maker="10MU", serial=serial, cd=cd)
        return SerialInfo(maker="", serial="", cd="")


class PacoParser(SerialParser):
    def parse(self, input_text: str) -> SerialInfo:
        input_text = self._preprocess(input_text)

        if "cd" in input_text:
            cd_pattern = r"paco-(cd\d+)?"
            cd_match = re.search(cd_pattern, input_text)
            cd = cd_match.group(1).upper() if cd_match else ""
        else:
            cd_pattern = r"paco-\d+-\d+-(\d{1,2})+"
            cd_match = re.search(cd_pattern, input_text)
            cd = f"CD{cd_match.group(1)}" if cd_match else ""

        number_pattern = r"(\d{3,}-\d{3,})"
        match = re.search(number_pattern, input_text)
        if match:
            serial = match.group(1)
            return SerialInfo(maker="PACO", serial=serial, cd=cd)
        return SerialInfo(maker="", serial="", cd="")


class Kin8Parser(SerialParser):
    def parse(self, input_text: str) -> SerialInfo:
        input_text = self._preprocess(input_text)

        number_pattern = r"kin8-(\d{3,})"
        number_match = re.search(number_pattern, input_text)
        serial = number_match.group(1)

        if "cd" in input_text:
            cd_pattern = r"(cd\d+)$"
            cd_match = re.search(cd_pattern, input_text)
            cd = cd_match.group(1) if cd_match else ""
        else:
            cd_pattern = r"\d{3,}-(\d{1,2})+"
            cd_match = re.search(cd_pattern, input_text)
            cd = f"CD{cd_match.group(1)}" if cd_match else ""

        return SerialInfo(maker="KIN8", serial=serial.upper(), cd=cd.upper())


class StandardParser(SerialParser):
    def parse(self, input_text: str) -> SerialInfo:
        input_text = self._preprocess(input_text)

        match = re.search(r"([a-zA-Z]+)[-_]?(\w+)", input_text, re.A)
        if not match:
            return SerialInfo(maker="", serial="", cd="")

        maker, serial = match.groups()

        if "cd" in input_text:
            cd_pattern = r"(cd\d+)$"
            cd_match = re.search(cd_pattern, input_text)
            cd = cd_match.group(1) if cd_match else ""
        else:
            cd_pattern = r"\d{3,}-(\d+)+"
            cd_match = re.search(cd_pattern, input_text)
            cd = f"CD{cd_match.group(1)}" if cd_match else ""

        serial = re.sub(r"c$", "", serial, flags=re.IGNORECASE)
        serial = re.sub(r"(\d+)(c)", r"\1", serial)

        if re.search(r"\d+ch$", serial, flags=re.I):
            serial = serial[:-2]

        return SerialInfo(maker=maker.upper(), serial=serial.upper(), cd=cd.upper())


class SerialParserFactory:
    @staticmethod
    def get_parser(input_text: str) -> SerialParser:
        if "fc2" in input_text.lower():
            return FC2Parser()
        elif "1pon" in input_text.lower():
            return OnePonDoParser()
        elif "carib" in input_text.lower():
            return CaribParser()
        elif "10mu" in input_text.lower():
            return MuParser()
        elif "paco" in input_text.lower():
            return PacoParser()
        elif "kin8" in input_text.lower():
            return Kin8Parser()
        else:
            return StandardParser()

