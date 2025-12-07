# Git全量指令练习教程

## 前言
本教程将使用 `git_practice_test.py` 文件来练习所有Git指令，从基础到高级，保姆级详细说明每一步操作和原因。

## 目录
1. [Git基础配置](#1-git基础配置)
2. [工作区与暂存区操作](#2-工作区与暂存区操作)
3. [提交历史管理](#3-提交历史管理)
4. [分支管理](#4-分支管理)
5. [合并与冲突解决](#5-合并与冲突解决)
6. [标签管理](#6-标签管理)
7. [远程仓库操作](#7-远程仓库操作)
8. [高级功能](#8-高级功能)

---

## 1. Git基础配置

### 1.1 查看Git版本
```bash
git --version
```
**原因**：检查Git是否正确安装。

### 1.2 配置用户名和邮箱
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```
**原因**：设置提交代码时的身份信息，这将出现在所有提交记录中。

### 1.3 查看配置信息
```bash
git config --list
git config user.name
```
**原因**：验证配置是否正确。

---

## 2. 工作区与暂存区操作

### 2.1 查看当前仓库状态
```bash
git status
```
**原因**：了解仓库当前的状态，包括已修改、已暂存和未跟踪的文件。

### 2.2 跟踪新文件
```bash
git add git_practice_test.py
```
**原因**：将新创建的测试文件添加到暂存区，开始跟踪它。

### 2.3 查看文件变化
```bash
git diff
```
**原因**：查看工作区中文件的具体修改内容（未暂存的修改）。

### 2.4 查看已暂存的变化
```bash
git diff --staged
```
**原因**：查看已暂存但尚未提交的文件修改内容。

### 2.5 提交更改
```bash
git commit -m "Initial commit: Add git_practice_test.py"
```
**原因**：将暂存区的更改提交到版本库，创建一个新的提交记录。

### 2.6 修改文件并再次提交
```bash
# 修改文件（使用编辑器添加以下内容）
echo "# 添加新内容" >> git_practice_test.py

git status
git add git_practice_test.py
git commit -m "Add new content to test file"
```
**原因**：练习完整的修改-暂存-提交流程。

### 2.7 撤销工作区修改
```bash
# 先修改文件
echo "This change will be discarded" >> git_practice_test.py

git status
git checkout -- git_practice_test.py
git status
```
**原因**：学习如何撤销工作区中尚未暂存的修改。

### 2.8 撤销暂存区修改
```bash
# 修改并暂存文件
echo "This change will be unstaged" >> git_practice_test.py
git add git_practice_test.py
git status

git reset HEAD git_practice_test.py
git status
```
**原因**：学习如何将文件从暂存区移回工作区。

---

## 3. 提交历史管理

### 3.1 查看提交历史
```bash
git log
git log --oneline
git log --graph --oneline --all
```
**原因**：查看所有提交记录，了解项目的历史变更。

### 3.2 查看特定文件的提交历史
```bash
git log -- git_practice_test.py
git log -p -- git_practice_test.py
```
**原因**：查看特定文件的所有修改历史和具体修改内容。

### 3.3 查看提交详情
```bash
git show <commit_id>
```
**原因**：查看某个特定提交的详细信息，包括修改的文件和内容。

### 3.4 回退到之前的提交
```bash
# 查看当前提交ID
git log --oneline

# 回退到上一个提交
git reset --hard HEAD~1

# 查看文件内容
cat git_practice_test.py
```
**原因**：学习如何将仓库回退到之前的某个提交状态。

### 3.5 恢复到最新提交
```bash
# 查看所有提交（包括已回退的）
git reflog

# 恢复到最新提交
git reset --hard <latest_commit_id>
```
**原因**：学习如何从回退状态恢复到最新的提交。

### 3.6 修改最新提交信息
```bash
# 修改文件
echo "Fixing something" >> git_practice_test.py
git add git_practice_test.py
git commit --amend -m "Update test file and fix commit message"
```
**原因**：学习如何修改最新一次提交的信息或添加新的修改到最新提交。

---

## 4. 分支管理

### 4.1 查看分支列表
```bash
git branch
git branch -a  # 查看所有分支（包括远程）
```
**原因**：了解当前仓库中的所有分支。

### 4.2 创建新分支
```bash
git branch feature-branch
git checkout -b feature-branch  # 创建并切换到新分支
```
**原因**：创建一个新的分支来开发新功能，避免影响主分支。

### 4.3 切换分支
```bash
git checkout main
git checkout feature-branch
```
**原因**：在不同分支之间切换工作。

### 4.4 在新分支上修改文件
```bash
# 确保在feature-branch分支上
git branch

echo "# Feature branch content" >> git_practice_test.py
git add git_practice_test.py
git commit -m "Add feature branch content"
```
**原因**：在新分支上进行开发工作。

### 4.5 查看分支差异
```bash
git diff main feature-branch
git diff main feature-branch -- git_practice_test.py
```
**原因**：查看两个分支之间的差异，特别是特定文件的差异。

### 4.6 删除分支
```bash
git checkout main
git branch -d feature-branch  # 删除已合并的分支
git branch -D feature-branch  # 强制删除未合并的分支
```
**原因**：删除不再需要的分支，保持仓库整洁。

---

## 5. 合并与冲突解决

### 5.1 合并分支（无冲突）
```bash
# 先确保feature-branch有新的提交
git checkout feature-branch
echo "# More feature content" >> git_practice_test.py
git add git_practice_test.py
git commit -m "Add more feature content"

# 切换回main分支并合并
git checkout main
git merge feature-branch
```
**原因**：将feature-branch的修改合并到main分支。

### 5.2 创建冲突
```bash
# 在main分支修改文件
git checkout main
echo "# Main branch change" >> git_practice_test.py
git add git_practice_test.py
git commit -m "Modify file in main branch"

# 在feature-branch也修改相同位置
git checkout feature-branch
echo "# Feature branch change" >> git_practice_test.py
git add git_practice_test.py
git commit -m "Modify file in feature branch"
```
**原因**：创建一个合并冲突场景，以便练习解决冲突。

### 5.3 解决冲突
```bash
# 尝试合并，会产生冲突
git checkout main
git merge feature-branch

# 查看冲突文件
git status
cat git_practice_test.py

# 手动编辑文件，解决冲突
# 冲突部分会显示为：
# <<<<<<< HEAD
# # Main branch change
# =======
# # Feature branch change
# >>>>>>> feature-branch

# 选择保留哪个版本，或者合并两者
# 解决后提交
git add git_practice_test.py
git commit -m "Resolve merge conflict"
```
**原因**：学习如何解决合并冲突，这是团队协作中常见的情况。

### 5.4 使用变基合并
```bash
# 创建一个新分支进行变基练习
git checkout -b rebase-branch
echo "# Rebase branch content" >> git_practice_test.py
git add git_practice_test.py
git commit -m "Add rebase content"

# 切换回main分支并添加新提交
git checkout main
echo "# Main branch new commit" >> git_practice_test.py
git add git_practice_test.py
git commit -m "Add new commit in main"

# 切换回rebase-branch进行变基
git checkout rebase-branch
git rebase main

# 合并回main分支
git checkout main
git merge rebase-branch
```
**原因**：学习使用变基（rebase）来保持提交历史的线性，这在某些团队工作流程中很有用。

---

## 6. 标签管理

### 6.1 查看标签
```bash
git tag
git tag -l "v1.*"  # 查看特定模式的标签
```
**原因**：了解仓库中已有的标签。

### 6.2 创建轻量标签
```bash
git tag v1.0
```
**原因**：创建一个简单的标签，仅包含提交ID。

### 6.3 创建带注释的标签
```bash
git tag -a v1.1 -m "Version 1.1 release"
```
**原因**：创建一个带有详细说明的标签，通常用于发布版本。

### 6.4 查看标签详情
```bash
git show v1.1
```
**原因**：查看标签的详细信息，包括注释和指向的提交。

### 6.5 为之前的提交打标签
```bash
git log --oneline  # 找到要打标签的提交ID
git tag -a v0.9 <commit_id> -m "Version 0.9 release"
```
**原因**：学习如何为历史提交添加标签。

### 6.6 删除标签
```bash
git tag -d v1.0
```
**原因**：删除不再需要的标签。

---

## 7. 远程仓库操作

### 7.1 查看远程仓库
```bash
git remote
git remote -v  # 查看远程仓库URL
```
**原因**：了解当前配置的远程仓库。

### 7.2 添加远程仓库
```bash
git remote add origin <remote_repository_url>
```
**原因**：关联本地仓库与远程仓库，以便进行同步。

### 7.3 推送本地分支到远程
```bash
git push -u origin main
```
**原因**：将本地main分支推送到远程仓库，并建立跟踪关系。

### 7.4 推送标签到远程
```bash
git push origin v1.1
git push origin --tags  # 推送所有标签
```
**原因**：将本地标签推送到远程仓库，以便团队成员共享。

### 7.5 从远程仓库拉取更新
```bash
git pull
```
**原因**：获取远程仓库的最新更新并合并到本地分支。

### 7.6 从远程仓库获取更新但不合并
```bash
git fetch
git diff origin/main
```
**原因**：获取远程更新但不自动合并，以便先查看差异再决定如何处理。

### 7.7 克隆远程仓库
```bash
git clone <remote_repository_url> new_project
```
**原因**：创建一个远程仓库的本地副本。

---

## 8. 高级功能

### 8.1 查看文件的每行最后修改者
```bash
git blame git_practice_test.py
```
**原因**：查看文件中每行代码的最后修改者和提交信息，用于代码审查。

### 8.2 储藏工作
git stash
git stash
```
**原因**：将当前工作区的修改临时保存，以便切换到其他分支处理紧急任务。

### 8.3 查看储藏列表
```bash
git stash list
```
**原因**：查看所有储藏的工作。

### 8.4 恢复储藏的工作
```bash
git stash apply  # 恢复最新的储藏但保留储藏记录
git stash pop    # 恢复最新的储藏并删除储藏记录
git stash apply stash@{1}  # 恢复特定的储藏
```
**原因**：恢复之前储藏的工作。

### 8.5 删除储藏
```bash
git stash drop  # 删除最新的储藏
git stash clear  # 清除所有储藏
```
**原因**：删除不再需要的储藏。

### 8.6 清理未跟踪的文件
```bash
git clean -n  # 查看将被清理的文件
git clean -f  # 强制清理未跟踪的文件
git clean -df # 清理未跟踪的文件和目录
```
**原因**：清理仓库中不需要的临时文件和目录。

### 8.7 查看仓库历史统计
```bash
git shortlog
git shortlog -s -n  # 按提交次数排序
```
**原因**：查看贡献者的提交统计信息。

### 8.8 生成提交历史图形
```bash
git log --graph --oneline --all --decorate
```
**原因**：以图形化方式查看提交历史和分支关系，更直观地了解项目发展。

---

## 总结
通过使用 `git_practice_test.py` 文件完成以上所有操作，您已经练习了Git的大部分核心指令。建议多次重复练习，直到熟练掌握这些指令的使用场景和操作方法。

Git是一个强大的版本控制系统，熟练使用它将大大提高您的开发效率和团队协作能力。
