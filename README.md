# Executable Prompt Engineering (EPE)

**提示词不再是描述——而是可编译、可运行、可生成最终产物的完整执行程序。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📖 概述

EPE 是一种全新的提示词工程范式。核心理念：将自然语言提示词视为**源码**，将 AI 视为**编译器**，将最终输出定义为**可直接运行的可执行产物**。

### P→C→E→A 模型

```
Prompt（源码） → Compile（AI编译） → Executable（可执行物） → Action（现实动作）
```

---

## 📦 PROGRAM 标准格式

```
[PROGRAM]
NAME:   项目名
GOAL:   一句话执行目标
STEPS:  核心步骤（→连接）
RULES:  约束条件
OUTPUT: 最终可执行物
                      ← VERSION 缺省: 1.0.0
                      ← INPUT 缺省: 来自上下文
[END]
```

[查看完整规范 →](SPEC.md)

---

## 🎯 核心规则

1. **提示词具备源码属性** — 可编译 · 可复现 · 可逆向 · 可扩展 · 可维护
2. **AI = 编译器** — 输出不是「建议」而是「编译结果」
3. **输出可直接运行** — 验收标准：放在目标环境中就能跑

---

## 📁 仓库结构

```
├── README.md          ← 本文件
├── LICENSE            ← MIT
├── SPEC.md            ← EPE 完整规范
├── WHITEPAPER.md      ← 方法论白皮书
├── CONTRIBUTING.md    ← 贡献指南
├── examples/          ← PROGRAM 示例
└── cli/               ← EPE 编译器工具
    └── epe.py
```

---

## 🚀 快速开始

```bash
cat examples/pdf-report.epe      # 看一个示例
python3 cli/epe.py validate examples/pdf-report.epe  # 验证格式
```

写你自己的：

```bash
cat > my-task.epe << 'EOF'
[PROGRAM]
NAME: my-task
GOAL: ...
STEPS: A → B → C
RULES: ...
OUTPUT: ...
[END]
EOF
```

发给任意 LLM，编译执行。

---

## 📜 声明

EPE (Executable Prompt Engineering) 是一个开放的方法论标准，采用 MIT 协议开源。
**提示词即源码，自然语言即编程语言。**
