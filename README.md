# Executable Prompt Engineering (EPE)

**提示词不再是描述——而是可编译、可运行、可生成最终产物的完整执行程序。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📖 概述

EPE 是一种全新的提示词工程范式。它的核心理念是将自然语言提示词视为**源码**，将 AI 视为**编译器**，将最终输出定义为**可直接运行的可执行产物**。

### P→C→E→A 模型

```
Prompt（源码） → Compile（AI编译） → Executable（可执行物） → Action（现实动作）
```

| 环节 | 含义 | 验收标准 |
|------|------|---------|
| **P** | 以 PROGRAM 块结构化的自然语言意图 | 包含完整的 5 字段 |
| **C** | AI 将自然语言解析为执行计划 | 产物可直接应用 |
| **E** | 产出的代码、脚本、文件、配置 | 无需人工修改即可运行 |
| **A** | 真实世界的执行结果 | 可验证的现实产出 |

---

## 📦 PROGRAM 标准格式

所有 EPE 提示词以统一的 PROGRAM 块作为入口：

```
[PROGRAM]
NAME:   项目名
GOAL:   一句话执行目标（要达成的结果）
STEPS:  核心步骤（3-7步，→分隔）
RULES:  约束条件（至少2条边界规则）
OUTPUT: 最终可执行物描述
[END]
```

[查看完整规范 →](SPEC.md)

---

## 🎯 核心规则

### 规则1：提示词具备「源码属性」
可编译 · 可复现 · 可逆向 · 可扩展 · 可维护

### 规则2：AI = 编译器
输出不是「建议」而是「编译结果」，错误处理遵循编译器逻辑——报错而非模糊回答。

### 规则3：最终输出必须「可直接运行」
只输出代码、配置、脚本、文件、指令。验收标准：放在目标环境中就能跑。

---

## 🔬 EPE vs 传统提示词

| 维度 | 传统提示词 | EPE |
|------|-----------|-----|
| 形式 | 自然语言段落 | 结构化 PROGRAM 块 |
| 可复现性 | 低 | 高（CONSTRAINT 固定行为边界） |
| 可版本化 | ❌ | ✅ Git 管理版本 |
| 可逆向 | ❌ | ✅ 代码可反推意图 |
| 工程化 | ❌ 一次性 | ✅ 可作为标准流程复用 |
| 产物验收 | 主观判断 | 客观标准（能否运行） |

---

## 📁 仓库结构

```
executable-prompt-engineering/
├── README.md          ← 本文件
├── LICENSE            ← MIT
├── SPEC.md            ← EPE 完整规范
├── WHITEPAPER.md      ← 方法论白皮书
├── CONTRIBUTING.md    ← 贡献指南
├── examples/          ← PROGRAM 示例
│   ├── pdf-report.epe
│   ├── ai-debate.epe
│   ├── website-monitor.epe
│   └── md-tree.epe
└── cli/               ← EPE 编译器工具（WIP）
    └── epe.py
```

---

## 🚀 快速开始

```bash
# 1. 查看 EPE 规范
cat SPEC.md

# 2. 查看示例
cat examples/pdf-report.epe

# 3. 写你自己的 PROGRAM
cat > my-prompt.epe << 'EOF'
[PROGRAM]
NAME: my-task
VERSION: 1.0
PURPOSE: ...
INPUT: ...
LOGIC: ...
CONSTRAINT: ...
OUTPUT: ...
[END]
EOF

# 4. 发给任意 LLM，即可编译执行
```

---

## 🤝 参与贡献

EPE 是一个开放的方法论。欢迎通过以下方式参与：

- **提 Issue**：格式改进建议、新示例、使用反馈
- **提 PR**：完善规范、添加示例、开发 CLI 工具
- **讨论**：方法论拓展、跨语言实现、最佳实践

[贡献指南 →](CONTRIBUTING.md)

---

## 📜 声明

EPE (Executable Prompt Engineering) 是一个开放的方法论标准，采用 MIT 协议开源。

**核心观点：** 提示词即源码，自然语言即编程语言。AI 编译器范式将重新定义人机交互的基础模型。
