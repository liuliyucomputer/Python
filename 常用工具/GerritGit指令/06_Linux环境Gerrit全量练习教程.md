# Linux环境下Gerrit全量练习教程

## 1. 环境准备

### 1.1 系统要求
- **操作系统**：推荐使用 Ubuntu 20.04 LTS 或 CentOS 7/8
- **内存**：至少 4GB RAM（推荐 8GB 以上）
- **磁盘空间**：至少 20GB 可用空间
- **网络**：可以访问互联网用于下载依赖

### 1.2 依赖安装

#### Ubuntu 系统
```bash
# 更新系统包列表
sudo apt update

# 安装Java（Gerrit运行需要Java环境）
sudo apt install -y openjdk-11-jdk

# 安装Git（版本控制工具）
sudo apt install -y git

# 安装Apache2（可选，用于反向代理）
sudo apt install -y apache2

# 安装PostgreSQL（可选，用于Gerrit数据库）
sudo apt install -y postgresql postgresql-contrib
```

#### CentOS 系统
```bash
# 更新系统包列表
sudo yum update -y

# 安装Java
sudo yum install -y java-11-openjdk java-11-openjdk-devel

# 安装Git
sudo yum install -y git

# 安装Apache2
sudo yum install -y httpd

# 安装PostgreSQL
sudo yum install -y postgresql-server postgresql-contrib
```

### 1.3 验证安装
```bash
# 验证Java版本
java -version

# 验证Git版本
git --version
```

## 2. Gerrit服务器安装与配置

### 2.1 下载Gerrit
```bash
# 创建Gerrit安装目录
sudo mkdir -p /opt/gerrit
cd /opt/gerrit

# 下载Gerrit最新版本（访问https://www.gerritcodereview.com/download.html获取最新版本）
sudo wget https://gerrit-releases.storage.googleapis.com/gerrit-3.6.3.war
```

### 2.2 初始化Gerrit数据库（可选）
```bash
# 启动PostgreSQL服务
sudo systemctl start postgresql

# 创建Gerrit数据库和用户
sudo -u postgres psql -c "CREATE USER gerrit WITH PASSWORD 'gerritpassword';"
sudo -u postgres psql -c "CREATE DATABASE reviewdb OWNER gerrit;"
```

### 2.3 安装Gerrit
```bash
# 创建Gerrit用户
sudo useradd -m -s /bin/bash gerrit

# 切换到Gerrit用户
sudo su - gerrit

# 创建Gerrit站点目录
mkdir review_site

# 初始化Gerrit（使用H2数据库，适合练习环境）
java -jar /opt/gerrit/gerrit-3.6.3.war init -d review_site
```

### 2.4 Gerrit初始化配置（交互式）
初始化过程中需要回答以下问题（保姆级提示）：

```
*** Gerrit Code Review 3.6.3
***

Create '/home/gerrit/review_site' [Y/n]? Y

*** Git Repositories
***

Location of Git repositories   [git]: 直接回车

*** SQL Database
***

Database server type           [h2]: 直接回车（或输入postgresql使用PostgreSQL）

*** Index
***

Type                           [lucene]: 直接回车

*** User Authentication
***

Authentication method          [OPENID]: 输入http（使用HTTP身份验证）
Get username from custom HTTP header [y/N]? N
SSO logout URL                 : 直接回车

*** Review Labels
***

Install Verified label         [y/N]? Y（安装验证标签）

*** Email Delivery
***

SMTP server hostname           [localhost]: 直接回车
SMTP server port               [(default)]: 直接回车
SMTP encryption                [NONE]: 直接回车
SMTP username                  : 直接回车

*** Container Process
***

Run as                         [gerrit]: 直接回车
Java runtime                   [/usr/lib/jvm/java-11-openjdk-amd64]: 直接回车
Copy gerrit-3.6.3.war to review_site/bin/gerrit.war [Y/n]? Y
Copying gerrit-3.6.3.war to review_site/bin/gerrit.war

*** SSH Daemon
***

Listen on address              [*]: 直接回车
Listen on port                 [29418]: 直接回车

*** HTTP Daemon
***

Behind reverse proxy           [y/N]? N
Use SSL (https://)             [y/N]? N
Listen on address              [*]: 直接回车
Listen on port                 [8080]: 直接回车
Canonical URL                  [http://localhost:8080/]: 直接回车（或输入服务器IP地址）

*** Plugins
***

Install plugin download-commands version v3.6.3 [y/N]? Y
Install plugin hooks version v3.6.3 [y/N]? Y
Install plugin replication version v3.6.3 [y/N]? Y
Install plugin reviewnotes version v3.6.3 [y/N]? Y
Install plugin singleusergroup version v3.6.3 [y/N]? Y
Install plugin webhooks version v3.6.3 [y/N]? Y

Initialized /home/gerrit/review_site
```

### 2.5 启动Gerrit服务
```bash
# 切换到Gerrit用户
sudo su - gerrit

# 启动Gerrit
cd review_site
bin/gerrit.sh start
```

### 2.6 验证Gerrit服务
```bash
# 检查Gerrit服务状态
bin/gerrit.sh status

# 查看Gerrit日志
tail -f logs/error_log
```

## 3. Gerrit客户端配置

### 3.1 访问Gerrit Web界面
打开浏览器，访问：`http://服务器IP:8080/`

### 3.2 第一次登录
1. 第一次访问会提示设置管理员账户
2. 输入用户名（如：admin）和密码
3. 点击"Create Account"

### 3.3 生成SSH密钥
```bash
# 生成SSH密钥对（按提示操作，默认路径即可）
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# 查看公钥内容
cat ~/.ssh/id_rsa.pub
```

### 3.4 添加SSH密钥到Gerrit
1. 登录Gerrit Web界面
2. 点击右上角头像 → Settings
3. 点击左侧菜单：SSH Public Keys
4. 复制`~/.ssh/id_rsa.pub`的内容到文本框
5. 点击"Add New SSH Key"

### 3.5 配置Git用户信息
```bash
# 配置全局用户名
git config --global user.name "Your Name"

# 配置全局邮箱
git config --global user.email "your_email@example.com"

# 配置Gerrit推送URL
git config --global url.ssh://admin@服务器IP:29418/.pushInsteadOf https://服务器IP:8080/
```

## 4. Gerrit界面介绍

### 4.1 主界面
- **Projects**：查看所有项目
- **Changes**：查看所有变更请求
- **Groups**：用户组管理
- **People**：用户管理
- **Plugins**：插件管理
- **Settings**：个人设置

### 4.2 项目页面
- **Branches**：查看分支
- **Tags**：查看标签
- **Commits**：查看提交历史
- **Browse**：浏览仓库内容

### 4.3 变更页面
- **Files**：查看变更的文件
- **Comments**：查看评论
- **History**：查看变更历史
- **Related Changes**：查看相关变更

## 5. Gerrit指令全量练习

### 5.1 项目操作

#### 创建项目
```bash
# 创建项目命令（需要管理员权限）
gerrit create-project --name my-project --description "My first project"

# 带分支创建项目
gerrit create-project --name my-project-with-branches --description "Project with branches" --branch master --branch develop
```

#### 克隆项目
```bash
# 克隆项目
git clone ssh://admin@服务器IP:29418/my-project

# 进入项目目录
cd my-project

# 添加Gerrit远程（如果克隆时没有自动添加）
git remote add gerrit ssh://admin@服务器IP:29418/my-project
```

### 5.2 变更操作

#### 创建变更
```bash
# 创建并切换到新分支
git checkout -b feature/new-feature

# 创建测试文件
echo "Hello Gerrit!" > hello.txt

# 添加文件到暂存区
git add hello.txt

# 提交变更
git commit -m "Add hello.txt file"

# 推送到Gerrit（注意：必须推送到refs/for/分支名）
git push gerrit HEAD:refs/for/master
```

#### 查看变更
```bash
# 查看所有变更
gerrit query --format=JSON status:open

# 查看特定项目的变更
gerrit query --format=JSON project:my-project status:open

# 查看特定用户的变更
gerrit query --format=JSON owner:self status:open
```

#### 审查变更
```bash
# 查看变更详情
gerrit query --format=JSON change:1

# 批准变更
gerrit review --code-review +2 --verified +1 1,1

# 提交变更（合并到目标分支）
gerrit review --submit 1,1
```

#### 回复变更
```bash
# 添加评论
gerrit review --message "Good work!" 1,1

# 添加特定文件的评论
gerrit review --message "This line needs improvement" --file hello.txt --line 1 1,1
```

### 5.3 用户和组管理

#### 用户管理
```bash
# 创建用户
gerrit create-account --full-name "Test User" --email "test@example.com" testuser

# 设置用户密码
gerrit set-password testuser

# 删除用户
gerrit delete-account testuser
```

#### 组管理
```bash
# 创建组
gerrit create-group --description "Developers group" developers

# 向组添加用户
gerrit set-members --add testuser developers

# 从组移除用户
gerrit set-members --remove testuser developers

# 删除组
gerrit delete-group developers
```

### 5.4 权限管理
```bash
# 设置项目权限
gerrit set-project --permission read --group developers --add my-project

gerrit set-project --permission push --group developers --add my-project

gerrit set-project --permission push --group developers --branch master --remove my-project
```

### 5.5 其他常用指令
```bash
# 查看Gerrit版本
gerrit version

# 查看Gerrit状态
gerrit show-queue

# 重新索引
gerrit reindex --project my-project

# 清理缓存
gerrit flush-caches
```

## 6. Gerrit工作流程完整练习

### 6.1 创建并提交变更
1. 克隆项目
2. 创建分支
3. 修改代码
4. 提交变更
5. 推送到Gerrit

### 6.2 审查变更
1. 登录Gerrit Web界面
2. 查看变更
3. 添加评论
4. 设置Code-Review分数
5. 设置Verified分数
6. 提交变更

### 6.3 处理评论和更新
```bash
# 修改文件
echo "Updated content" > hello.txt

# 添加并提交更新
git add hello.txt
git commit --amend

# 推送到Gerrit（更新同一变更）
git push gerrit HEAD:refs/for/master
```

### 6.4 合并变更
1. 登录Gerrit Web界面
2. 找到已批准的变更
3. 点击"Submit"

## 7. 常见问题及解决方案

### 7.1 SSH连接问题
**问题**：`Permission denied (publickey).`
**解决方案**：
1. 检查SSH密钥是否正确添加到Gerrit
2. 检查SSH配置文件：`~/.ssh/config`
3. 确保使用正确的用户名和端口

### 7.2 推送问题
**问题**：`fatal: remote error: You are not allowed to push code to this project`
**解决方案**：
1. 检查用户权限
2. 确保推送到`refs/for/`分支
3. 检查Gerrit项目配置

### 7.3 Gerrit启动失败
**问题**：`ERROR: Cannot start Gerrit: HTTP server failed to start`
**解决方案**：
1. 检查端口是否被占用：`netstat -tulpn | grep 8080`
2. 查看日志：`tail -f logs/error_log`
3. 检查Java版本是否兼容

### 7.4 变更不显示
**问题**：推送后在Gerrit界面看不到变更
**解决方案**：
1. 检查推送命令是否正确（必须是`refs/for/分支名`）
2. 检查用户权限
3. 查看Gerrit日志

## 8. 高级配置（可选）

### 8.1 配置反向代理（Apache）
```bash
# 创建Gerrit配置文件
sudo vim /etc/apache2/sites-available/gerrit.conf
```

添加以下内容：
```apache
<VirtualHost *:80>
    ServerName gerrit.example.com
    ProxyRequests Off
    ProxyVia Off
    ProxyPreserveHost On

    <Proxy *>
        Order deny,allow
        Allow from all
    </Proxy>

    ProxyPass / http://localhost:8080/
    ProxyPassReverse / http://localhost:8080/
</VirtualHost>
```

启用配置：
```bash
sudo a2ensite gerrit.conf
sudo a2enmod proxy_http
sudo systemctl restart apache2
```

### 8.2 配置PostgreSQL数据库
编辑Gerrit配置文件：`review_site/etc/gerrit.config`

```ini
[database]
  type = postgresql
  hostname = localhost
  database = reviewdb
  username = gerrit
  password = gerritpassword
```

重启Gerrit：
```bash
bin/gerrit.sh restart
```

## 9. 清理与卸载

### 9.1 停止Gerrit服务
```bash
sudo su - gerrit
cd review_site
bin/gerrit.sh stop
```

### 9.2 卸载Gerrit
```bash
# 删除Gerrit用户
sudo userdel -r gerrit

# 删除Gerrit安装目录
sudo rm -rf /opt/gerrit

# 删除Gerrit站点目录
sudo rm -rf /home/gerrit
```

## 10. 总结

本教程提供了Linux环境下Gerrit的完整练习流程，包括：
1. 环境准备与依赖安装
2. Gerrit服务器安装与配置
3. Gerrit客户端配置
4. Gerrit界面介绍
5. 所有Gerrit指令练习
6. 完整工作流程演练
7. 常见问题解决方案

通过按照本教程的步骤进行练习，您将全面掌握Gerrit的使用方法和所有指令。

## 11. 参考资源

- [Gerrit官方文档](https://gerrit-review.googlesource.com/Documentation/index.html)
- [Git官方文档](https://git-scm.com/doc)
- [Gerrit中文文档](https://gerrit-documentation-zh.readthedocs.io/zh_CN/latest/)
