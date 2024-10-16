// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// 引入markdown解析插件
// 创建一个声明文件来避免TypeScript编译错误
// declare module '@kangc/v-md-editor' {
//     const content: any;
//     export default content;
// };

// 引入markdown解析插件
// 创建一个声明文件来避免TypeScript编译错误

// import VMdEditor from '@kangc/v-md-editor';
import VMdPreview from '@kangc/v-md-editor/lib/preview';

import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import hljs from 'highlight.js';
VMdPreview.use(githubTheme, {
    Hljs: hljs,
});

import VMdEditor from '@kangc/v-md-editor';
VMdEditor.use(githubTheme, {
    Hljs: hljs,
});


import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

app.use(router)
app.use(VMdEditor);
app.use(ElementPlus)

app.mount('#app')
