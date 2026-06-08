---
name: arxiv-ranking-tracker
version: 0.1
description: 搜推广领域arXiv论文追踪，聚焦排序模型方向
---

# 搜推广领域 ArXiv 论文数据 API

## 触发条件
用户想要获取搜推广领域（搜索/推荐/广告）的arXiv论文数据，尤其是排序模型方向

## 功能说明
通过URL参数获取JSON格式的arXiv论文数据，聚焦搜推广领域

## 基础仓库 URL
由 GitHub Actions 自动注入

## URL参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `category` | arXiv类别 | `cs.IR`, `cs.AI`, etc. |
| `author` | 作者姓名 | `Smith` |
| `keywords` | 关键词，逗号分隔 | `ranking,recommendation` |

## 搜推广领域筛选关键词

### 排序模型核心
- ranking, reranking, learning to rank, ltr
- ctr, cvr, cps, click-through
- pre-ranking, preranking, rough sort
- multi-task ranking

### 召回与检索
- retrieval, recall, matching, embedding
- vector search, approximate nearest neighbor

### 推荐系统
- recommendation, recommender, collaborative filtering

### 广告系统
- ad ranking, ad recommendation, bid optimization

## 样例
```
bash scripts/fetch.sh "https://<username>.github.io/arxiv-ranking-tracker/?category=cs.IR&keywords=ranking,recommendation"
```

## 筛选逻辑

```
category AND (keywords OR author)
```

- category: 硬筛选，只返回指定类别
- keywords: 在标题和摘要中搜索
- author: 在作者字段中搜索
- keywords与author是"或"关系

## JSON响应结构

```json
{
  "category": "cs.IR",
  "author": "Smith",
  "keywords": ["ranking"],
  "count": 10,
  "papers": [
    {
      "id": "2401.00001",
      "title": "标题",
      "authors": "作者1, 作者2",
      "categories": ["cs.IR"],
      "summary": "tldr",
      "date": "2024-01-01",
      "url": "https://arxiv.org/abs/2401.00001",
      "domain": "排序模型/Ranking",
      "importance": "高/High",
      "ranking_relevance": "与排序模型的关系说明"
    }
  ]
}
```