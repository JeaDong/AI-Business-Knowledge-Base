# 知间 · 研发知识库

一个本机运行的研发知识工作台：**FastAPI + SQLite FTS5 + React/Vite + 本机 Codex CLI**。
目标仓库只读；不依赖原项目的 Flask、数据库、Redis 或业务服务。

## 启动

需要 Python 3.11+、Node.js 20.19+ 和已登录的 Codex CLI。

```sh
cd /Users/vino/rd-knowledge
codex login status
# 如未登录：codex login
./start.sh
```

打开 http://127.0.0.1:8765 。启动脚本安装缺失依赖、构建前端，并在首次启动时生成模块需求清单及索引。
已安装环境快速启动：`.venv/bin/python run.py`。
修改前端后执行 `cd frontend && npm run build`，然后重启后端。

## 第一版功能

- 对话分析：自由提问、需求分析、代码分析、测试设计；保留历史。
- 单任务串行调用 Codex，任务状态通过 SSE 展示，支持停止、超时和错误重试。
- 知识库：中英文关键词/业务别名检索、代码符号切分、原文阅读及行号定位。
- 现状需求：从代码反推的总览和 11 个模块清单，以及兑换、安全重置详细草稿。
- 回答引用绑定不可变来源快照，重新同步不会改变旧回答指向的内容。
- 可以将回答显式保存为知识草稿并同步入库，或导出 Markdown。
- 每次同步重新扫描允许的已跟踪文件，但仅对内容/提交版本变化的文件重建索引；删除的来源退出当前检索，保留历史引用。

## 模型与隐私边界

后端调用 `codex exec`，使用当前操作系统用户的 Codex 登录，无需在网页输入 Key。
每次分析会将问题、最近对话与检索到的片段交给 Codex，消耗该账号额度。
运行使用临时工作目录、只读沙箱、不加载用户配置，禁用 shell、浏览器、插件等工具。
首版只分析提供的检索证据，不让 Agent 自由执行仓库代码。

索引只读取指定仓库 Git 已跟踪的 `app/`、`tests/`、`migrations/versions/`、`docs/architecture/` 和 README 的允许文本类型。
排除配置目录、翻译文件、密钥命名文件、软链接与超大文件，并对常见密钥格式做基础脱敏。这不是完整 DLP，接入其他仓库前应检查其中敏感内容。
本地 SQLite 内含代码片段、对话和需求草稿，位于忽略的 `data/` 目录。

**仅监听 127.0.0.1。** 当前没有团队 SSO、用户隔离或生产级权限；不要直接改成公网监听。
当前服务是个人本地 MVP，多角色使用同一知识结构，不代表已具备多用户部署能力。
请求来源检查保护本地写接口；不暴露任意文件读取、shell 执行或仓库路径修改接口。

## 需求文档的含义

`docs/requirements/00-overview.md`：范围总览；`inventory-*.md`：根据 AST 提取的路由、方法说明、字段与显式控制装饰器。
接口清单使用局部路由，完整 URL 需要核查命名空间及网关。模块分组按路径关键词推断。
`01-exchange.md` 和 `02-security.md`：人工结合代码整理的详细行为、测试建议与待确认项。
所有文档均为“现状需求草稿”，不能当作产品正式确认或已执行测试的证明。

刷新模块清单与索引：

```sh
.venv/bin/python -m backend.bootstrap
```

此命令更新总览及自动模块清单，不覆盖详细草稿和用户保存的分析。
页面“同步知识库”也会更新自动模块清单。详细草稿仍保留原有整理基线，代码变化后需要重新分析和评审。

## 配置

通过环境变量设置，示例见 `.env.example`（不会自动加载该文件）：

| 名称 | 默认值 | 说明 |
|---|---|---|
| KNOWLEDGE_REPO | 同级 coinex_backend | 只读来源仓库 |
| KNOWLEDGE_DATA | 项目 data | SQLite 所在目录 |
| CODEX_BIN | codex | Codex 程序位置 |
| CODEX_MODEL | 留空 | 使用 Codex 默认模型；可显式指定账号支持的模型 |
| CODEX_TIMEOUT | 240 | 单次分析超时秒数 |
| PORT | 8765 | 本地监听端口 |

## 验证

```sh
.venv/bin/python -m pytest -q
cd frontend && npm run build
```

测试使用临时仓库和假模型，不消耗额度。实际 Codex 连通性需要在工作台发送一个问题验证。
依赖锁：Python `requirements.lock.txt`，前端 `package-lock.json`。

## API

`GET /api/status`、`POST /api/sync`、`GET /api/sources`、`GET /api/search`、`GET /api/sources/{id}`。
`GET/POST /api/conversations`、`GET /api/conversations/{id}`、`POST /api/conversations/{id}/messages`。
`GET /api/jobs/{id}`、`GET /api/jobs/{id}/events`、`POST /api/jobs/{id}/cancel`、`POST /api/messages/{id}/save`。
开发接口文档：`/docs`（Swagger UI 资源从 CDN 加载），离线可直接查看 `/openapi.json`。

## 已知范围

没有向量模型、全量调用图、自动改代码或自动运行测试。检索为关键词、中文二元词与业务别名扩展，需要结合真实问题继续评估召回。
“检索依据”表示传给模型的证据；模型正文编号表示其引用，尚未对每条事实做独立模型校验。
保存的知识草稿也会参与检索，但始终带未审核标记。历史快照保留会逐步占用磁盘空间，未加入清理策略。
不支持任意文件上传；当前文档入口是本地 Markdown 及显式保存的分析结果。
