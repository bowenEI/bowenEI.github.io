---
title: "重装 Windows 系统和软件指南"
date: 2025-10-27T15:34:18+08:00
lastmod: 2025-10-29T17:00:00+08:00
draft: false
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

### 永久禁用更新

注册表定位至

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings
```

新建 `DWORD` 值 `FlightSettingsMaxPauseDays` 为 65535（0xFFFF），即最多可暂停更新 65535 天。然后在设置中即可发现选择暂停更新的时间更长。

### 杂项

使用 [DesktopOK](https://www.softwareok.com/?seite=Microsoft/DesktopOK) 可以定制系统字体。

字体推荐更纱黑体（Sarasa）。系统字体可以使用 Sarasa UI SC，编程和终端字体通常使用等宽字体，包括 Sarasa Mono SC、Sarasa Term SC、Sarasa Fixed SC。

## 常用软件安装

### IDE

- [VS Code](https://code.visualstudio.com/)
- [Trae](https://www.trae.cn/)

### 装机必备

- [Microsoft Office](https://www.microsoft.com/zh-cn/microsoft-365/)
  - 可从 [MSDN](https://msdn.itellyou.cn/) 下载 Microsoft 各类软件资源
  - [Office Tool Plus](https://otp.landian.vip/zh-cn/) 快速自定义安装 Office 软件
- [Notepad3](https://rizonesoft.com/downloads/notepad3/)
- [SumatraPDF](https://www.sumatrapdfreader.org/free-pdf-reader)
- [LocalSend](https://localsend.org/)
- [Snipaste](https://www.snipaste.com/)
  - Microsoft Store [下载地址](https://apps.microsoft.com/detail/9p1wxpkb68kx)
- [Pot](https://pot-app.com/)
- [思源笔记](https://b3log.org/siyuan/)
  - Microsoft Store [下载地址](https://apps.microsoft.com/detail/9p7hpmxp73k4)
- [7-Zip](https://www.7-zip.org/)
- [Draw.io](https://app.diagrams.net/)
  - Microsoft Store [下载地址](https://apps.microsoft.com/detail/9mvvszk43qqw)
- [PotPlayer](https://potplayer.daum.net/)
  - Microsoft Store [下载地址](https://apps.microsoft.com/detail/xp8bsbgqw2dks0)
- [PowerToys](https://learn.microsoft.com/zh-cn/windows/powertoys/)
  - Microsoft Store [下载地址](https://apps.microsoft.com/detail/xp89dcgq3k6vld)

### 文献管理 Zotero

- [Zotero](https://www.zotero.org/)
- [Zotero Connector](https://www.zotero.org/download/) 浏览器插件

Zotero 是一个强大的文献管理工具，推荐安装以下插件以增强功能：

- [Actions and Tags for Zotero](https://github.com/windingwind/zotero-actions-tags/releases/)：提供批量标签管理功能。

{{< callout type="tips" >}}

关于更多的 Zotero 插件，请参考 [Zotero 插件商店](https://zotero-chinese.com/plugins/)。

{{< /callout >}}

## WSL 配置

### 安装

> 参考资料：[Microsoft 官方 WSL 安装指南](https://learn.microsoft.com/zh-cn/windows/wsl/install)

首先在“控制面板 --> 程序 --> 启用或关闭 Windows 功能”中启用适用于 Windows 的 Linux 子系统和 Hyper-V。

重启系统后，在 PowerShell（管理员权限）中执行以下命令安装 WSL 和 Ubuntu 发行版：

```powershell
wsl --install
```

安装完成后，打开 Ubuntu 终端，设置用户名和密码。

更新软件包：

```bash
sudo apt update && sudo apt upgrade -y
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

## 开发环境

> 以下配置均在 WSL 终端中进行。

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

目前最新的 Node.js LTS 版本为 22：

```bash
nvm install 22
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

## Docker

推荐使用 [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/) 来管理 Docker 容器。安装完成后，可以通过 WSL 终端直接使用 Docker 命令。

{{< callout type="error" >}}

不推荐使用 Ubuntu Server 的安装方式在 WSL 中安装 Docker，因为这种方式需要额外配置 Docker 的守护进程，且不如 Docker Desktop 方便。

{{< /callout >}}

## Nvidia 显卡驱动

推荐使用 [Nvidia 官方驱动](https://www.nvidia.cn/geforce/drivers/) 来查找和安装合适的显卡驱动。驱动版本是向下兼容的，一般安装最新版本即可。

安装完成后，通过 `nvidia-smi` 命令检查驱动是否安装成功，并且查看 WSL 的驱动版本是否与 Windows 系统的驱动版本一致。

## 数据库

### SQLite

SQLite 为所有 Linux 发行版默认安装，无需额外配置。

### MongoDB

- 服务端：[MongoDB Community Edition](https://www.mongodb.com/try/download/community)
- 客户端：[MongoDB Compass](https://www.mongodb.com/products/tools/compass)

### Redis

- 服务端：[Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/)
- 客户端：[RedisInsight](https://redis.io/insight/)

## 内网穿透

推荐使用 [Tailscale](https://tailscale.com/) 进行内网穿透。其本质是基于 WireGuard 的零配置 VPN，只需要身份认证即可让多个端侧设备安全互联，而无需集中式 VPN 服务器。

### 客户端

通常情况下，客户端都是 Windows 系统，直接访问[官网](https://tailscale.com/download/windows)下载安装包即可。安装完成后同样需要进行身份认证。

### 服务端

通常情况下，服务端都是 Linux 系统，安装 Tailscale 服务端需要在 Linux 系统中执行安装脚本。

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

这对于 WSL 也同样适用。

根据安装提示，安装完成后需要执行下列命令来连接 Tailscale 网络。

```bash
tailscale up
```

此过程中，需要进行身份认证，认证成功后即可连接 Tailscale 网络。

```bash
sudo apt install ssh
sudo systemctl enable ssh
sudo systemctl start ssh
```

最后，别忘了在服务端安装并启动 SSH 服务。
