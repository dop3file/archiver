import os

from encoder import HuffmanEncoder
from decoder import HuffmanDecoder
from utils import DataSource, MEGABYTE


def encode(filepath):
    output_filepath = input("Введите путь к файлу для кодирования: ")
    encoder = HuffmanEncoder()
    data_source = DataSource()
    data = data_source.read_file(filepath)
    result = encoder.encode(data)
    data_source.write_result(result, output_filepath)
    print("Файл упешно закодирован!")
    print(f"Вес исходного файла - {os.path.getsize(filepath) / MEGABYTE} Mb")
    print(f"Вес выходного файла - {os.path.getsize(output_filepath) / MEGABYTE} Mb")


def decode(filepath):
    output_filepath = input("Введите путь к файлу для раскодирования: ")
    decoder = HuffmanDecoder()
    data_source = DataSource()
    result = decoder.decode(decoder.read(filepath))
    data_source.write_file(result, output_filepath)
    print("Файл успешно разкодирован!")


operation_type = input("Введите тип операции[encode/decode]: ")
filepath = input("Введите путь к файлу: ")
operations = {
    "encode": encode,
    "decode": decode
}
operations[operation_type](filepath)


