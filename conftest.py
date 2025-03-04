import pytest
import os
import datetime
from pathlib import Path
from httprunner import HttpRunner
from utils.logger import logger
from config.config import conf


def pytest_configure(config):  # 配置 pytest
    rootdir = config.rootdir
    if Path(conf.report.path).is_absolute():
        config.report_path = conf.report.path
    else:
        config.report_path = os.path.join(rootdir, conf.report.path)
    # 创建当月目录（如：reports/2025-03）
    current_month = datetime.datetime.now().strftime("%Y-%m")
    setattr(config, "conf", conf)  # 添加 conf 属性到 config
    current_path = f"{config.report_path}/detail/{current_month}"
    os.makedirs(current_path, exist_ok=True)
    os.makedirs(f"{config.report_path}/archive", exist_ok=True)
    report_file = os.path.join(current_path,  f"test_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
    config.option.htmlpath = report_file  # 设置 HTML 报告路径


def pytest_sessionstart(session):  # pytest session start hook
    logger.init(session.config.conf.log.path, session.config.conf.log.get_level(), session.config.conf.log.archive)


def pytest_sessionfinish(session, exitstatus):  # pytest session finish hook
    """在测试会话结束钩子"""
    pass


@pytest.fixture  # fixture
def setup():
    print("初始化测试环境")
    yield  # 测试执行阶段
    print("清理测试环境")


def get_yaml_files():  # 收集所有 YAML 文件
    yaml_files = []
    yaml_dir = os.path.join(os.path.dirname(__file__), "tests/yaml_cases")
    for root, _, files in os.walk(yaml_dir):
        for file in files:
            if file.endswith(".yml") or file.endswith(".yaml"):
                yaml_files.append(os.path.join(root, file))
    return yaml_files


@pytest.fixture(scope="session")
def http_runner():
    """返回 HttpRunner 实例，failfast=False 确保运行所有用例"""
    return HttpRunner()


# base_url fixture
@pytest.fixture(scope="session")
def base_url():
    """示例：可从配置文件读取"""
    return conf.base_url


# 自动参数化所有 YAML 文件
def pytest_generate_tests(metafunc):
    if "yaml_file" in metafunc.fixturenames:
        yaml_files = get_yaml_files()
        if not yaml_files:
            pytest.skip("No YAML files found in tests/yaml_cases/")
        metafunc.parametrize("yaml_file", yaml_files, ids=[os.path.basename(f) for f in yaml_files])