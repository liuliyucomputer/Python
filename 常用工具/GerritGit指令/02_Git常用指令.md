# Git常用指令

## 1. 仓库管理

### 1.1 创建本地仓库

```bash
# 在当前目录初始化Git仓库
git init

# 在指定目录初始化Git仓库
git init /path/to/repo
```

### 1.2 克隆远程仓库

```bash
# 克隆远程仓库
git clone https://github.com/user/repo.git

# 克隆远程仓库到指定目录
git clone https://github.com/user/repo.git /path/to/local/repo

# 克隆时指定分支
git clone -b branch-name https://github.com/user/repo.git

# 克隆时只获取最新版本（浅克隆）
git clone --depth 1 https://github.com/user/repo.git
```

### 1.3 查看仓库状态

```bash
# 查看当前仓库状态
git status

# 查看当前仓库状态（简洁格式）
git status -s
```

### 1.4 查看仓库信息

```bash
# 查看Git配置信息
git config --list

# 查看当前分支和提交信息
git log --oneline --decorate

# 查看远程仓库信息
git remote -v

# 查看仓库统计信息
git count-objects -v
```

## 2. 文件操作

### 2.1 查看文件差异

```bash
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最后一次提交的差异
git diff --staged

# 查看工作区与最后一次提交的差异
git diff HEAD

# 查看两个版本之间的差异
git diff commit1 commit2

# 查看两个分支之间的差异
git diff branch1 branch2

# 只查看差异摘要
git diff --stat

# 忽略空格差异
git diff -w
```

### 2.2 添加文件到暂存区

```bash
# 添加指定文件到暂存区
git add file.txt

# 添加多个文件到暂存区
git add file1.txt file2.txt

# 添加所有修改的文件到暂存区
git add .

# 添加当前目录下所有修改的文件到暂存区
git add --all

# 添加指定目录下所有修改的文件到暂存区
git add /path/to/dir/
```

### 2.3 从暂存区移除文件

```bash
# 从暂存区移除文件，但保留工作区的文件
git reset HEAD file.txt

# 从暂存区和工作区同时移除文件
git rm file.txt

# 强制从暂存区和工作区移除文件
git rm -f file.txt

# 只从暂存区移除文件，保留工作区的文件
git rm --cached file.txt
```

### 2.4 撤销文件修改

```bash
# 撤销工作区的修改（恢复到暂存区的状态）
git checkout -- file.txt

# 撤销工作区的所有修改（恢复到最后一次提交的状态）
git checkout HEAD -- .

# 撤销工作区的修改（使用reset命令）
git reset HEAD file.txt
git checkout -- file.txt
```

### 2.5 查看文件历史

```bash
# 查看文件的修改历史
git log --follow file.txt

# 查看文件的修改历史（简洁格式）
git log --oneline --follow file.txt

# 查看文件的详细修改内容
git log -p file.txt

# 查看文件的修改统计信息
git log --stat file.txt
```

## 3. 提交管理

### 3.1 提交修改

```bash
# 提交暂存区的修改
git commit -m "Commit message"

# 提交所有修改的文件（跳过暂存区）
git commit -am "Commit message"

# 提交时显示差异
git commit -v

# 修改最后一次提交
git commit --amend

# 修改最后一次提交的信息
git commit --amend -m "New commit message"
```

### 3.2 查看提交历史

```bash
# 查看提交历史
git log

# 查看提交历史（简洁格式）
git log --oneline

# 查看提交历史（带图形化分支）
git log --oneline --graph

# 查看提交历史（显示所有分支）
git log --oneline --graph --all

# 查看提交历史（限制数量）
git log -n 5

# 查看提交历史（显示作者和时间）
git log --pretty=format:"%h %an %ad %s" --date=short

# 查看提交历史（按作者过滤）
git log --author="Your Name"

# 查看提交历史（按提交信息过滤）
git log --grep="Bug fix"

# 查看提交历史（按时间过滤）
git log --since="2023-01-01" --until="2023-12-31"
```

### 3.3 回退提交

```bash
# 回退到指定提交（保留工作区和暂存区的修改）
git reset --soft commit-id

# 回退到指定提交（保留工作区的修改，重置暂存区）
git reset --mixed commit-id

# 回退到指定提交（重置工作区和暂存区）
git reset --hard commit-id

# 回退到上一次提交
git reset --hard HEAD^  # 或 HEAD~1

# 回退到上上次提交
git reset --hard HEAD^^  # 或 HEAD~2

# 撤销特定提交（创建新提交）
git revert commit-id

# 撤销多个提交
git revert commit1..commit2
```

### 3.4 查看提交详情

```bash
# 查看指定提交的详情
git show commit-id

# 查看指定提交的文件修改
git show commit-id:file.txt

# 查看最后一次提交的详情
git show HEAD
```

## 4. 分支管理

### 4.1 查看分支

```bash
# 查看本地分支
git branch

# 查看所有分支（本地+远程）
git branch -a

# 查看远程分支
git branch -r

# 查看分支和提交信息
git branch -v

# 查看分支和上游分支信息
git branch -vv
```

### 4.2 创建分支

```bash
# 创建新分支
git branch branch-name

# 创建新分支并切换到该分支
git checkout -b branch-name

# 创建新分支并指定上游分支
git checkout -b branch-name origin/master

# 基于指定提交创建分支
git branch branch-name commit-id
```

### 4.3 切换分支

```bash
# 切换到指定分支
git checkout branch-name

# 切换到上一个分支
git checkout -

# 切换到主分支
git checkout master  # 或 main
```

### 4.4 合并分支

```bash
# 合并指定分支到当前分支
git merge branch-name

# 合并时创建合并提交
git merge --no-ff branch-name

# 合并时使用变基
git merge --squash branch-name
```

### 4.5 删除分支

```bash
# 删除本地分支（只有当分支已经合并时才能删除）
git branch -d branch-name

# 强制删除本地分支（即使分支未合并）
git branch -D branch-name

# 删除远程分支
git push origin --delete branch-name

# 删除远程分支的本地引用
git fetch origin --prune
```

### 4.6 重命名分支

```bash
# 重命名本地分支
git branch -m old-branch-name new-branch-name

# 重命名当前分支
git branch -m new-branch-name

# 重命名本地分支并推送新名称到远程
git branch -m old-branch-name new-branch-name
git push origin new-branch-name
git push origin --delete old-branch-name
git branch -u origin/new-branch-name
```

## 5. 远程仓库操作

### 5.1 添加远程仓库

```bash
# 添加远程仓库
git remote add origin https://github.com/user/repo.git

# 添加多个远程仓库
git remote add upstream https://github.com/upstream/repo.git
```

### 5.2 查看远程仓库

```bash
# 查看远程仓库
git remote

# 查看远程仓库详细信息
git remote -v

# 查看远程仓库的URL
git remote get-url origin

# 查看远程仓库的信息
git remote show origin
```

### 5.3 修改远程仓库

```bash
# 修改远程仓库的URL
git remote set-url origin https://github.com/user/new-repo.git

# 添加远程仓库的push URL
git remote set-url --push origin https://github.com/user/repo.git
```

### 5.4 删除远程仓库

```bash
# 删除远程仓库
git remote remove origin
```

### 5.5 拉取远程修改

```bash
# 拉取远程仓库的修改（默认分支）
git pull

# 拉取指定远程仓库的修改
git pull origin

# 拉取指定远程分支的修改到当前分支
git pull origin branch-name

# 拉取远程分支的修改并变基
git pull --rebase origin branch-name
```

### 5.6 推送修改到远程

```bash
# 推送当前分支到远程仓库（默认分支）
git push

# 推送当前分支到指定远程仓库
git push origin

# 推送指定分支到远程仓库
git push origin branch-name

# 推送当前分支并设置上游分支
git push -u origin branch-name

# 推送所有分支到远程仓库
git push --all origin

# 推送标签到远程仓库
git push --tags origin

# 强制推送到远程仓库（慎用）
git push -f origin branch-name
```

### 5.7 同步远程仓库

```bash
# 同步远程仓库的分支和标签
git fetch origin

# 同步所有远程仓库的分支和标签
git fetch --all

# 同步远程仓库并删除本地不存在的远程分支
git fetch origin --prune
```

## 6. 标签管理

### 6.1 查看标签

```bash
# 查看所有标签
git tag

# 查看标签（带过滤）
git tag -l "v1.*"

# 查看标签的详细信息
git show tag-name
```

### 6.2 创建标签

```bash
# 创建轻量标签
git tag tag-name

# 创建带注释的标签
git tag -a tag-name -m "Tag message"

# 基于指定提交创建标签
git tag tag-name commit-id

# 创建带GPG签名的标签
git tag -s tag-name -m "Tag message"
```

### 6.3 推送标签

```bash
# 推送指定标签到远程仓库
git push origin tag-name

# 推送所有标签到远程仓库
git push --tags origin
```

### 6.4 删除标签

```bash
# 删除本地标签
git tag -d tag-name

# 删除远程标签
git push origin --delete tag-name
```

## 7. 冲突解决

### 7.1 查看冲突文件

```bash
# 查看冲突文件
git status

# 查看冲突内容
git diff
```

### 7.2 解决冲突

1. 手动编辑冲突文件，解决冲突
2. 添加解决冲突后的文件到暂存区
3. 提交解决冲突的修改

```bash
# 解决冲突后添加文件到暂存区
git add file.txt

# 提交解决冲突的修改
git commit -m "Resolve conflicts"
```

### 7.3 撤销合并

```bash
# 撤销合并（在合并未提交前）
git merge --abort

# 撤销合并（在合并已提交后）
git reset --hard HEAD^  # 或 HEAD~1
```

## 8. 高级功能

### 8.1 变基（Rebase）

```bash
# 变基当前分支到指定分支
git rebase branch-name

# 变基当前分支到指定提交
git rebase commit-id

# 交互式变基
git rebase -i HEAD~5  # 最近5次提交

# 继续变基
git rebase --continue

# 跳过当前冲突
git rebase --skip

# 中止变基
git rebase --abort
```

### 8.2 贮藏（Stash）

```bash
# 贮藏当前工作区的修改
git stash

# 贮藏当前工作区的修改并添加注释
git stash save "Stash message"

# 查看贮藏列表
git stash list

# 查看贮藏的详细信息
git stash show

# 查看贮藏的修改内容
git stash show -p

# 应用最近的贮藏
git stash apply

# 应用指定的贮藏
git stash apply stash@{0}

# 应用贮藏并删除它
git stash pop

# 删除最近的贮藏
git stash drop

# 删除指定的贮藏
git stash drop stash@{0}

# 删除所有贮藏
git stash clear
```

### 8.3 子模块（Submodule）

```bash
# 添加子模块
git submodule add https://github.com/user/submodule.git path/to/submodule

# 克隆包含子模块的仓库
git clone https://github.com/user/repo.git
git submodule init
git submodule update

# 克隆包含子模块的仓库（一键操作）
git clone --recurse-submodules https://github.com/user/repo.git

# 更新子模块
git submodule update --remote
```

### 8.4 忽略文件

创建 `.gitignore` 文件，列出需要忽略的文件和目录：

```
# 忽略所有 .log 文件
*.log

# 忽略 node_modules 目录
node_modules/

# 忽略特定文件
.env

# 忽略 build 目录下的所有文件
build/*

# 但保留 build/assets 目录
build/assets/!
```

### 8.5 查看Git对象

```bash
# 查看Git对象
git cat-file -t object-id  # 查看对象类型
git cat-file -p object-id  # 查看对象内容
git cat-file -s object-id  # 查看对象大小
```

## 9. 总结

本章节介绍了Git日常工作中最常用的指令，包括：

- 仓库管理：初始化、克隆、查看状态
- 文件操作：添加、移除、撤销修改
- 提交管理：提交、查看历史、回退
- 分支管理：创建、切换、合并、删除
- 远程仓库操作：拉取、推送、同步
- 标签管理：创建、推送、删除
- 冲突解决：查看冲突、解决冲突
- 高级功能：变基、贮藏、子模块

这些指令涵盖了Git的核心功能，掌握它们将帮助您高效地使用Git进行版本控制。在实际工作中，您可能会根据项目需求和工作流程选择使用不同的指令组合。

下一章：[Gerrit基础概念](03_Gerrit基础概念.md)