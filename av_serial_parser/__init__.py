from .parsers import SerialParserFactory, SerialInfo


def serial_parser(input_text: str) -> SerialInfo:
    parser = SerialParserFactory.get_parser(input_text)
    return parser.parse(input_text)