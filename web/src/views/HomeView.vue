
<template>
  <div class="Main">
    <div class="chatUrlBox">
      <el-input v-model="url" style="width: 440px" placeholder="Please input" />
      <el-button @click="">获取</el-button>
    </div>
    <v-md-editor v-model="text" height="100vh"></v-md-editor>
  </div>
</template>
<script lang="ts" setup>
import { ref } from 'vue'
const text = ref("123")
const url = ref("123")
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
