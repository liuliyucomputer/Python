# Gerrit基础概念

## 1. Gerrit简介

### 1.1 Gerrit的定义
Gerrit是一个基于Web的代码审查工具，它集成了Git版本控制系统，提供了强大的代码审查、访问控制和工作流程管理功能。Gerrit允许团队成员在代码合并到主分支之前进行审查，确保代码质量和一致性。

### 1.2 Gerrit的历史
- 2006年：Gerrit由Google开发，最初用于Android项目的代码审查
- 2009年：Gerrit 1.0正式发布
- 2012年：Gerrit 2.0发布，引入了基于Git的存储机制
- 2018年：Gerrit 2.15发布，支持Git LFS和增强的UI
- 2020年：Gerrit 3.0发布，完全重写了UI组件

### 1.3 Gerrit的核心特点
- **代码审查**：支持多人协作审查代码，确保代码质量
- **工作流程控制**：可定制的工作流程，支持多种代码审查模式
- **访问控制**：细粒度的权限管理，控制用户对代码库的访问
- **Git集成**：无缝集成Git版本控制系统
- **Web界面**：直观的Web界面，支持代码浏览、审查和管理
- **插件系统**：可扩展的插件架构，支持自定义功能
- **REST API**：提供REST API，支持自动化集成

### 1.4 Gerrit与其他代码审查工具的比较

| 特性 | Gerrit | GitHub | GitLab | Review Board |
|------|--------|--------|--------|--------------|
| 集成Git | ✅ | ✅ | ✅ | ❌ |
| 代码审查 | ✅ | ✅ | ✅ | ✅ |
| 工作流程控制 | ✅ | ⚠️ | ✅ | ⚠️ |
| 访问控制 | ✅ | ⚠️ | ✅ | ⚠️ |
| 插件系统 | ✅ | ⚠️ | ✅ | ⚠️ |
| 自托管 | ✅ | ❌ | ✅ | ✅ |
| 免费开源 | ✅ | ⚠️ | ✅ | ✅ |
| 企业支持 | ✅ | ✅ | ✅ | ✅ |

## 2. Gerrit核心概念

### 2.1 变更(Change)
变更是Gerrit中代码审查的基本单位，对应一个待审查的代码修改。一个变更通常包含：
- 提交信息
- 文件修改内容
- 审查历史
- 评论和建议
- 状态信息（新建、已审查、已合并、已放弃等）

### 2.2 提交(Commit)
与Git中的提交概念类似，但Gerrit会为每个提交生成一个唯一的变更ID(Change ID)，用于跟踪和管理变更。

### 2.3 审查者(Reviewer)
审查者是参与代码审查的人员，负责检查代码质量、提供反馈和批准变更。

### 2.4 所有者(Owner)
变更多所有者是创建变更的人员，负责根据审查者的反馈修改代码。

### 2.5 项目(Project)
项目是Gerrit中的代码库，对应Git仓库。每个项目可以有独立的访问控制和工作流程配置。

### 2.6 分支(Branch)
与Git中的分支概念相同，Gerrit允许在不同分支上进行代码审查。

### 2.7 引用(Reference)
引用是Git中的概念，在Gerrit中用于表示分支、标签等。Gerrit使用引用控制来管理代码的提交和合并。

### 2.8 工作流程(Workflow)
工作流程定义了代码从提交到合并的过程，包括审查规则、批准条件和合并策略。

### 2.9 标签(Label)
标签用于表示审查者对变更的评价，如"Code-Review"（代码审查）、"Verified"（验证）等。每个标签可以有不同的评分（如+1、+2、-1、-2）。

### 2.10 合并策略(Merge Strategy)
合并策略定义了如何将变更合并到目标分支，如Fast-forward、Recursive等。

## 3. Gerrit架构

### 3.1 整体架构

Gerrit采用客户端-服务器架构，主要包含以下组件：

- **Gerrit服务器**：核心组件，处理HTTP请求、Git操作和代码审查逻辑
- **Git仓库**：存储代码和版本历史
- **数据库**：存储元数据，如用户信息、项目配置、变更状态等
- **认证系统**：处理用户认证，支持LDAP、OAuth等多种认证方式
- **Web界面**：提供用户交互界面
- **REST API**：提供程序化访问接口

### 3.2 技术栈

Gerrit主要使用以下技术开发：

- **Java**：服务器端开发语言
- **Git**：版本控制系统
- **Jetty**：嵌入式Web服务器
- **PostgreSQL/MySQL/H2**：数据库支持
- **Google Web Toolkit(GWT)**：Web界面开发框架（Gerrit 3.0之前）
- **Polymer/React**：Web界面开发框架（Gerrit 3.0及以后）

### 3.3 数据存储

Gerrit使用两种存储机制：

1. **Git仓库**：存储代码和版本历史
2. **数据库**：存储元数据，包括：
   - 用户信息和权限
   - 项目配置
   - 变更状态和审查历史
   - 评论和建议
   - 工作流程配置

## 4. Gerrit工作原理

### 4.1 变更提交流程

Gerrit的核心工作流程是变更提交和审查流程：

1. **开发者提交变更**：开发者使用Git命令将变更推送到Gerrit的特殊引用(Refs/for/branch-name)
2. **Gerrit创建变更**：Gerrit检测到推送，创建一个新的变更记录
3. **分配审查者**：系统自动或手动分配审查者
4. **代码审查**：审查者检查代码，提供反馈和评分
5. **修改代码**：开发者根据审查反馈修改代码，再次推送到Gerrit
6. **验证变更**：自动化测试或CI系统验证变更
7. **批准变更**：审查者批准变更（如Code-Review+2、Verified+1）
8. **合并变更**：Gerrit将变更合并到目标分支
9. **通知相关人员**：Gerrit发送通知给相关人员

### 4.2 Git引用控制

Gerrit使用Git的引用控制机制来管理代码提交：

- **Refs/for/branch-name**：用于提交待审查的变更
- **Refs/changes/xx/yyyy/zz**：用于存储变更的不同版本
- **Refs/heads/branch-name**：目标分支，只有通过审查的变更才能合并到这里

### 4.3 审查工作流程

Gerrit支持多种审查工作流程，包括：

#### 4.3.1 默认工作流程

1. 开发者提交变更到Refs/for/branch-name
2. 审查者进行代码审查
3. 开发者根据反馈修改代码
4. 审查者批准变更
5. Gerrit合并变更到目标分支

#### 4.3.2 提交-合并工作流程

1. 开发者提交变更到Refs/for/branch-name
2. 变更自动合并到目标分支
3. 审查者进行代码审查
4. 如发现问题，开发者创建新的变更修复

#### 4.3.3 分支工作流程

1. 开发者创建功能分支
2. 在功能分支上开发和提交代码
3. 将功能分支推送到Gerrit进行审查
4. 审查通过后合并到主分支

## 5. Gerrit安装与配置

### 5.1 系统要求

- **操作系统**：Linux、Windows、macOS
- **Java版本**：Java 11或更高版本
- **内存**：至少2GB RAM，建议4GB或更多
- **磁盘空间**：根据代码库大小而定，建议至少10GB
- **数据库**：PostgreSQL、MySQL或H2（仅用于测试）

### 5.2 安装步骤

#### 5.2.1 下载Gerrit

```bash
# 下载最新版本的Gerrit
wget https://gerrit-releases.storage.googleapis.com/gerrit-3.5.1.war
```

#### 5.2.2 初始化Gerrit

```bash
# 创建Gerrit安装目录
mkdir -p /opt/gerrit
cd /opt/gerrit

# 初始化Gerrit
gjava -jar gerrit-3.5.1.war init --batch -d gerrit-site \
  --git-dir=/opt/gerrit/git \
  --database-type=h2 \
  --reviewdb-password=gerrit \
  --index-type=lucene \
  --smtp-server=smtp.gmail.com \
  --smtp-port=587 \
  --smtp-user=your.email@gmail.com \
  --smtp-pass=your-password \
  --smtp-ssl=true \
  --user=admin \
  --password=admin \
  --enable-attention-set \
  --enable-register-new-emails \
  --install-plugin=commit-message-length-validator \
  --install-plugin=download-commands \
  --install-plugin=reviewnotes \
  --install-plugin=singleusergroup \
  --install-plugin=webhooks
```

#### 5.2.3 启动Gerrit

```bash
# 启动Gerrit服务
cd /opt/gerrit/gerrit-site
bin/gerrit.sh start
```

#### 5.2.4 访问Gerrit

在浏览器中访问：http://localhost:8080

### 5.3 基本配置

#### 5.3.1 配置文件

Gerrit的主要配置文件位于`gerrit-site/etc/gerrit.config`，包含以下主要部分：

```ini
[gerrit]
  basePath = git
  serverId = gerrit-server-id
  canonicalWebUrl = http://localhost:8080/
[database]
  type = h2
  database = db/ReviewDB
[index]
  type = lucene
  directory = index
[auth]
  type = LDAP
[ldap]
  server = ldap://ldap.example.com
  username = cn=admin,dc=example,dc=com
  password = ldap-password
  accountBase = ou=people,dc=example,dc=com
  groupBase = ou=groups,dc=example,dc=com
[sendemail]
  smtpServer = smtp.gmail.com
  smtpServerPort = 587
  smtpUser = your.email@gmail.com
  smtpPass = your-password
  smtpEncryption = tls
[container]
  user = gerrit
  javaHome = /usr/lib/jvm/java-11-openjdk-amd64
[sshd]
  listenAddress = *:29418
[httpd]
  listenUrl = http://*:8080/
[cache]
  directory = cache
```

#### 5.3.2 配置认证方式

Gerrit支持多种认证方式，包括：

##### 5.3.2.1 LDAP认证

```ini
[auth]
  type = LDAP
[ldap]
  server = ldap://ldap.example.com
  username = cn=admin,dc=example,dc=com
  password = ldap-password
  accountBase = ou=people,dc=example,dc=com
  groupBase = ou=groups,dc=example,dc=com
  accountPattern = (&(objectClass=inetOrgPerson)(uid=${username}))
  groupPattern = (&(objectClass=groupOfUniqueNames)(uniqueMember=${dn}))
```

##### 5.3.2.2 HTTP认证

```ini
[auth]
  type = HTTP
```

##### 5.3.2.3 OpenID认证

```ini
[auth]
  type = OPENID
```

#### 5.3.3 配置SMTP邮件服务

```ini
[sendemail]
  smtpServer = smtp.gmail.com
  smtpServerPort = 587
  smtpUser = your.email@gmail.com
  smtpPass = your-password
  smtpEncryption = tls
  from = Gerrit Code Review <your.email@gmail.com>
```

#### 5.3.4 配置Git服务器

```ini
[sshd]
  listenAddress = *:29418
  maxConnections = 64
[git]
  uploadPack = true
  receivePack = true
```

## 6. Gerrit基本使用

### 6.1 克隆Gerrit仓库

```bash
# 克隆Gerrit仓库
git clone ssh://admin@localhost:29418/your-project.git
```

### 6.2 提交变更到Gerrit

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
```

### 6.3 查看和管理变更

1. 登录Gerrit Web界面
2. 点击"Changes"菜单查看所有变更
3. 点击变更ID查看变更详情
4. 点击"Review"按钮进行代码审查
5. 提供评论和评分
6. 点击"Submit"按钮合并变更

## 7. 总结

本章节介绍了Gerrit的基础概念、架构、工作原理和安装配置：

- Gerrit是一个强大的代码审查工具，集成了Git版本控制系统
- Gerrit的核心概念包括变更、提交、审查者、项目等
- Gerrit使用Git的引用控制机制来管理代码提交
- Gerrit支持多种审查工作流程，可根据项目需求定制
- Gerrit的安装和配置相对简单，支持多种认证方式和数据库

掌握这些基础概念将帮助您更好地理解和使用Gerrit进行代码审查。在接下来的章节中，我们将深入学习Gerrit的常用命令和高级功能。

下一章：[Gerrit常用命令](04_Gerrit常用命令.md)