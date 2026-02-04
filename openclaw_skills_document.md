# OpenClaw Skills 仓库介绍及热门技能清单

## 仓库概述

OpenClaw（前身为 Moltbot，最初为 Clawdbot）是一个在本地运行的AI助手，可以直接在您的机器上操作。Skills（技能）扩展了它的功能，使其能够与外部服务交互、自动化工作流程并执行专门任务。

这个awesome-openclaw-skills仓库收集了社区构建的各种实用技能，帮助用户发现和安装适合自己需求的技能。

## 安装方法

### ClawHub CLI
```bash
npx clawhub@latest install <skill-slug>
```

### 手动安装
将技能文件夹复制到以下位置之一：

- 全局: ~/.openclaw/skills/
- 工作区: <project>/skills/

优先级: 工作区 > 本地 > 捆绑

## 热门技能清单

根据GitHub上的星标数和实用性，以下是几个值得推荐的技能：

### 1. Coding Agents & IDEs 类别
- **coding-agent**: 运行Codex CLI、Claude Code、OpenCode或Pi Coding Agent
- **skill-creator**: 创建有效技能的指南
- **cursor-agent**: 用于使用Cursor CLI代理的综合技能
- **debug-pro**: 系统化调试方法论和语言特定调试命令

### 2. DevOps & Cloud 类别
- **github**: 使用gh命令与GitHub交互
- **docker-essentials**: 容器管理、镜像操作的基本Docker命令和工作流程
- **aws-infra**: 基于聊天的AWS基础设施助手
- **kubernetes**: 全面的Kubernetes和OpenShift集群管理

### 3. Web & Frontend Development 类别
- **frontend-design**: 创建具有高质量设计的独特、生产级前端界面
- **react-email-skills**: 使用React组件创建美观、响应式的HTML电子邮件
- **ui-ux-master**: 结合Apple HIG、现代Web设计和SuperDesign模式的UI/UX设计技能

### 4. AI & LLMs 类别
- **ai-image-gen**: OpenAI图像生成功能
- **openai-whisper**: OpenAI语音转文字功能
- **search-research**: 搜索和研究工具集

### 5. Productivity & Tasks 类别
- **apple-notes**: Apple笔记应用集成
- **apple-reminders**: Apple提醒事项集成
- **notion**: Notion集成
- **obsidian**: Obsidian笔记集成

## 总结

OpenClaw Skills生态系统非常丰富，涵盖了从编程助手到日常生产力工具的各个方面。通过这些技能，您可以大幅扩展OpenClaw的功能，使其适应您的具体需求。建议根据您的使用场景选择相应的技能进行安装和使用。