def test_run_yaml(http_runner, yaml_file, base_url):
    """通用函数：运行单个 YAML 文件并验证结果"""
    http_runner.with_config({"base_url": base_url}).run(yaml_file)
    summary = http_runner.summary
    assert summary["success"], f"YAML 测试失败: {yaml_file}"

def test_dummy(http_runner):
    print("Dummy test running")
    assert True