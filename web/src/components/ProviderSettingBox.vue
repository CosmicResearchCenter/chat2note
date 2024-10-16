<template>
    <el-card class="box-card">
        <template #header>
            <div class="card-header">
                <el-select v-model="value" placeholder="Select" size="large" style="width: 240px">
                    <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
            </div>
        </template>
        <div class="card-body">
            <el-form label-width="400px" label-position="top">
                <!-- API_KEY -->
                <el-form-item v-if="providers_info[value].API_KEY !== undefined" label="API_KEY">
                    <el-input v-model="providers_info[value].API_KEY" />
                </el-form-item>

                <!-- BASE_URL -->
                <el-form-item v-if="providers_info[value].BASE_URL !== undefined" label="BASE_URL">
                    <el-input v-model="providers_info[value].BASE_URL" />
                </el-form-item>

                <!-- MODEL -->
                <el-form-item v-if="providers_info[value].MODEL !== undefined" label="MODEL">
                    <el-input v-model="providers_info[value].MODEL" />
                </el-form-item>

                <!-- APP_ID (for SPARKAI) -->
                <el-form-item v-if="providers_info[value].APP_ID !== undefined" label="APP_ID">
                    <el-input v-model="providers_info[value].APP_ID" />
                </el-form-item>

                <!-- API_SECRET (for SPARKAI) -->
                <el-form-item v-if="providers_info[value].API_SECRET !== undefined" label="API_SECRET">
                    <el-input v-model="providers_info[value].API_SECRET" />
                </el-form-item>

                <!-- DOMAIN (for SPARKAI) -->
                <el-form-item v-if="providers_info[value].DOMAIN !== undefined" label="DOMAIN">
                    <el-input v-model="providers_info[value].DOMAIN" />
                </el-form-item>
                <!-- 提交按钮 -->
                <el-form-item>
                    <el-button type="primary" @click="submitProvider">提交</el-button>
                </el-form-item>
            </el-form>
        </div>
    </el-card>
</template>

<script lang="ts">
import { ref, defineComponent, reactive } from 'vue';
import { ElMessage } from 'element-plus';

export default defineComponent({
    name: 'ProviderSettingBox',
    setup() {
        const options = [
            { value: 'OPENAI', label: 'OPENAI' },
            { value: 'ZHIPUAI', label: 'ZHIPUAI' },
            { value: 'DOUBAO', label: 'DOUBAO' },
            { value: 'SPARKAI', label: 'SPARKAI' },
        ];

        const providers_info = reactive({
            OPENAI: {
                API_KEY: "",
                BASE_URL: "https://api.openai.com/v1",
                MODEL: "gpt-4o-mini",
            },
            ZHIPUAI: {
                API_KEY: "",
                MODEL: "glm-4",
            },
            DOUBAO: {
                API_KEY: "",
                BASE_URL: "",
                MODEL: "",
            },
            SPARKAI: {
                APP_ID: "",
                API_KEY: "",
                API_SECRET: "",
                BASE_URL:"",
                DOMAIN: "",
            },
        });

        const value = ref(options[0].value);

        const submitProvider = async () => {
            if(!providers_info[value.value].API_KEY) {
                ElMessage.error('API_KEY不能为空');
                return;
            }
            
            const data = {
                provider: value.value,
                api_key: providers_info[value.value]?.API_KEY || "",
                config: JSON.stringify(providers_info[value.value])
            };
            console.log(data);
            try {
                const response = await fetch('http://127.0.0.1:9988/v1/api/chat2note/set_provider', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    throw new Error(`提交失败: ${response.statusText}`);
                }

                const result = await response.json();
                console.log('提交成功:', result);
                ElMessage({
                    message: '信息设置成功',
                    type: 'success',
                })
            } catch (error) {
                console.error('提交失败:', error);
                ElMessage.error('设置失败')
            }
        };

        return {
            options,
            value,
            providers_info,
            submitProvider
        };
    },
});
</script>
<style>

</style>