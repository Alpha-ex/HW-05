# Перевірити шлях до файлу, Синтаксис написання запиту, створення ЛОГ-файлу,
# таблиця параметрів регулярних виразів!
# Ця творчисть не зовсім моя, більше для ознайомлення та вивчення

import sys
import re

def parse_log_line(line: str) -> dict:
    # Парсить рядок логу і повертає словник з рівнем логування та повідомленням.
    
    match = re.match(r"\[(\w+)\] (.+)", line)
    if match:
        return {"level": match.group(1), "message": match.group(2)}
    else:
        return {"level": None, "message": line}

def load_logs(file_path: str) -> list:
    # Завантажує логи з файлу.
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    # Фільтрує логи за рівнем.
    return [log for log in logs if parse_log_line(log)["level"] == level]

def count_logs_by_level(logs: list) -> dict:
    # Підраховує кількість записів за рівнем логування.
    log_counts = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARNING": 0}
    for log in logs:
        level = parse_log_line(log)["level"]
        if level in log_counts:
            log_counts[level] += 1
    return log_counts

def display_log_counts(counts: dict):
    # Виводить результати підрахунку записів за рівнем логування у вигляді таблиці.
    print("Level\tCount")
    print("----------------")
    for level, count in counts.items():
        print(f"{level}\t{count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python script.py <шлях_до_лог_файлу> [рівень_логування]")
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    
    if len(sys.argv) == 3:
        level_filter = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level_filter)
        log_counts = count_logs_by_level(filtered_logs)
    else:
        log_counts = count_logs_by_level(logs)
    
    display_log_counts(log_counts)