# userepe — 用户自定义配方

把你的 `.epe` 文件放在这里。这些是你自己写的配方，不会被仓库更新覆盖。

## 使用建议

- 每个 `.epe` 文件是一个独立的 PROGRAM 配方
- 可以直接拷贝 `stdepe/` 里的模板过来改
- 建议按场景分类命名：`weekly-report.epe`、`deploy-check.epe`

```
cp EPE/stdepe/pdf-report.epe EPE/userepe/weekly-report.epe
# 编辑 weekly-report.epe
git add EPE/userepe/weekly-report.epe
git commit -m "userepe: add weekly report recipe"
```
