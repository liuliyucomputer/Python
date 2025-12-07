# Windows系统Gerrit保姆级使用教程

## 1. 什么是Gerrit？

Gerrit是一个基于Web的代码审查工具，它集成了Git版本控制系统，提供了强大的代码审查、访问控制和工作流程管理功能。Gerrit允许团队成员在代码合并到主分支之前进行审查，确保代码质量和一致性。

### 1.1 Gerrit的工作原理

Gerrit的核心工作原理是在Git之上添加了一层代码审查机制。当开发者提交代码时，代码不会直接进入主分支，而是先进入Gerrit的审查队列。其他团队成员可以对代码进行审查，提供反馈和建议。只有通过审查的代码才能被合并到主分支。

### 1.2 Gerrit的核心概念

- **变更(Change)**：Gerrit中代码审查的基本单位，对应一个待审查的代码修改
- **提交(Commit)**：与Git中的提交概念类似，但Gerrit会为每个提交生成一个唯一的Change ID
- **审查者(Reviewer)**：参与代码审查的人员，负责检查代码质量、提供反馈和批准变更
- **所有者(Owner)**：创建变更的人员，负责根据审查者的反馈修改代码
- **项目(Project)**：Gerrit中的代码库，对应Git仓库
- **分支(Branch)**：与Git中的分支概念相同
- **引用(Reference)**：Git中的概念，在Gerrit中用于表示分支、标签等
- **工作流程(Workflow)**：定义了代码从提交到合并的过程
- **标签(Label)**：用于表示审查者对变更的评价，如"Code-Review"、"Verified"

## 2. Windows系统Git安装与配置

在使用Gerrit之前，我们需要先安装和配置Git。

### 2.1 Git下载

1. 访问Git官方下载页面：[https://git-scm.com/download/win](https://git-scm.com/download/win)
2. 根据你的Windows系统位数（32位或64位）下载对应的安装包

### 2.2 Git安装

1. 双击下载的安装包，开始安装
2. 选择安装目录（建议使用默认目录）
3. 在"Select Components"页面，建议勾选以下组件：
   - Git GUI Here
   - Git Bash Here
   - Git LFS (Large File Storage)
4. 在"Choosing the default editor used by Git"页面，选择你熟悉的编辑器（如Notepad++或VS Code）
5. 在"Adjusting the name of the initial branch in new repositories"页面，保持默认设置（master）
6. 在"Configuring the line ending conversions"页面，选择"Checkout Windows-style, commit Unix-style line endings"（这是跨平台开发的最佳选择）
7. 在"Configuring the terminal emulator to use with Git Bash"页面，选择"Use Windows' default console window"
8. 其余选项保持默认，点击"Install"完成安装

### 2.3 Git配置

安装完成后，我们需要配置Git的基本信息：

1. 打开Git Bash（在任意文件夹右键选择"Git Bash Here"）
2. 配置用户名和邮箱：

```bash
git config --global user.name "你的姓名"
git config --global user.email "你的邮箱"
```

3. 配置Git使用的编辑器：

```bash
git config --global core.editor "notepad++ -multiInst -nosession"
# 或者如果你使用VS Code：
git config --global core.editor "code --wait"
```

4. 配置自动换行处理：

```bash
git config --global core.autocrlf true
git config --global core.safecrlf warn
```

5. 查看配置信息：

```bash
git config --list
```

## 3. Gerrit客户端配置（SSH密钥设置）

Gerrit通常使用SSH协议进行认证和数据传输，因此我们需要在Windows系统上配置SSH密钥。

### 3.1 生成SSH密钥对

1. 打开Git Bash
2. 输入以下命令生成SSH密钥对：

```bash
ssh-keygen -t rsa -b 4096 -C "你的邮箱"
```

3. 按Enter键使用默认保存路径（`C:\Users\你的用户名\.ssh\id_rsa`）
4. 输入密码（可选，用于保护SSH私钥）
5. 再次输入密码确认

### 3.2 查看和复制SSH公钥

1. 生成密钥后，使用以下命令查看公钥内容：

```bash
cat ~/.ssh/id_rsa.pub
```

2. 复制公钥内容（从`ssh-rsa`开始到你的邮箱结束）

### 3.3 在Gerrit服务器上添加SSH公钥

1. 打开Gerrit Web界面（由你的团队管理员提供URL）
2. 登录你的Gerrit账户
3. 点击右上角的用户名，选择"Settings"
4. 在左侧菜单中选择"SSH Public Keys"
5. 点击"Add Key..."按钮
6. 将复制的SSH公钥粘贴到文本框中
7. 点击"Add"按钮保存

### 3.4 测试SSH连接

1. 在Git Bash中输入以下命令测试与Gerrit服务器的SSH连接：

```bash
ssh -p 29418 你的用户名@gerrit服务器地址
```

2. 如果是第一次连接，会提示"The authenticity of host '[gerrit服务器地址]:29418 ([IP地址]:29418)' can't be established. RSA key fingerprint is SHA256:..."，输入"yes"并按Enter
3. 如果设置了SSH密钥密码，会提示输入密码
4. 如果连接成功，会看到类似"  ****    Welcome to Gerrit Code Review    ****"的欢迎信息

## 4. Gerrit基本操作

### 4.1 克隆Gerrit仓库

1. 打开Gerrit Web界面，找到你要克隆的项目
2. 点击项目名称进入项目页面
3. 点击右上角的"Clone"按钮
4. 选择"SSH"选项，复制克隆命令
5. 打开Git Bash，进入你要存放项目的目录
6. 粘贴克隆命令并执行：

```bash
git clone ssh://你的用户名@gerrit服务器地址:29418/项目名称.git
```

### 4.2 创建分支

1. 进入克隆的项目目录：

```bash
cd 项目名称
```

2. 创建并切换到新分支：

```bash
git checkout -b 新分支名称
```

### 4.3 修改代码

使用你熟悉的编辑器修改代码文件

### 4.4 提交代码

1. 查看修改的文件：

```bash
git status
```

2. 将修改的文件添加到暂存区：

```bash
git add 文件名
# 或添加所有修改的文件
git add .
```

3. 提交修改：

```bash
git commit -m "提交信息"
```

4. 重要提示：Gerrit需要在提交信息中包含Change ID。如果你的项目配置了Gerrit提交钩子，Change ID会自动生成。如果没有，你需要手动添加或使用Gerrit的命令生成。

## 5. Gerrit代码审查流程

### 5.1 推送变更到Gerrit

1. 将本地提交推送到Gerrit的特殊引用：

```bash
git push origin HEAD:refs/for/目标分支名称
```

2. 例如，推送到master分支：

```bash
git push origin HEAD:refs/for/master
```

3. 推送成功后，会在Git Bash中看到类似"remote: ... https://gerrit服务器地址/变更ID"的信息，复制这个URL

### 5.2 查看和管理变更

1. 打开复制的URL，进入变更详情页面
2. 你可以看到变更的文件修改、提交信息等
3. 点击"Add Reviewer"按钮添加审查者
4. 审查者会收到邮件通知

### 5.3 代码审查

1. 审查者登录Gerrit Web界面，查看分配给自己的变更
2. 点击变更ID进入变更详情页面
3. 点击文件名称查看具体的代码修改
4. 可以在代码行旁边添加评论
5. 审查完成后，点击"Review"按钮提供反馈：
   - Code-Review：+1（同意）、+2（强烈同意）、-1（需要修改）、-2（强烈反对）
   - Verified：+1（验证通过）、-1（验证失败）

### 5.4 根据审查反馈修改代码

1. 如果审查者要求修改代码，在本地分支中进行修改
2. 添加修改的文件到暂存区：

```bash
git add .
```

3. 使用amend命令修改上次提交（保持同一个Change ID）：

```bash
git commit --amend
```

4. 再次推送到Gerrit：

```bash
git push origin HEAD:refs/for/目标分支名称
```

### 5.5 合并变更

1. 当变更获得足够的批准（通常是Code-Review+2和Verified+1），可以合并变更
2. 在变更详情页面，点击"Submit"按钮
3. 选择合并策略（通常使用默认的"Merge If Necessary"）
4. 点击"Submit"按钮完成合并

## 6. Gerrit高级功能

### 6.1 解决合并冲突

如果你的变更与目标分支有冲突，Gerrit会提示"Merge Conflict"。解决冲突的步骤：

1. 拉取目标分支的最新代码：

```bash
git fetch origin 目标分支名称
```

2. 将你的变更与目标分支合并：

```bash
git merge origin/目标分支名称
```

3. 使用编辑器解决冲突（冲突文件中会有类似`<<<<<<< HEAD`、`=======`、`>>>>>>> origin/目标分支名称`的标记）
4. 解决冲突后，添加修改的文件到暂存区：

```bash
git add 冲突文件名称
```

5. 提交合并结果：

```bash
git commit
```

6. 推送到Gerrit：

```bash
git push origin HEAD:refs/for/目标分支名称
```

### 6.2 查看变更历史

1. 在Gerrit Web界面，点击"Changes"菜单
2. 可以使用过滤条件查看特定状态的变更：
   - Open：打开的变更
   - Merged：已合并的变更
   - Abandoned：已放弃的变更

### 6.3 放弃变更

如果你的变更不再需要，可以放弃它：

1. 进入变更详情页面
2. 点击"Abandon"按钮
3. 输入放弃原因（可选）
4. 点击"Abandon Change"按钮

### 6.4 恢复已放弃的变更

1. 查看已放弃的变更（使用"Abandoned"过滤条件）
2. 进入变更详情页面
3. 点击"Restore"按钮

## 7. Gerrit最佳实践

### 7.1 提交信息规范

- 提交信息要清晰、简洁，说明修改的目的
- 第一行是简短的标题（不超过50个字符）
- 第二行是空行
- 第三行开始是详细的描述（每行不超过72个字符）
- 包含Change ID（由Gerrit自动生成或手动添加）

### 7.2 代码审查规范

- 每次提交的代码量不宜过大（建议不超过200行）
- 代码要符合项目的编码规范
- 审查者要及时提供反馈，给出具体的改进建议
- 开发者要认真对待审查反馈，及时修改代码

### 7.3 分支管理规范

- 主分支（master）保持稳定，只包含已通过审查的代码
- 功能开发在独立的分支中进行
- 分支名称要清晰，说明分支的用途（如feature/新功能名称、bugfix/问题编号）

### 7.4 工作流程建议

1. 每天开始工作前，拉取目标分支的最新代码
2. 开发新功能或修复bug时，创建独立的分支
3. 频繁提交代码，每次提交只包含一个逻辑上的修改
4. 及时推送到Gerrit进行审查
5. 根据审查反馈及时修改代码
6. 变更合并后，删除本地的功能分支

## 8. 常见问题与解决方案

### 8.1 SSH连接失败

**问题**：`ssh: connect to host gerrit服务器地址 port 29418: Connection timed out`

**解决方案**：
1. 检查Gerrit服务器地址和端口是否正确
2. 检查网络连接是否正常
3. 检查防火墙是否阻止了SSH连接

### 8.2 推送失败，提示缺少Change ID

**问题**：`remote: ERROR: commit xxxxxxxx: missing Change-Id in message footer`

**解决方案**：
1. 安装Gerrit提交钩子：

```bash
git clone ssh://你的用户名@gerrit服务器地址:29418/tools/hooks.git
hooks/commit-msg .git/hooks/
```

2. 使用amend命令重新提交，添加Change ID：

```bash
git commit --amend
# 在提交信息末尾添加：Change-Id: Ixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 其中xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx是随机生成的字符串
```

### 8.3 变更无法提交

**问题**：点击"Submit"按钮后，提示"Submit failed: Not enough approvals"

**解决方案**：
1. 检查变更是否获得了足够的批准（通常需要Code-Review+2和Verified+1）
2. 联系项目管理员或审查者，请求批准你的变更

### 8.4 忘记SSH密钥密码

**解决方案**：
1. 生成新的SSH密钥对（参考3.1节）
2. 在Gerrit服务器上添加新的公钥（参考3.3节）
3. 删除旧的SSH密钥（可选）

## 8. Gerrit命令行工具

Gerrit提供了命令行工具`gerrit`，可以用于管理变更、项目、用户等。以下是常用的Gerrit命令：

### 8.1 安装Gerrit命令行工具

1. 下载Gerrit命令行工具：

```bash
# 克隆Gerrit工具仓库
git clone ssh://你的用户名@gerrit服务器地址:29418/tools/gerrit.git
```

2. 将Gerrit命令添加到系统PATH：

```bash
# 将以下行添加到你的~/.bashrc或~/.bash_profile文件中
export PATH=$PATH:/path/to/gerrit/bin
```

3. 重新加载配置：

```bash
source ~/.bashrc
```

### 8.2 常用Gerrit命令

#### 8.2.1 变更管理

```bash
# 列出所有变更
gerrit query --format=JSON status:open

# 列出特定项目的变更
gerrit query --format=JSON project:项目名称 status:open

# 列出特定用户的变更
gerrit query --format=JSON owner:用户名 status:open

# 查看变更详情
gerrit query --format=JSON change:变更ID

# 放弃变更
gerrit review --abandon 变更ID,补丁集编号

# 恢复变更
gerrit review --restore 变更ID,补丁集编号

# 提交变更
gerrit review --submit 变更ID,补丁集编号
```

#### 8.2.2 代码审查

```bash
# 给变更打分
gerrit review --code-review +2 --verified +1 变更ID,补丁集编号

# 添加评论
gerrit review --message "评论内容" 变更ID,补丁集编号

# 添加审查者
gerrit set-reviewers --add 审查者用户名 变更ID

# 删除审查者
gerrit set-reviewers --delete 审查者用户名 变更ID
```

#### 8.2.3 项目管理

```bash
# 列出所有项目
gerrit ls-projects

# 创建项目
gerrit create-project 新项目名称

# 删除项目
gerrit delete-project 项目名称

# 配置项目访问权限
gerrit set-project-parent 项目名称 --parent 父项目名称
```

#### 8.2.4 用户管理

```bash
# 创建用户
gerrit create-account 用户名 --full-name "用户全名" --email 邮箱地址

# 删除用户
gerrit delete-account 用户名

# 列出用户组
gerrit ls-groups

# 创建用户组
gerrit create-group 组名

# 添加用户到组
gerrit add-member 组名 用户名
```

## 9. Gerrit高级功能补充

### 9.1 补丁集管理

```bash
# 查看变更的所有补丁集
git fetch origin refs/changes/xx/yyyy/0

# 切换到特定补丁集
git checkout FETCH_HEAD

# 比较两个补丁集
git diff refs/changes/xx/yyyy/1 refs/changes/xx/yyyy/2
```

### 9.2 标签管理

```bash
# 列出所有标签
git tag

# 创建标签
git tag -a 标签名称 -m "标签描述"

# 推送标签到Gerrit
git push origin 标签名称

# 删除标签
git tag -d 标签名称
git push origin :refs/tags/标签名称
```

### 9.3 钩子(Hooks)使用

Gerrit支持多种钩子，可以在特定事件发生时自动执行脚本：

1. **提交钩子(commit-msg)**：在提交时自动添加Change ID
2. **引用钩子(ref-update)**：在引用更新时执行
3. **变更钩子(change-merged)**：在变更合并时执行

安装提交钩子：

```bash
# 方法1：从Gerrit服务器克隆钩子
git clone ssh://你的用户名@gerrit服务器地址:29418/tools/hooks.git
hooks/commit-msg .git/hooks/

# 方法2：手动创建提交钩子
cat > .git/hooks/commit-msg << 'EOF'
#!/bin/sh
# 自动添加Change ID的脚本
EOF
chmod +x .git/hooks/commit-msg
```

### 9.4 合并策略

Gerrit支持多种合并策略：

1. **Fast-forward Only**：只能快进合并，要求变更基于目标分支的最新提交
2. **Merge If Necessary**：如果不能快进合并，则创建合并提交
3. **Rebase If Necessary**：如果不能快进合并，则先变基再合并
4. **Cherry-pick**：将变更作为新的提交应用到目标分支

在Gerrit Web界面提交变更时，可以选择合并策略。

## 10. 总结

通过本教程，你应该已经掌握了在Windows系统上使用Gerrit的基本操作和高级功能，包括：

1. Git在Windows上的安装和配置
2. Gerrit客户端的SSH密钥设置
3. Gerrit基本操作：克隆仓库、创建分支、提交代码
4. Gerrit代码审查流程：推送、审核、修改、合并
5. Gerrit高级功能：冲突解决、变更管理
6. Gerrit最佳实践和常见问题解决方案

要在任何Windows电脑上熟练使用Gerrit，你需要：
1. 安装Git并配置基本信息
2. 生成SSH密钥对并添加到Gerrit服务器
3. 熟悉Gerrit的Web界面操作
4. 掌握Gerrit命令行工具的使用
5. 遵循项目的编码规范和工作流程
6. 了解Gerrit的高级功能和最佳实践

本教程涵盖了Gerrit的所有常用指令和功能，包括：
- Git基础操作和配置
- Gerrit SSH密钥设置
- 变更的创建、推送和管理
- 代码审查流程
- Gerrit命令行工具的安装和使用
- 变更管理、代码审查、项目管理和用户管理的命令
- 补丁集管理、标签管理、钩子使用和合并策略
- 最佳实践和常见问题解决方案

通过不断实践，你将能够在任何Windows电脑上高效地使用Gerrit进行代码审查和团队协作，成为Gerrit使用专家。

---

**作者**：控制轨道
**版本**：1.0
**更新日期**：2025年12月
