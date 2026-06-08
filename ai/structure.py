from pydantic import BaseModel, Field, field_validator
import re

class Structure(BaseModel):
    tldr: str = Field(description="generate a too long; didn't read summary")
    motivation: str = Field(description="describe the motivation in this paper")
    method: str = Field(description="method of this paper")
    result: str = Field(description="result of this paper")
    conclusion: str = Field(description="conclusion of this paper")
    # 搜推广领域定制字段
    domain: str = Field(description="categorize this paper into one of: [排序模型/Ranking, 召回模型/Recall, 重排模型/Reranking, 预估模型/CTR-CVR Estimation, 向量检索/Vector Retrieval, 搜索引擎/Search Engine, 推荐系统/Recommender System, 广告系统/Ad System, 其他/Other]. Reply in Chinese.")
    importance: str = Field(description="rate the importance of this paper for ranking model research: [高/High, 中/Medium, 低/Low]. Consider innovation, practical value, and relevance to ranking models. Reply in Chinese.")
    ranking_relevance: str = Field(description="explain how this paper relates to ranking models in search/recommendation/advertising systems. If not directly related, explain the potential connection. Reply in Chinese.")