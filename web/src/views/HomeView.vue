<template>
  <div class="Main">
    <div v-if="isLoading" class="loadingBox">
      <el-skeleton :rows="10" animated />
    </div>
    <div v-else class="paid">
      <div class="menuBoxDefault">
        <div class="setProviderButton">
          <el-button  @click="showSetProviderBox">设置提供商</el-button>
        </div>
      </div>
      <div class="hidenMarkdownBox" v-if="!showMarkdown">
        <h1 style="font-size: 100px;">Chat2Note</h1>
        <div class="chatUrlBox">
          <el-select
            v-model="provider"
            placeholder="模型提供商"
            size="large"
            style="width: 120px"
          >
            <el-option
              v-for="item in providers"
              :key="item"
              :label="item"
              :value="item"
            />
          </el-select>
          <el-input v-model="url" class="inputBox" placeholder="Please input URL" @keyup.enter="fetchStreamResponse" />
          <el-button class="inputButton" @click="fetchStreamResponse" type="primary">获取</el-button>
          
        </div>
      </div>

      <div class="markdownBox" v-else>
        <div class="menuBox">
          <el-select
            v-model="provider"
            placeholder="Select"
            size="large"
            style="width: 120px"
          >
            <el-option
              v-for="item in providers"
              :key="item"
              :label="item"
              :value="item"
            />
          </el-select>
          <div class="chatUrlBoxMini">
            <el-input v-model="url" style="width: 440px;height: 50px;"@keyup.enter="fetchStreamResponse" placeholder="Please input" />
            <el-button @click="fetchStreamResponse" style="width: 100px; height: 50px;"type="primary">获取</el-button>
          </div>
          <div class="exportBox">
            <el-button  @click="exportMarkdown" style="width: 100px; height: 50px;">导出</el-button>
          </div>
        </div>

        <v-md-editor v-model="responseText" height="100vh"></v-md-editor>
      </div>
    </div>
  </div>
  <el-dialog v-model="isShowSetProviderBox" title="设置提供商" width="800">
    <ProviderSettingBox class="providerSettingBox" ></ProviderSettingBox>
  </el-dialog>
  <!-- <el-drawer v-model="isShowSetProviderBox" title="I am the title" :with-header="false">
    
  </el-drawer> -->
  
</template>
<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue';
import ProviderSettingBox from '../components/ProviderSettingBox.vue';

//用于设置是否显示markdown编辑器
const showMarkdown = ref(false);

// 控制显示“加载中”提示
const isLoading = ref(false);
const providers = ref([]);
// const text = ref("123")
const url = ref("")
const provider = ref("")
// 定义响应数据的状态
const responseText = ref('');
// 导出为 .md 文件的函数
const exportMarkdown = () => {
  const blob = new Blob([responseText.value], { type: "text/markdown" });
  const url = URL.createObjectURL(blob);

  // 创建一个隐藏的 <a> 元素并触发下载
  const a = document.createElement("a");
  a.href = url;
  a.download = "note.md";  // 设置下载文件名
  a.click();

  // 释放 URL 对象
  URL.revokeObjectURL(url);
};
// 流式请求函数
const fetchStreamResponse = async () => {
  // 点击后显示加载中的提示
  isLoading.value = true;
  showMarkdown.value = true;
  // 清空响应数据
  responseText.value = '';
  // 发起请求
  const post_url = 'http://127.0.0.1:9988/v1/api/chat2note/chat2note';
  const payload = {
    url: url.value,
    provider: provider.value,
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
          isLoading.value = false;
          const chunk = decoder.decode(value, { stream: true });

          receivedText += chunk;
          responseText.value = receivedText;

        }
      }
    } else {
      console.error('No response body');
    }
  } catch (error) {
    isLoading.value = true;
    console.error('Error fetching stream:', error);
  }
};

const isShowSetProviderBox = ref(false);
const showSetProviderBox = () =>{
  
  if(isShowSetProviderBox.value){
    isShowSetProviderBox.value = false;
  }else{
    isShowSetProviderBox.value = true;
  }
}

const isShowSetUrlBox = ref(false);
const showSetUrlBox = () =>{
  if(isShowSetUrlBox.value){
    isShowSetUrlBox.value = false;
  }else{
    isShowSetUrlBox.value = true;
  }
}

const getProviders = async () => {
  const get_url = 'http://127.0.0.1:9988/v1/api/chat2note/get_providers';

  try {
    const response = await fetch(get_url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })

    if (response.ok) {
      const data = await response.json();
      providers.value = data.data;
      console.log(providers.value);
    } else {
      console.error('Error:', response.status);
    }
  } catch (error) {
    console.error('Error:', error);
    
  }
};
onMounted(() => {
  getProviders();
  console.log("mounted\n123132")
});
</script>
<style scoped>
.Main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* 水平方向居中 */
  align-items: center;
  /* 垂直方向居中 */
  height: 100vh;
  /* width: 100vh; */
  /* 让父容器充满整个视窗高度 */
}

.loadingBox {
  width: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.paid {

  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.menuBoxDefault{
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -10;
  width: 100%;
  height: 100%;
}
.hidenMarkdownBox {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: -300px;
}

.menuBox {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding-bottom: 10px
}

.chatUrlBoxMini {
  display: flex;
  align-self: center;
  justify-self: center;
}

.chatUrlBox {
  display: flex;
  gap: 10px;
  /* 控制输入框和按钮之间的间距 */
  align-items: center;
  flex-direction: row;
}

.markdownBox {
  padding-top: 100px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.inputBox {
  width: 800px;
  height: 60px;
  font-size: xx-large;
}

.inputButton {
  flex-shrink: 0;
  /* 防止按钮缩小 */
  width: 120px;
  height: 60px;
  font-size: xx-large;
}

</style>
