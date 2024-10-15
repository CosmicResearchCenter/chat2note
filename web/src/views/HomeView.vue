
<template>
  <div class="Main">
    <div class="chatUrlBox">
      <el-input v-model="url" style="width: 440px" placeholder="Please input" />
      <el-button @click="fetchStreamResponse">获取</el-button>
    </div>
    <v-md-editor v-model="responseText" height="100vh"></v-md-editor>
  </div>
</template>
<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue';
// const text = ref("123")
const url = ref("")
// 定义响应数据的状态
const responseText = ref('');

// 流式请求函数
const fetchStreamResponse = async () => {

  const post_url = 'http://127.0.0.1:9988/v1/api/chat2note/chat2note';
  const payload = {
    url: url.value,
    steaming: true
  };

  try {
    const response = await fetch(post_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (response.body) {
      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      let done = false;
      let receivedText = '';

      // 循环读取流式数据
      while (!done) {
        const { value, done: readerDone } = await reader.read();
        done = readerDone;

        if (value) {
          const chunk = decoder.decode(value, { stream: true });
          
          receivedText += chunk;
          responseText.value = receivedText;
          
        }
      }
    } else {
      console.error('No response body');
    }
  } catch (error) {
    console.error('Error fetching stream:', error);
  }
};

onMounted(() => {
    console.log("mounted\n123132")
});
</script>
<style scoped>
.Main{
  display: flex;
  flex-direction: column;
  justify-self: center;
  align-items: center;
}
.chatUrlBox{
  display: flex;
  flex-direction: row;
}
</style>
