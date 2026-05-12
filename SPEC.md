# EPE (Executable Prompt Engineering) 规范

**版本：1.0.0 | 状态：草案**

---

## 1. 概述

EPE（Executable Prompt Engineering，可执行提示词工程）是一种将自然语言提示词视为「源码」、将 AI 视为「编译器」的新范式。本文件定义了 EPE 格式的完整规范。

---

## 2. PROGRAM 块规范

### 2.1 语法

PROGRAM 块使用方括号标记开始和结束，采用 Key: Value 格式：

```
[PROGRAM]
NAME: <项目名>
VERSION: <版本号>
PURPOSE: <执行目标>
INPUT: <输入条件>
LOGIC: <核心逻辑>
CONSTRAINT: <约束条件>
OUTPUT: <可执行物>
[END]
```

### 2.2 字段定义

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| `NAME` | ✅ | String | 项目名。简短有描述性，建议 2-10 字。用于版本管理和文档索引。 |
| `VERSION` | ✅ | String | 语义化版本号。遵循 semver 规范（如 `1.0.0`）。 |
| `PURPOSE` | ✅ | String | 一句话阐明要达成的**结果**，而非「要做什么」。这是对产物的顶层验证标准。 |
| `INPUT` | ✅ | String | 输入条件和参数。包括：数据源、运行时依赖、API 密钥位置、环境假设。多项用顿号或逗号分隔。 |
| `LOGIC` | ✅ | String | 核心处理逻辑。应分解为 3-7 个步骤，使用 → 连接（`A → B → C`）。每个步骤应对应一个可执行动作。 |
| `CONSTRAINT` | ✅ | String | 至少 2 条边界规则。用顿号或逗号分隔。包括：技术上不许做的事、必须遵守的约定、输出质量标准。 |
| `OUTPUT` | ✅ | String | 最终产物的精确描述。必须指明：输出形式（文件/代码/配置）、存放位置（如适用）、格式要求。 |

### 2.3 扩展字段（可选）

以下字段可以在标准 7 字段之外附加：

| 字段 | 说明 |
|------|------|
| `DEPENDS` | 依赖列表（需要预装的基础设施） |
| `METRICS` | 执行成功的量化验收标准 |
| `TIMEOUT` | 预期执行时间上限 |
| `TAGS` | 分类标签，方便检索 |
| `AUTHOR` | 作者署名 |

### 2.4 文件扩展名

EPE 文件推荐使用 `.epe` 扩展名，以与普通 Markdown 文件区分。

```yaml
my-task.epe     # ✅ EPE 格式
my-prompt.md    # ❌ 可能被误认为是普通文档
```

### 2.5 MIME 类型

建议媒体类型：`text/vnd.epe`

---

## 3. 编译模型

### 3.1 P→C→E→A 管线

```
[PROGRAM] 块
    │
    ▼
┌─────────────────────────────┐
│  Compile 阶段（AI 编译器）    │
│  ├─ 解析 PROGRAM 7 字段       │
│  ├─ 加载上下文信息            │
│  ├─ 逐步骤生成对应代码        │
│  └─ 校验约束是否全部满足      │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  Executable 阶段（产物）      │
│  ├─ 代码脚本（.py .sh .js）   │
│  ├─ 文档配置（.html .yaml）   │
│  ├─ 可运行文件               │
│  └─ 命令行指令序列            │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  Action 阶段（执行）          │
│  ├─ 文件写入磁盘              │
│  ├─ 脚本解释执行              │
│  ├─ 服务部署启动              │
│  └─ 消息通知推送              │
└─────────────────────────────┘
```

### 3.2 编译错误处理

AI 编译器应遵循以下错误处理规则：

1. **缺少必填字段** → 报错并指出缺失字段名
2. **约束冲突** → 报错并说明违反了哪条约束
3. **INPUT 不满足** → 报错并指出缺失的输入条件
4. **OUTPUT 无法生成** → 报错并说明技术原因
5. **不报模糊答案** → 不能以「也许你可以试试……」替代编译失败

---

## 4. 文件格式要求

### 4.1 PROGRAM 头

- 必须以 `[PROGRAM]` 作为第一个非空行
- 必须以 `[END]` 作为结束行
- 7 个标准字段的书写顺序：NAME → VERSION → PURPOSE → INPUT → LOGIC → CONSTRAINT → OUTPUT
- 字段名统一大写英文
- 冒号为英文冒号 `:` 后接一个空格

### 4.2 注释

支持两种注释方式：

```
# 行内注释：以 # 开头的整行为注释
[PROGRAM]
NAME: my-task
# VERSION: 0.5  ← 被注释掉，不生效
VERSION: 1.0
PURPOSE: ...
```

```
// 行末注释
PURPOSE: 生成报告 // 这是对目的的解释
```

### 4.3 多行值

当某字段值需要多行时，使用 `|` 延续标记：

```
LOGIC: |
  第一步：扫描目录
  第二步：过滤目标文件
  第三步：提取元数据
  第四步：格式化输出
```

---

## 5. 验证规则

### 5.1 编译前验证

| 检查项 | 规则 |
|--------|------|
| NAME 非空 | 项目名不能为空 |
| VERSION 格式 | 遵循 MAJOR.MINOR.PATCH（如 1.0.0） |
| PURPOSE 非空 | 必须有明确的执行目标 |
| LOGIC 步数 | 至少 3 步，至多 7 步 |
| CONSTRAINT 条数 | 至少 2 条 |
| OUTPUT 具体化 | 必须是可执行物描述，不能是「一段文字」 |
| 所有字段填写 | 7 个标准字段不能缺失 |

### 5.2 产物验收标准

- [ ] 产物文件存在并可读取
- [ ] 不需要额外人类编辑即可运行
- [ ] 产物行为与 PURPOSE 一致
- [ ] 所有 CONSTRAINT 中的规则都被遵守
- [ ] 产物使用 INPUT 中声明的数据源

---

## 6. 版本管理

EPE 文件自身是源码，应纳入 Git 版本管理：

```bash
# 在 git 仓库中管理 .epe 文件
git add my-pipeline.epe
git commit -m "feat: add data processing pipeline v1"

# 版本迭代
# v1.0.0 → v1.1.0（添加功能）
# v1.0.0 → v2.0.0（不兼容的改动）
# v1.0.0 → v1.0.1（修复/优化）
```

---

## 7. 用例示例

### 7.1 PDF 报告生成

```
[PROGRAM]
NAME: 行业分析报告生成
VERSION: 1.0
PURPOSE: 根据主题生成专业 PDF 分析报告
INPUT: 报告主题、配色方案（默认#1B3A5C/#0077C8）
LOGIC: 网络调研收集资料 → 结构化分析 → 编写HTML+CSS → WeasyPrint渲染
CONSTRAINT: 旁门左道浅色风格、文件名格式{主题}_深瞳1号_{YYYYMMDD}、先检查 weasyprint 依赖
OUTPUT: PDF文件（存至 workspace/report/YYYYMMDD/）
[END]
```

### 7.2 网站变更监控

```
[PROGRAM]
NAME: 网站变更监控脚本
VERSION: 1.0
PURPOSE: 生成可直接运行的 Python 监控脚本
INPUT: 目标URL、检查间隔（秒）、接收邮箱
LOGIC: HTTP GET → 计算内容哈希 → 对比上次哈希 → 不一致则发邮件
CONSTRAINT: 只用 Python 标准库、敏感信息从 .env 读取
OUTPUT: monitor.py + .env.template（直接 python3 monitor.py 运行）
[END]
```

### 7.3 CRON 定时任务

```
[PROGRAM]
NAME: 每日市场摘要
VERSION: 1.1
PURPOSE: 每天早上 8 点生成市场摘要并推送到微信
INPUT: 数据源URL列表、微信接收人ID
LOGIC: 访问数据源 → 结构化摘要 → 格式化消息 → 微信推送
CONSTRAINT: 结果不超过 2000 字、失败后重试 3 次
OUTPUT: 微信消息（通过 Hermes Agent cronjob 自动执行）
[END]
```
