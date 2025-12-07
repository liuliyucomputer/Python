# Gerrit常用命令

## 1. Gerrit命令行工具

Gerrit提供了命令行工具，通过SSH协议与Gerrit服务器交互。这些命令以`gerrit`为前缀，通过SSH连接到Gerrit服务器执行。

### 1.1 基本连接

```bash
# 连接到Gerrit服务器
ssh -p 29418 admin@localhost gerrit

# 查看Gerrit命令列表
ssh -p 29418 admin@localhost gerrit help

# 查看特定命令的帮助
ssh -p 29418 admin@localhost gerrit help command-name
```

### 1.2 配置SSH密钥

在使用Gerrit命令行工具之前，需要配置SSH密钥：

```bash
# 生成SSH密钥（如果还没有）
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# 查看公钥内容
cat ~/.ssh/id_rsa.pub
```

然后将公钥添加到Gerrit的用户设置中：
1. 登录Gerrit Web界面
2. 点击右上角的用户名，选择"Settings"
3. 点击"SSH Public Keys"
4. 点击"Add Key"，粘贴公钥内容
5. 点击"Add"按钮保存

## 2. 变更管理命令

### 2.1 创建和提交变更

```bash
# 创建分支
git checkout -b feature-branch

# 修改文件
# ...

# 添加文件到暂存区
git add .

# 提交修改（注意：提交信息中必须包含Change-Id）
git commit -m "Add new feature"

# 推送到Gerrit的特殊引用
git push origin HEAD:refs/for/master

# 推送到指定分支
git push origin HEAD:refs/for/branch-name

# 推送到指定分支并设置审查者
git push origin HEAD:refs/for/master%r=reviewer1@example.com,r=reviewer2@example.com

# 推送到指定分支并设置主题
git push origin HEAD:refs/for/master%topic=feature-topic
```

### 2.2 查看变更

```bash
# 查看所有变更
git ls-remote origin refs/changes/*

# 查看特定变更
git ls-remote origin refs/changes/xx/yyyy/zz

# 通过SSH命令查看变更
tssh -p 29418 admin@localhost gerrit query --format=JSON status:open project:your-project
```

### 2.3 更新变更

```bash
# 修改文件
# ...

# 添加文件到暂存区
git add .

# 提交修改（使用--amend更新最后一次提交）
git commit --amend

# 推送到Gerrit的特殊引用（更新现有变更）
git push origin HEAD:refs/for/master
```

### 2.4 放弃变更

```bash
# 通过Web界面放弃变更
# 1. 登录Gerrit Web界面
# 2. 找到要放弃的变更
# 3. 点击"Abandon"按钮

# 通过SSH命令放弃变更
ssh -p 29418 admin@localhost gerrit review --abandon change-id,patch-set
```

### 2.5 恢复变更

```bash
# 通过Web界面恢复变更
# 1. 登录Gerrit Web界面
# 2. 找到要恢复的变更
# 3. 点击"Restore"按钮

# 通过SSH命令恢复变更
ssh -p 29418 admin@localhost gerrit review --restore change-id,patch-set
```

### 2.6 合并变更

```bash
# 通过Web界面合并变更
# 1. 登录Gerrit Web界面
# 2. 找到要合并的变更
# 3. 点击"Submit"按钮

# 通过SSH命令合并变更
ssh -p 29418 admin@localhost gerrit review --submit change-id,patch-set
```

## 3. 审查命令

### 3.1 审查变更

```bash
# 审查变更并提供评分
ssh -p 29418 admin@localhost gerrit review --code-review +2 --verified +1 change-id,patch-set

# 审查变更并提供评论
ssh -p 29418 admin@localhost gerrit review --message "Good work!" change-id,patch-set

# 拒绝变更
ssh -p 29418 admin@localhost gerrit review --code-review -1 --message "Need some changes" change-id,patch-set

# 批准变更
ssh -p 29418 admin@localhost gerrit review --code-review +2 --verified +1 --submit change-id,patch-set
```

### 3.2 添加评论

```bash
# 添加文件级评论
ssh -p 29418 admin@localhost gerrit review --file file.txt --message "This is a file comment" change-id,patch-set

# 添加行级评论
ssh -p 29418 admin@localhost gerrit review --file file.txt --line 10 --message "This is a line comment" change-id,patch-set
```

### 3.3 添加审查者

```bash
# 添加审查者
ssh -p 29418 admin@localhost gerrit set-reviewers --add reviewer1@example.com change-id

# 移除审查者
ssh -p 29418 admin@localhost gerrit set-reviewers --remove reviewer1@example.com change-id

# 添加CC
ssh -p 29418 admin@localhost gerrit set-reviewers --cc cc1@example.com change-id
```

## 4. 项目管理命令

### 4.1 创建项目

```bash
# 创建项目
ssh -p 29418 admin@localhost gerrit create-project --name your-project

# 创建项目并设置默认分支
ssh -p 29418 admin@localhost gerrit create-project --name your-project --default-branch main

# 创建项目并设置描述
ssh -p 29418 admin@localhost gerrit create-project --name your-project --description "This is a test project"

# 创建项目并设置为私有
ssh -p 29418 admin@localhost gerrit create-project --name your-project --private
```

### 4.2 查看项目

```bash
# 查看所有项目
ssh -p 29418 admin@localhost gerrit ls-projects

# 查看项目配置
ssh -p 29418 admin@localhost gerrit config --get-all project:your-project

# 查看项目分支
ssh -p 29418 admin@localhost gerrit ls-projects --branches your-project
```

### 4.3 配置项目

```bash
# 设置项目描述
ssh -p 29418 admin@localhost gerrit config --set project:your-project description "New description"

# 设置项目默认分支
ssh -p 29418 admin@localhost gerrit config --set project:your-project HEAD refs/heads/main

# 设置项目提交消息模板
ssh -p 29418 admin@localhost gerrit config --set project:your-project commitMessageTemplate "Default commit message"
```

### 4.4 删除项目

```bash
# 删除项目
ssh -p 29418 admin@localhost gerrit delete-project --yes-really-delete your-project
```

## 5. 权限管理命令

### 5.1 查看权限

```bash
# 查看项目权限
ssh -p 29418 admin@localhost gerrit ls-groups --project your-project

# 查看组权限
ssh -p 29418 admin@localhost gerrit ls-members --project your-project group-name
```

### 5.2 管理组

```bash
# 创建组
ssh -p 29418 admin@localhost gerrit create-group --description "Developers group" developers

# 添加成员到组
ssh -p 29418 admin@localhost gerrit set-members --add username developers

# 移除成员从组
ssh -p 29418 admin@localhost gerrit set-members --remove username developers

# 删除组
ssh -p 29418 admin@localhost gerrit delete-group developers
```

### 5.3 设置权限

权限设置通常通过Gerrit Web界面完成：
1. 登录Gerrit Web界面
2. 点击"Projects"菜单，选择"List"
3. 点击要配置的项目
4. 点击"Access"
5. 点击"Edit"按钮修改权限
6. 配置完成后点击"Save Changes"按钮

## 6. Gerrit工作流程

### 6.1 默认工作流程

1. **克隆仓库**：
   ```bash
   git clone ssh://admin@localhost:29418/your-project.git
   cd your-project
   ```

2. **创建分支**：
   ```bash
   git checkout -b feature-branch
   ```

3. **修改文件**：
   ```bash
   # 使用编辑器修改文件
   # ...
   ```

4. **提交修改**：
   ```bash
   git add .
   git commit -m "Add new feature"
   ```

5. **推送到Gerrit**：
   ```bash
   git push origin HEAD:refs/for/master
   ```

6. **代码审查**：
   - 审查者登录Gerrit Web界面
   - 查看变更并提供反馈
   - 给出代码审查评分（如+1、+2、-1、-2）

7. **修改代码**（如果需要）：
   ```bash
   # 修改文件
   # ...
   git add .
   git commit --amend
   git push origin HEAD:refs/for/master
   ```

8. **验证变更**：
   - CI/CD系统自动验证变更
   - 给出验证评分（如+1、-1）

9. **合并变更**：
   - 审查者批准变更（Code-Review+2）
   - 验证通过（Verified+1）
   - 点击"Submit"按钮合并变更

10. **删除分支**：
    ```bash
    git checkout master
    git pull
    git branch -d feature-branch
    ```

### 6.2 主题分支工作流程

主题分支工作流程允许将相关的变更组合在一起进行审查：

1. **创建主题分支**：
   ```bash
   git checkout -b topic-branch
   ```

2. **提交第一个变更**：
   ```bash
   # 修改文件
   # ...
   git add .
   git commit -m "Change 1"
   git push origin HEAD:refs/for/master%topic=my-topic
   ```

3. **提交第二个变更**：
   ```bash
   # 修改文件
   # ...
   git add .
   git commit -m "Change 2"
   git push origin HEAD:refs/for/master%topic=my-topic
   ```

4. **审查主题**：
   - 在Gerrit Web界面中，点击"Topics"菜单
   - 找到并查看整个主题的变更
   - 对每个变更进行审查

### 6.3 提交-合并工作流程

提交-合并工作流程允许变更自动合并，然后再进行审查：

1. **配置项目**：
   - 在Gerrit Web界面中，进入项目的"Access"设置
   - 为"refs/heads/*"设置"Push"权限给开发组
   - 禁用"Code-Review"和"Verified"标签的必填要求

2. **直接推送到分支**：
   ```bash
   git push origin feature-branch:master
   ```

3. **代码审查**：
   - 审查者在Gerrit中查看已合并的变更
   - 如果发现问题，创建新的变更进行修复

## 7. 常用Git命令与Gerrit结合

### 7.1 配置Git用户信息

```bash
# 设置用户名
git config --global user.name "Your Name"

# 设置用户邮箱
git config --global user.email "your.email@example.com"
```

### 7.2 配置Git钩子

为了确保每次提交都包含Change-Id，可以配置Git钩子：

```bash
# 创建commit-msg钩子文件
cat > ~/.git/hooks/commit-msg << 'EOF'
#!/bin/sh
#
# This hook adds a Change-Id line to the commit message if it's not already there.

CHANGE_ID_AFTER="Bug|Issue|Fixes|Closes"
MSG="$(cat "$1")"

# Check if the message already contains a Change-Id
if grep -q "^Change-Id:" "$1"; then
    exit 0
fi

# Generate a Change-Id
CHANGE_ID=$(uuidgen | tr -d '-' | cut -c1-20)

# Add the Change-Id to the message
if grep -q "^$CHANGE_ID_AFTER:" "$1"; then
    sed -i "/^$CHANGE_ID_AFTER:/a\nChange-Id: I$CHANGE_ID" "$1"
else
    echo "\nChange-Id: I$CHANGE_ID" >> "$1"
fi
EOF

# 使钩子文件可执行
chmod +x ~/.git/hooks/commit-msg
```

### 7.3 同步Gerrit变更

```bash
# 同步Gerrit的变更
ssh -p 29418 admin@localhost gerrit replicate

# 同步特定项目的变更
ssh -p 29418 admin@localhost gerrit replicate --project your-project
```

## 8. 总结

本章节介绍了Gerrit的常用命令和工作流程，包括：

- Gerrit命令行工具的基本使用
- 变更的创建、提交和管理
- 代码审查和评论
- 项目和权限管理
- 多种工作流程示例

掌握这些命令和工作流程将帮助您高效地使用Gerrit进行代码审查和团队协作。在实际工作中，您可以根据项目需求和团队习惯选择合适的工作流程。

下一章：[GerritGit高级用法](05_GerritGit高级用法.md)