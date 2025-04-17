---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Git 本地仓库"
linktitle: "Git 本地仓库"
date: 2021-12-03T10:03:39+08:00
type: docs
summary: ""
weight: 30
---

<!--more-->

## 创建版本库

```sh
git init
```

即可在当前文件夹创建本地仓库。

## 把文件添加到版本库

### 暂存更改

```sh
git add README.md #将README.md文件添加到版本库
git add .         #将已更改的所有文件添加到版本库
```

### 提交更改

```sh
git commit -m "add README.md"
```

注意，`-m` 参数后面是提交的说明，应当便于他人阅读。

一次 `commit` 会将所有已经暂存的更改提交，因此一个好习惯是在对多个文件都做了修改后，根据需要分别暂存提交。不暂存而直接将所有更改提交是一个不好的习惯。

## 穿梭时光

**Git** 的强大之处就在于它就好像给了我们一个时间轴，让我们可以在过去和未来之间自由穿梭。要知道 **Git** 是如何实现这一功能的，我们首先要了解工作区和暂存区的区别和联系。

### 工作区和暂存区

- 工作区

通常就是指 **Git** 仓库所在的文件目录，是我们直接可以看到的，也是我们工作时的载体。

- 暂存区

在每一个 **Git** 仓库的根目录下都有一个隐藏文件夹，它就是版本库。而暂存区 `stage` 就位于版本库中，它专门用来存放已经添加 `add` 但还未提交 `commit` 的修改。

### 撤销修改

#### 修改未暂存

```sh
git checkout -- README.md
```

该命令可以直接将 `README.md` 文件在**工作区**的修改全部撤销，这里有以下两种情况：

1. `README.md` 自修改后还未暂存，则直接撤销全部工作区修改会回到和上一个版本库一模一样的状态。
2. `README.md` 暂存后又作了修改，则直接撤销全部工作区修改会回到刚刚暂存时的状态。

注：现在新的命令 `restore` 取代 `checkout` 命令，因为 `checkout` 还有其他用途（后文详述）。而且，如果不加两个短横线，该命令就完全三另外一种操作了。为了不混淆，新版 **Git** 提倡使用新的命令。

```sh
git restore README.md
```

#### 修改已暂存

```sh
git reset HEAD README.md
```

注意，这里的 `reset` 命令的含义是将已暂存的修改撤销 `unstage`，重新返回到上一个版本的状态。这里 `HEAD` 表示最新的版本，在后文中，`HEAD` 还会多次出现，并且含义可能各不相同。

### 版本回退

当我们已经提交了修改之后，如果发现有问题想要撤销回到过去，结果发现并不是暂存区那样很容易就撤销了，应该怎么办？

首先，我们需要查看提交日志，使用 `git log` 命令：

```sh
commit 746eb565b0840bc5241d4e16e757bcdb2deec007 (HEAD -> master, origin/master, origin/HEAD)
Author: Fourier-Ubuntu <zhoubw1999@126.com>
Date:   Tue Sep 29 12:58:16 2020 +0800

    add README.md

commit f27f2ad514235263bbe539a9bd3daff9e652a302
Author: Fourier <zhoubw1999@126.com>
Date:   Fri Sep 18 16:04:24 2020 +0800

    update README.md
```

`commit` 后面的一大串十六进制数是通过SHA1哈希算法计算出来的，可以唯一确定一次提交。如果我们想要回到当前版本的上一个版本，可以使用如下命令：

```sh
git reset --hard 746eb
git reset --hard HEAD^
```

*注*

1. 直接写哈希值只需要写几位即可，**Git** 会自动推断是哪一次提交。
2. 在 `HEAD` 的右上角加 `^` 表示它的上一个版本，如果加2个则表示它的上一个版本的上一个版本，以此类推。

### HEAD 指针

本节我们要来彻底弄清楚 `HEAD` 的含义，并且了解 **Git** 版本控制的机制。这一次，`HEAD` 又有了新的称呼——指针。要理解 `HEAD` 指针，我们需要理解 **Git** 版本控制的时间线机制。

在 **Git** 中，每一次提交意味着沿着时间线前进一步，来到一个新的时间点。换句话说，每一次提交都和一个时间点一一对应。每当提交完成后，`HEAD` 指针会指向新的时间点。也就是说，`HEAD` 始终指向当前版本库。因此，要实现版本回退，只需要修改 `HEAD` 指针即可。

### 重返未来

在回退版本后，又发现自己原来写得没有问题，想要再回到最一开始都提交的状态，就需要再次重返未来。但是，当我们再次使用 `git log` 查看历史记录时，却发现 `HEAD` 指针后的所有版本库都不见了！这可如何是好？

这个时候，查看命令历史记录命令 `git reflog` 就派上用场了：

```sh
746eb56 (HEAD -> master, origin/master, origin/HEAD) HEAD@{0}: commit: update README.md
f27f2ad HEAD@{1}: add README.md
```

这样，再用 `git reset` 命令就能够重返未来了。