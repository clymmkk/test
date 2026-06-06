# Nginx 反向代理配置全栈演示项目

一个完整的前后端分离全栈演示项目，用于深入学习 Nginx 反向代理配置。项目通过 Vue 3 前端 + Flask 后端 + Nginx 反向代理的经典架构，演示 Nginx 如何作为统一入口处理多种路径模式的反向代理场景。

## 项目架构

```
nginx-reverse-proxy-demo/
├── frontend/     # Vue 3 前端应用
├── backend/      # Flask 后端 API（多服务）
├── nginx/        # Nginx 配置目录
└── README.md
```

## 技术栈

- **前端**：Vue 3 + Vite
- **后端**：Flask (Python)
- **反向代理**：Nginx

## 快速开始

### 1. 安装依赖

```bash
# 安装 Python 依赖
cd backend
pip install -r requirements.txt

# 安装 Node.js 依赖
cd ../frontend
npm install
```

### 2. 启动后端服务

```bash
cd backend
# 启动主服务（端口 6000）
python app.py

# 启动管理面板（端口 6001）
python admin_app.py

# 启动文件上传服务（端口 6002）
python upload_app.py
```

### 3. 构建前端

```bash
cd frontend
npm run build
```

### 4. 启动 Nginx

将 `nginx/nginx.conf` 复制到 Nginx 配置目录（如 `C:/nginx/conf/nginx.conf`），然后启动 Nginx。

或者使用命令行启动：

```bash
nginx -c C:/Users/cly/Desktop/nginx/nginx/nginx.conf
```

### 5. 访问演示页面

打开浏览器访问 `http://localhost`，即可看到演示页面。

## 反向代理场景详解

### 场景 1：标准 API 前缀转发

```nginx
location /api/ {
    proxy_pass         http://127.0.0.1:6000;
    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
}
```

**说明**：这是最常见的反向代理场景。Nginx 将 `/api/` 开头的请求转发到后端服务。

### 场景 2：子服务路由

```nginx
location /admin/ {
    proxy_pass         http://127.0.0.1:6001;
    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
}
```

**说明**：Nginx 可以根据不同路径将请求转发到不同的后端服务，实现服务拆分。

### 场景 3：文件服务路由

```nginx
location /upload/ {
    proxy_pass         http://127.0.0.1:6002;
    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
    client_max_body_size 100M;
}
```

**说明**：文件上传服务可以独立部署，Nginx 可以配置上传大小限制等参数。

### 场景 4：路径重写

```nginx
location /service/v1/ {
    proxy_pass         http://127.0.0.1:5000/api/;
    proxy_set_header   Host             $host;
}
```

**说明**：客户端访问 `/service/v1/hello`，Nginx 会将其重写为 `/api/hello` 转发到后端。这在版本升级或接口重构时非常有用。

### 场景 5：末尾斜杠差异

```nginx
location /api-v2 {
    proxy_pass         http://127.0.0.1:6000;  # 不带斜杠
    proxy_set_header   Host             $host;
}
```

**说明**：`proxy_pass` 末尾带斜杠和不带斜杠有本质区别：

- 带斜杠（`/api/`）：Nginx 会去掉 location 匹配部分
- 不带斜杠（`/api-v2`）：Nginx 会保留 location 匹配部分

### 场景 6：静态资源服务

```nginx
location / {
    root   C:/Users/cly/Desktop/nginx/frontend/dist;
    index  index.html;
    try_files $uri $uri/ /index.html;
}
```

**说明**：`try_files` 指令对于单页应用（SPA）非常重要，确保前端路由能正常工作。

## 验证方法

1. 启动所有服务后，访问 `http://localhost`
2. 点击页面上的"发送请求"按钮
3. 观察响应结果，确认请求通过 Nginx 代理成功
4. 打开浏览器开发者工具，查看响应头中的 `X-Proxy-By: nginx`

## 常见问题

### 问题 1：Nginx 无法访问前端构建产物

**解决方案**：确保 `nginx.conf` 中的 `root` 路径正确指向 `frontend/dist` 目录。

### 问题 2：proxy_pass 末尾斜杠导致路径错误

**解决方案**：理解带斜杠和不带斜杠的区别，根据实际需求选择。

### 问题 3：跨域问题

**解决方案**：后端已启用 CORS 支持，或者通过 Nginx 统一入口避免跨域。
