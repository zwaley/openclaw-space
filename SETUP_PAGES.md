# 启用 GitHub Pages 步骤

为了让您的贪吃蛇游戏可以在线访问，您需要在 GitHub 上启用 Pages 功能。

## 操作步骤

1. 访问您的仓库：https://github.com/zwaley/openclaw-space

2. 点击仓库页面上的 "Settings" 选项卡（设置）

3. 向下滚动到 "Pages" 部分（在 "Code and automation" 区域下）

4. 在 "Source" 下拉菜单中，选择：
   - Branch: `main`
   - Folder: `/docs` 

5. 点击 "Save" 按钮

6. 等待几分钟，GitHub 会自动构建您的网站

## 访问您的游戏

启用后，您的游戏将在以下网址可用：
- 主页：https://zwaley.github.io/openclaw-space/
- 游戏：https://zwaley.github.io/openclaw-space/games/snake.html

## 注意事项

- 首次启用可能需要 1-5 分钟才能生效
- 如果网站仍未出现，请刷新页面或稍后再试
- 我们已经设置了 GitHub Actions 自动部署，所以以后的更改会自动更新网站

## 已完成的配置

- 贪吃蛇游戏文件已放置在 `docs/games/snake.html`
- 主页已创建在 `docs/index.html`
- GitHub Actions 工作流已配置用于自动部署
- Jekyll 配置已完成