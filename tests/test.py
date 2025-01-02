import av_serial_parser


if __name__ == "__main__":
    test_inputs = [
        "1PON-061524-001",
        "103024_01-10MU",
        "103124_100-PACO",
        "KIN8-3911-cd1",
        "start-135V",
        "hhd800.com@053124-001-1pon",
        "hhd800.com@KIN8-3911-cd1",
    ]

    for input_text in test_inputs:
        result = av_serial_parser.serial_parser(input_text)
        print(f"Input: {input_text}")
        print(f"Parsed: {result}")
        print(f"Parsed: {result.maker}-{result.serial}")
        print(f"As string: {str(result)}")
