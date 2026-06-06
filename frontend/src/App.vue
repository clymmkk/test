<template>
  <div class="container">
    <header>
      <h1>Nginx 反向代理配置演示</h1>
      <p>通过 Nginx 统一入口处理多种路径模式的反向代理场景</p>
    </header>
    <ProxyDemo />
  </div>
</template>

<script setup>
import ProxyDemo from './components/ProxyDemo.vue'
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  background: #f5f7fa;
  color: #333;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

header {
  text-align: center;
  padding: 40px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 12px;
  margin-bottom: 30px;
}

header h1 {
  font-size: 2rem;
  margin-bottom: 10px;
}

header p {
  opacity: 0.9;
  font-size: 1.1rem;
}
</style>
