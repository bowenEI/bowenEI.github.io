---
title: "重装 Windows 系统和软件指南"
date: 2026-04-04T01:18:48+08:00
lastmod: 2026-06-12T15:43:21+08:00
draft: false
tags:
  - 技术分享
---

本文档旨在提供一个全面的指南，方便用户重装 Windows 系统并配置常用软件和开发环境。

<!--more-->

## 制作启动盘

推荐使用 [Rufus](https://rufus.ie/) 制作启动盘。Github [下载地址](https://github.com/pbatard/rufus/releases)。

Microsoft 官方 Windows 系统镜像[下载地址](https://www.microsoft.com/zh-cn/software-download/windows11)。当前最新的系统版本为 25H2。

{{< callout type="important" >}}

需要注意，在 Rufus 中选择绕过至少 4GB RAM、安全启动和 TPM 2.0 检测，以确保系统能够顺利安装。

{{< /callout >}}

## Windows 系统配置

### 激活

推荐使用[沧水的 KMS 服务](https://kms.cangshui.net/)激活 Windows 系统。激活脚本[下载地址](https://kms.cangshui.net/kms/KMS-Cangshui.net.bat)。

### 设置

- 启用开发者模式
- 用户账户控制等级设置为“从不通知”
- 关闭传递优化

### 永久禁用更新

注册表定位至

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings
```

新建 `DWORD` 值 `FlightSettingsMaxPauseDays` 为 65535（0xFFFF），即最多可暂停更新 65535 天。然后在设置中即可发现选择暂停更新的时间更长。

### 右键菜单

使用经典 Win10 右键菜单：

```powershell
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

使用 Win11 右键菜单：

```powershell
reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /va /f
```

均须重启文件资源管理器生效。

### 系统字体

微软雅黑字体是一个**功勋卓著但廉颇老矣**的设计。它在模糊的屏幕时代解决了“看清”的问题，却在高清时代输给了“好看”。

使用 [DesktopOK](https://www.softwareok.com/?seite=Microsoft/DesktopOK) 可以定制系统字体。字体推荐更纱黑体（Sarasa Gothic），可以通过[微软应用商店](https://apps.microsoft.com/detail/9mw0m424ncz7?gl=CN&hl=zh-cn)下载。

> [更纱黑体这么多版本，要怎么选？ - 知乎](https://zhuanlan.zhihu.com/p/627059922)

系统字体可以使用 Sarasa UI SC，编程和终端字体通常使用等宽字体，包括 Sarasa Mono SC、Sarasa Term SC、Sarasa Fixed SC。

## 装机必备

|名称|描述|
| :---------------: | :-------------------------------------------: |
|[VS Code](https://code.visualstudio.com/)|强大轻量级 IDE + Agent Coder|
|~~[Trae](https://www.trae.cn/)~~|字节跳动 Agent Coder|
|[Microsoft Office](https://www.microsoft.com/zh-cn/microsoft-365/)|办公软件全家桶|
|[Clash Verge Rev](https://www.clashverge.dev/)|基于 Mihomo 内核的 Clash 客户端|
|[Office Tool Plus](https://otp.landian.vip/zh-cn/)|快速自定义安装 Office 软件|
|[Notepad3](https://rizonesoft.com/downloads/notepad3/)|国产 Notepad++ 平替<br />|
|[SumatraPDF](https://www.sumatrapdfreader.org/free-pdf-reader)|轻量化 PDF 阅读器|
|[LocalSend](https://localsend.org/)|局域网文件传输|
|[Snipaste](https://www.snipaste.com/)|截图|
|[Pot](https://pot-app.com/)|全局翻译|
|[思源笔记](https://b3log.org/siyuan/)|隐私优先的本地知识库|
|[Obsidian](https://obsidian.md/)|插件系统最为丰富的知识库|
|[7-Zip](https://www.7-zip.org/)|压缩|
|[Draw.io](https://app.diagrams.net/)|开源绘图|
|~~[Drawnix](https://drawnix.com/)~~|开源白板工具|
|[PotPlayer](https://potplayer.daum.net/)|全能视频播放器|
|[PowerToys](https://learn.microsoft.com/zh-cn/windows/powertoys/)|Windows 系统官方外挂|
|[uTools](https://www.u-tools.cn/)|功能丰富的插件应用生态|
|~~[OpenFiles](https://openfiles.pansysoft.app/)~~|~~开源万能格式文件查看器~~|
|[Allen Explorer](https://www.allenxiang.com/)|类 Chrome 的强大文件资源管理器|
|[Inkscape](https://inkscape.org/)|免费矢量图编辑器|

## 文献管理 Zotero

- [Zotero](https://www.zotero.org/) 桌面端
- [Zotero Connector](https://www.zotero.org/download/) 浏览器插件

- 插件

  - [Actions and Tags for Zotero](https://github.com/windingwind/zotero-actions-tags/releases/)：批量标签管理

{{< callout type="tips" >}}

关于更多的 Zotero 插件，请参考 [Zotero 插件商店](https://zotero-chinese.com/plugins/)。

{{< /callout >}}

## 编曲

- Cubase 专业 DAW（数字音频工作站）

  - Prism 音频转 MIDI 插件
  - Song Master Pro 音频分析
- Sibelius 专业打谱软件

  - NotePerformer 5 高质量替换音源

### 插件

- [VoiceMeeter Banana](https://vb-audio.com/Voicemeeter/banana.htm) 专业虚拟音频混音软件
- [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) 提供虚拟 MIDI 输入输出

### 音源

- [Pianoteq](https://www.modartt.com/pianoteq_overview) 物理建模钢琴音源
- [BBC Symphony Orchestra](https://www.spitfireaudio.com/en-us/collections/bbc-symphony-orchestra) 专业管弦音源
- ~~Keyscape 四巨头之钢琴音源~~
- Ample 系列民族乐器音源

## PowerShell

Windows 系统自带的 PowerShell 版本老旧，推荐安装最新的 [PowerShell 7](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows)。

```powershell
winget install --id Microsoft.PowerShell --source winget
```

### 终端美化

安装完成后，再安装 [Oh My Posh](https://ohmyposh.dev/docs/installation/windows) 以美化 PowerShell 终端。

```powershell
winget install JanDeDobbeleer.OhMyPosh --source winget --scope user --force
```

创建配置文件：

```powershell
notepad $PROFILE
```

并在文件中添加以下内容：

```powershell
oh-my-posh init pwsh | Invoke-Expression
```

然后让配置生效：

```powershell
. $PROFILE
```

如果想要更改主题，使用 `--config` 参数指定主题配置文件即可。可以从 [Oh My Posh 主题库](https://ohmyposh.dev/docs/themes) 搜寻喜欢的主题。

```powershell
oh-my-posh init pwsh --config <THEME_NAME> | Invoke-Expression
```

## WSL

根据最新的 [Microsoft 官方 WSL 安装指南](https://learn.microsoft.com/zh-cn/windows/wsl/install)，~~首先在“控制面板 –> 程序 –> 启用或关闭 Windows 功能”中启用适用于 Windows 的 Linux 子系统和 Hyper-V。~~ 无需手动提前配置再安装，直接在 PowerShell（管理员权限）中执行以下命令安装 WSL 和 Ubuntu 发行版：

```powershell
wsl --install -d Ubuntu
```

安装完成后，打开 Ubuntu 终端，设置用户名和密码。

更新软件包：

```bash
sudo apt update && sudo apt upgrade
```

### 终端美化

推荐使用 [Oh My Zsh](https://ohmyz.sh/) 美化终端。首先需要安装 Zsh：

```bash
sudo apt install zsh
```

设置 Zsh 为默认 shell：

```bash
chsh -s $(which zsh)
```

然后安装 Oh My Zsh：

1. 使用 curl 安装：

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

2. 使用 wget 安装：

```bash
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

安装 `zsh-syntax-highlighting` 插件以实现语法高亮：

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
${ZSH:-~/.oh-my-zsh}/plugins/zsh-syntax-highlighting
```

安装 `zsh-autosuggestions` 插件以实现命令自动补全：

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions.git \
${ZSH:-~/.oh-my-zsh}/plugins/zsh-autosuggestions
```

编辑 `~/.zshrc` 文件，将它们都添加到插件列表中：

```bash
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
```

最后，重新加载 Zsh 配置：

```bash
source ~/.zshrc
```

### 网络

为了使 WSL 可以和 Windows 系统共享网络，需要将 WSL 的网络模式设置为桥接模式。在用户目录下创建或编辑 `.wslconfig` 文件，添加以下内容：

```ini
[wsl2]
networkingMode=mirrored
dnsTunneling=true
firewall=true
autoProxy=true
```

### 访问 Windows 宿主文件系统

Windows C 盘挂载在 `/mnt/c`。因此，可以通过符号链接将 Windows 文件系统中的常用文件夹作为链接目标，例如：

```bash
ln -s /mnt/c/Users/<USER>/Downloads ~/downloads
```

## WSL 开发环境

### Python

#### Conda

推荐使用 [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) 作为 Python 包管理器。

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

使用以下命令激活 Conda 的 `base` 环境：

```bash
source ~/miniconda3/bin/activate
```

使用以下命令激活使用 Conda 但不进入 `base` 环境：

```bash
source ~/miniconda3/etc/profile.d/conda.sh
```

如果希望每次打开终端时自动激活 Conda，可以在安装成功后的问询中选择 `yes`，或者手动执行以下命令：

```bash
conda init          # 对当前 shell 生效
conda init --all    # 对所有 shell 生效
```

#### uv

[uv](https://docs.astral.sh/uv/) 是一个快速的 Python 包管理器，推荐使用它来安装 Python 包。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Node.js

推荐使用 `nvm` 来安装和管理不同版本的 [Node.js](https://nodejs.org/)。

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
```

安装最新版的 Node.js LTS：

```bash
nvm install lastest
```

### Go

推荐使用 [gvm](https://github.com/moovweb/gvm) 来安装和管理不同版本的 Go。

```bash
sudo apt-get install bison
zsh < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
```

然后通过 `gvm` 安装 Go 版本：

```bash
gvm install go1.4
gvm use go1.4 [--default]
```

当然，也可以直接从 [Go](https://golang.google.cn/dl/) 官方网站下载安装包进行安装。

#### Hugo

[Hugo](https://gohugo.io/) 是一个流行的静态网站生成器，推荐使用它来搭建个人博客。Hugo 的安装需要先安装 Go 环境，当然使用 Debian 的包管理器可以自动安装 Go 的环境。

一般来说，需要安装 `extended` 版本。通过 APT 安装的 Hugo 已经包含了 `extended` 版本。

```bash
sudo apt install hugo
```

当然，也可以直接前往 [GitHub](https://github.com/gohugoio/hugo/releases) 发行版页面下载安装包。有些主题对于 Hugo 的版本有要求，建议安装最新版本。

### Tex

推荐使用 [TeX Live](https://www.tug.org/texlive/) 作为 LaTeX 发行版。

通过 `apt` 安装较为方便，但版本可能较旧。

```bash
sudo apt install texlive-full
```

## Git

Windows 需要单独安装 [Git for Windows](https://git-scm.com/install/windows)，推荐使用 `winget` 进行安装：

```powershell
winget install --id Git.Git --source winget
```

Linux 发行版默认安装 Git。首先全局配置用户名和邮箱：

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

推荐使用 SSH 密钥进行身份验证。生成 SSH 密钥对：

```bash
ssh-keygen -t rsa -C "comment"
```

将公钥添加到 GitHub 账户中。`-C` 表示为 SSH 密钥添加备注。

```bash
cat ./.ssh/id_rsa.pub
```

## Docker

推荐使用 [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/) 来管理 Docker 容器。安装完成后，可以通过 WSL 终端直接使用 Docker 命令。

{{< callout type="error" >}}

不推荐使用 Ubuntu Server 的安装方式在 WSL 中安装 Docker，因为这种方式需要额外配置 Docker 的守护进程，且不如 Docker Desktop 方便。

{{< /callout >}}

## Agent

### CLI 类 Agent

#### Claude Code

使用 Anthropic 官方的安装脚本安装 [Claude Code CLI](https://claude.com/product/claude-code)。

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

如要通过 API Key 接入非 Anthropic 模型（例如 MiniMax），配置 `~/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.minimaxi.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "<MINIMAX_API_KEY>",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "ANTHROPIC_MODEL": "MiniMax-M3",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "MiniMax-M3",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "MiniMax-M3",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "MiniMax-M3",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "512000"
  }
}
```

还要新增 onboarding 标记，编辑 `~/.claude.json`

```json
{
  "hasCompletedOnboarding": true
}
```

#### Codex

OpenAI 官方推荐使用 `npm` 安装 [Codex CLI](https://developers.openai.com/codex/quickstart?setup=cli)。

```bash
npm i -g @openai/codex
```

如要通过 API Key 接入非 OpenAI 模型，配置 `~/.codex/auth.json`

```json
{
  "OPENAI_API_KEY": "<YOUR_API_KEY>"
}
```

配置 `~/.codex/config.toml`

```toml
model_provider = "<PROVIDER_NAME>"
model = "gpt-5.5"
model_reasoning_effort = "high"
disable_response_storage = true

[model_providers.<PROVIDER_NAME>]
name = "<PROVIDER_NAME>"
wire_api = "responses"
requires_openai_auth = false
base_url = "<PROVIDER_API_URL>"
```

#### ~~OpenCode~~

使用官方提供的安装脚本安装 [OpenCode CLI](https://opencode.ai/zh)。

```bash
curl -fsSL https://opencode.ai/install | bash
```

使用 `npm` 安装 [OpenCode CLI](https://opencode.ai/zh)。

```bash
npm i -g opencode-ai
```

### Claw 类 Agent

#### ~~OpenClaw~~

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

#### ~~Hermes Agent~~

```bash
curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash
```

#### Desktop for Windows

- [Codex Desktop](https://openai.com/zh-Hans-CN/index/codex-for-almost-everything/) 👉 Codex CLI 的重大更新和升级
- [WorkBuddy](https://copilot.tencent.com/work/) 👉 腾讯出品龙虾，小白友好

### Agent 管理

- [CC Switch](https://www.ccswitch.io/zh/) 👉 统一管理 API 提供商

- [Cherry Studio](https://www.cherry-ai.com/) 👉 超级 AI 工作站
