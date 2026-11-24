# 内容体系

个人主页回答「我是谁、最近在做什么」，博客写一件事的来龙去脉，Aum Notes 留下以后还会查的解释和实验。数据库、Rust 和系统软件是长期学习方向，AI 工具、个人基础设施和生活思考也有各自的写作空间。

| 内容 | 放在哪里 | 读者怎么找 |
| --- | --- | --- |
| 自我介绍、当前方向、精选项目和文章 | 个人主页 | 文章、项目、近况三块卡片 |
| 项目复盘、方法探究、个人随笔 | 博客 | 按发布时间读，按标签或关键词找 |
| 单个概念、源码细节、可复跑的实验 | Aum Notes | 从专题目录进入，或直接搜正文 |

## 个人主页

- 自我介绍用 Aum，学习方向写具体技术名。当前简介是「数据库基础设施、Rust、开源项目与个人写作」。近况卡把「查询优化、存储引擎和 SQL」放进一句短话。[首页内容][home-html]
- 文章卡选了两篇博客随笔，链接直达原文。项目卡展示 GreptimeDB 查询优化与开源贡献、Zenfeed-Py 的 RSS 聚合，每项带一句工作说明。卡片内容在 `index.html` 手动维护。[文章与项目][home-html]
- 导航和界面文案提供中英切换。问候按访问时间变化，首页与博客使用的中文文章标题保留原文。[首页文案][home-html] · [语言与问候][home-js]

## 博客

刊头用「记录生活、思考与探索。」概括写作范围。列表由 Markdown 生成，按发布时间倒序分页，每页八篇。标签跨文章使用，搜索索引收录标题、标签、摘要和正文。文章页显示发布时间、阅读统计和摘要，并提供大纲、相邻文章和评论区。[博客列表][blog-index] · [搜索索引][blog-search] · [文章页][blog-post]

| 已有题材 | 写法 | 样本 |
| --- | --- | --- |
| 项目与基础设施 | 从一个实际约束起笔，写数据模型、架构取舍和踩过的坑。 | [Zenfeed-Py][zenfeed] · [个人基础设施整理][infra] · [todo-hub 任务队列][todo] |
| 学习方法与 AI | 从亲身使用的问题提出假设，再用示例或推导分析机制，交代结论的适用范围。 | [AI 辅助期末复习][exam] · [上下文工程入门][context] |
| 生活与成长 | 用第一人称写一段具体经历，跟着时间和当时的感受展开，再写自己的判断怎样变化。 | [Hello World][hello] · [没有 Claude 的那些日子][claude] · [从焦虑自责到长期主义][long-term] |

文章放在 `src/content/posts/<slug>.md`，页面路径为 `/posts/<slug>/`。标题写读者会看到的问题或经历。项目文可在正文链接前文、代码与实际结果。中文界面和英文界面共享同一篇正文。

```yaml
---
title: 注意力不够用，所以我给自己和 Agent 搭了一个任务队列
date: 2026-11-01
tags: [AI Agent, Cloudflare, Workers, MCP, 效率]
summary: 记录用 Cloudflare Workers 和 D1 搭建共享任务队列的过程。
lang: zh
---
```

`title`、`date` 必填，`tags` 默认空数组，`lang` 默认 `zh`。列表优先读 `summary`，兼容 `description`。详情页可以用 `abstract` 覆盖显示的摘要。文章支持代码、公式、Mermaid、表格、提示块和脚注。[字段定义][blog-schema] · [Markdown 配置][blog-config] · [文章页][blog-post]

## Aum Notes

首页写「学习、探索、记录与沉淀」。目录和侧栏按专题组织，专题内按 `updated` 倒序。单篇聚焦一个可查的问题，常用最小示例说明行为，再列约束、边界情况或验证方法。下面是仓库的六篇起始示例。[笔记站首页][notes-home] · [目录][notes-topics] · [排序逻辑][notes-order] · [项目说明][notes-readme]

| 专题 | 分类 ID | 笔记示例 |
| --- | --- | --- |
| 计算机基础 | `cs` | [虚拟内存中的页表与缺页][note-vm] |
| 数据库与 SQL | `databases` | [SQL COUNT 到底在数什么][note-count] |
| Rust 与系统编程 | `rust` | [Rust Arc 与跨线程共享所有权][note-arc] |
| AI / LLM | `ai` | [LLM 推理时的 KV Cache][note-kv] |
| 面试 | `interviews` | [面试里怎么讲清一个技术项目][note-interview] |
| 学习与实验 | `lab` | [写一份可以重跑的实验记录][note-lab] |

笔记放在 `src/content/notes/<category>/<slug>.md`，页面路径为 `/notes/<category>/<slug>/`。四个字段都必填。页面从 frontmatter 读取一级标题，正文从二级标题开始，二级和三级标题进入本页大纲。正文和更新日期一起维护，站内可按标题、描述、专题和正文检索。Ideas 目前显示「暂无条目。」[分类定义][notes-categories] · [字段定义][notes-schema] · [笔记页][notes-page] · [搜索索引][notes-search] · [Ideas][notes-ideas]

```yaml
---
title: SQL COUNT 到底在数什么
description: 用三行数据区分 COUNT(*)、COUNT(expr) 和 COUNT(DISTINCT expr)。
category: databases
updated: '2026-11-23'
---
```

## 同一主题的写法

以数据库查询为例，首页近况用一句话说明正在学什么，项目卡指向实际开源贡献。笔记可单独说明 COUNT 的语义，用几行数据和执行计划验证。博客适合写一次查询优化工作的动机、约束、实验和取舍，正文可链接已有的概念笔记，首页再精选文章入口。[首页内容][home-html] · [COUNT 笔记][note-count]

[home-html]: https://github.com/Aumnertic/homepage/blob/9fc0ed2c47fc3f0df83d2cfdc3a703c77f4134a3/index.html
[home-js]: https://github.com/Aumnertic/homepage/blob/9fc0ed2c47fc3f0df83d2cfdc3a703c77f4134a3/home.js
[blog-index]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/pages/%5B...page%5D.astro
[blog-post]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/pages/posts/%5Bslug%5D.astro
[blog-search]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/pages/search-index.json.ts
[blog-schema]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/config.ts
[blog-config]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/astro.config.mjs
[zenfeed]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/posts/zenfeed-py.md
[infra]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/posts/personal-infra.md
[todo]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/posts/todo-hub.md
[exam]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/posts/ai-exam-review.md
[context]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/posts/context-engineering-intro.md
[hello]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/posts/hello-world.md
[claude]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/posts/the-days-without-claude.md
[long-term]: https://github.com/Aumnertic/blog-minimal/blob/d593eccd5e5d7b8740fee98e1b5267bf02cd9bdf/src/content/posts/from-anxiety-to-long-termism.md
[notes-home]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/pages/index.astro
[notes-topics]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/pages/topics/index.astro
[notes-order]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/lib/notes.ts
[notes-readme]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/README.md
[notes-categories]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/lib/categories.ts
[notes-schema]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/content.config.ts
[notes-page]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/pages/notes/%5B...id%5D.astro
[notes-search]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/pages/search-index.json.ts
[notes-ideas]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/pages/ideas.astro
[note-vm]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/content/notes/cs/virtual-memory.md
[note-count]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/content/notes/databases/sql-count.md
[note-arc]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/content/notes/rust/arc-shared-ownership.md
[note-kv]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/content/notes/ai/llm-kv-cache.md
[note-interview]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/content/notes/interviews/project-walkthrough.md
[note-lab]: https://github.com/Aumnertic/notes-repo/blob/b4b71455e0107f0d836dc49ca2d4ce42033b4a28/src/content/notes/lab/reproducible-experiment-log.md
