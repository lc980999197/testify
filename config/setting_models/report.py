from pydantic import BaseModel


class ReportConfig(BaseModel):
    path: str  # 存储路径
    archive: int  # 归档存储的保留月份数

