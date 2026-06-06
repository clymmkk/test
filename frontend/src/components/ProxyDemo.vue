<template>
  <div class="proxy-demo">
    <section class="scenario" v-for="(scenario, index) in scenarios" :key="index">
      <div class="scenario-header">
        <span class="scenario-number">场景 {{ index + 1 }}</span>
        <h3>{{ scenario.title }}</h3>
      </div>
      <div class="scenario-desc">{{ scenario.description }}</div>
      <div class="request-info">
        <div><strong>访问路径：</strong><code>{{ scenario.path }}</code></div>
        <div><strong>代理目标：</strong><code>{{ scenario.target }}</code></div>
      </div>
      <button class="request-btn" @click="makeRequest(scenario, index)" :disabled="loading[index]">
        {{ loading[index] ? '请求中...' : '发送请求' }}
      </button>
      <div v-if="responses[index]" class="response-box">
        <div class="response-header">
          <span :class="['status', responses[index].ok ? 'success' : 'error']">
            {{ responses[index].ok ? '✓ 成功' : '✗ 失败' }}
          </span>
        </div>
        <pre>{{ JSON.stringify(responses[index].data, null, 2) }}</pre>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const loading = ref([])
const responses = ref([])

const scenarios = [
  {
    title: '标准 API 前缀转发',
    description: '最经典的反向代理场景。Nginx 将 /api/ 开头的请求转发到主服务。',
    path: '/api/hello',
    target: 'http://127.0.0.1:6000/api/hello',
    url: '/api/hello'
  },
  {
    title: '子服务路由',
    description: 'Nginx 将 /admin/ 开头的请求转发到独立的管理面板服务，实现服务拆分。',
    path: '/admin/dashboard',
    target: 'http://127.0.0.1:6001/admin/dashboard',
    url: '/admin/dashboard'
  },
  {
    title: '文件服务路由',
    description: 'Nginx 将 /upload/ 开头的请求转发到文件上传服务，可配置上传大小限制。',
    path: '/upload/files',
    target: 'http://127.0.0.1:6002/upload/files',
    url: '/upload/files'
  },
  {
    title: '路径重写',
    description: 'Nginx 将外部路径 /service/v1/hello 重写为内部路径 /api/hello，实现路径映射。',
    path: '/service/v1/hello',
    target: 'http://127.0.0.1:6000/api/hello（内部路径重写）',
    url: '/service/v1/hello'
  },
  {
    title: '末尾斜杠差异对比',
    description: 'proxy_pass 末尾不带斜杠时，location 匹配部分会被保留。对比 /api-v2/hello 和 /api/hello 的差异。',
    path: '/api-v2/api/hello',
    target: 'http://127.0.0.1:6000/api/hello（proxy_pass 不带斜杠）',
    url: '/api-v2/api/hello'
  },
  {
    title: '静态资源服务',
    description: 'Nginx 直接提供 Vue 构建产物，try_files 指令支持 SPA 路由。',
    path: '/',
    target: 'frontend/dist/index.html（直接由 Nginx 提供）',
    url: null
  }
]

async function makeRequest(scenario, index) {
  if (!scenario.url) return
  loading.value[index] = true
  try {
    const response = await fetch(scenario.url)
    const data = await response.json()
    responses.value[index] = { ok: response.ok, data }
  } catch (error) {
    responses.value[index] = { ok: false, data: { error: error.message } }
  } finally {
    loading.value[index] = false
  }
}
</script>

<style scoped>
.proxy-demo {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.scenario {
  background: white;
  border-radius: 10px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  border-left: 4px solid #667eea;
}

.scenario-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.scenario-number {
  background: #667eea;
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
}

.scenario-header h3 {
  font-size: 1.2rem;
  color: #333;
}

.scenario-desc {
  color: #666;
  margin-bottom: 16px;
  line-height: 1.6;
}

.request-info {
  background: #f8f9fa;
  padding: 12px 16px;
  border-radius: 8px;
  margin-bottom: 16px;
  font-size: 0.9rem;
}

.request-info div {
  margin-bottom: 6px;
}

.request-info code {
  background: #e9ecef;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  color: #495057;
}

.request-btn {
  background: #667eea;
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 6px;
  font-size: 0.95rem;
  cursor: pointer;
  transition: background 0.2s;
}

.request-btn:hover {
  background: #5a67d8;
}

.request-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.response-box {
  margin-top: 16px;
  background: #1e1e1e;
  border-radius: 8px;
  overflow: hidden;
}

.response-header {
  padding: 8px 16px;
  background: #2d2d2d;
  border-bottom: 1px solid #3d3d3d;
}

.status {
  font-size: 0.85rem;
  font-weight: 600;
}

.status.success {
  color: #4ade80;
}

.status.error {
  color: #f87171;
}

.response-box pre {
  padding: 16px;
  margin: 0;
  color: #e4e4e4;
  font-size: 0.85rem;
  line-height: 1.6;
  overflow-x: auto;
}
</style>
