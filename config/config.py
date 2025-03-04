import os
from typing import Optional, Dict

import yaml
from pydantic import BaseModel, validator

from config.setting_models.environment import Environment
from config.setting_models.log import LogConfig
from config.setting_models.report import ReportConfig
from config.setting_models.template import Template


class Settings(BaseModel):
    environments: Dict[str, Environment]  # 环境列表
    env: str  # 环境选择
    report: ReportConfig  # 报告配置
    log: LogConfig  # 日志配置
    template: Optional[Template] = None  # 数据驱动模板

    @property
    def base_url(self):
        return self.get_env().base_url

    @classmethod
    @validator('env')
    def check_env(cls, selected_env: str, values):
        if 'environments' not in values:
            raise ValueError('environments 未定义')
        environments = values['environments']
        if selected_env not in environments.__dict__ or environments[selected_env] is None:
            raise ValueError(f'当前选择环境 {selected_env} 配置不存在')
        return selected_env

    def get_env(self) -> Environment:
        env = self.environments[self.env]
        if env is None:
            raise ValueError(f'环境 {self.env} 未配置')
        return env


def load_template() -> Template:
    template_path = os.path.join(os.path.dirname(__file__), '../template/template.yml')
    with open(template_path, 'r', encoding="utf-8") as f:
        return Template(**yaml.safe_load(f))


def load_config() -> Settings:
    config_path = os.path.join(os.path.dirname(__file__), './config.yml')
    with open(config_path, 'r', encoding="utf-8") as f:
        setting = Settings(**yaml.safe_load(f))
        setting.template = load_template()
    return setting


conf: Settings = load_config()
