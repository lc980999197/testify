import logging
import os
import shutil
import threading
from datetime import datetime, timedelta


class TestLogger:
    def __init__(self):
        self.log_dir = ""
        self.archive_months = None
        self.log_level = ""
        self.logger = None

    def init(self, log_dir="", log_level="", archive_months=3):
        self.log_dir = log_dir
        self.archive_months = archive_months
        self.log_level = log_level
        now = datetime.now()
        log_subdir = os.path.join(self.log_dir, now.strftime("%Y%m"))
        os.makedirs(log_subdir, exist_ok=True)
        log_file = os.path.join(log_subdir, f"test_run_{now.strftime('%Y%m%d_%H%M%S')}.log")
        threading.Thread(target=self._clean_old_logs).start()
        self.logger = logging.getLogger("TestFramework")
        self.logger.setLevel(self.log_level)
        self.logger.handlers.clear()

        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")

        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def _clean_old_logs(self):
        cutoff_date = datetime.now() - timedelta(days=self.archive_months * 30)  # 近似每月30天
        cutoff_year_month = cutoff_date.strftime("%Y%m")

        for folder in os.listdir(self.log_dir):
            folder_path = os.path.join(self.log_dir, folder)
            if os.path.isdir(folder_path) and folder <= cutoff_year_month:
                shutil.rmtree(folder_path)  # 删除过期的年月文件夹

    def info(self, message): self.logger.info(message)

    def warning(self, message): self.logger.warning(message)

    def error(self, message): self.logger.error(message)

    def debug(self, message): self.logger.debug(message)


logger = TestLogger()


