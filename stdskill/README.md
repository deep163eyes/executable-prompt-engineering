# EPE Standard Library

就像编程语言有标准库，EPE 提供一套开箱即用的典型模板。
每个模板是一个 `.epe` 文件，拷贝后填字段即可直接交给 AI 编译执行。

## 使用方式

```bash
cp stdlib/pdf-report.epe my-task.epe
# 编辑 SKILL、GOAL、STEPS、RULES、OUTPUT
# 发给 LLM，编译执行
```

## 模板索引

| 模板 | 场景 | 复杂度 |
|------|------|--------|
| `pdf-report.epe` | 生成专业 PDF 报告 | ⭐⭐ |
| `data-fetch.epe` | 从网页/API 获取数据 | ⭐ |
| `html-page.epe` | 生成美观 HTML 页面 | ⭐⭐ |
| `cron-task.epe` | 注册定时任务并交付 | ⭐⭐ |
| `data-pipeline.epe` | 数据 ETL 处理 | ⭐⭐⭐ |
| `shell-script.epe` | 生成自动化 Shell 脚本 | ⭐ |
| `parallel-research.epe` | 多主题并行调研汇总 | ⭐⭐⭐ |
| `format-convert.epe` | 格式转换（HTML→PDF/MD→HTML） | ⭐ |
| `code-review.epe` | 代码审查与质量报告 | ⭐⭐ |
| `git-workflow.epe` | Git 仓库操作与 CI | ⭐⭐ |
| `ai-chat.epe` | 带上下文的 AI 对话 | ⭐ |
| `monitor-alert.epe` | 网站/服务监控与告警 | ⭐⭐ |
