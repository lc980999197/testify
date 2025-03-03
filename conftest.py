import pytest
import os
from httprunner import HttpRunner


# 收集所有 YAML 文件
def get_yaml_files():
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
    print(666666666)
    return HttpRunner()


# base_url fixture
@pytest.fixture(scope="session")
def base_url():
    """示例：可从配置文件读取"""
    return "https://www.baidu.com"


# 自动参数化所有 YAML 文件
def pytest_generate_tests(metafunc):
    if "yaml_file" in metafunc.fixturenames:
        yaml_files = get_yaml_files()
        if not yaml_files:
            pytest.skip("No YAML files found in tests/yaml_cases/")
        metafunc.parametrize("yaml_file", yaml_files, ids=[os.path.basename(f) for f in yaml_files])