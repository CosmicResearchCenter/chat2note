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

                <!-- OPENAI -->
                <!-- API_KEY -->
                <el-form-item v-if="value=='OPENAI'" label="API_KEY">
                    <el-input v-model="providers_info.OPENAI.API_KEY" />
                </el-form-item>
                <!-- BASE_URL -->
                <el-form-item v-if="value=='OPENAI'" label="BASE_URL">
                    <el-input v-model="providers_info.OPENAI.BASE_URL" />
                </el-form-item> <!-- MODEL -->
                <el-form-item v-if="value=='OPENAI'" label="MODEL">
                    <el-input v-model="providers_info.OPENAI.MODEL" />
                </el-form-item>

                <!-- SPARKAI -->
                <!-- APP_ID (for SPARKAI) -->
                <el-form-item v-if="value=='SPARKAI'" label="APP_ID">
                    <el-input v-model="providers_info.SPARKAI.APP_ID" />
                </el-form-item>
                <!-- API_SECRET (for SPARKAI) -->
                <el-form-item v-if="value=='SPARKAI'" label="API_SECRET">
                    <el-input v-model="providers_info.SPARKAI.API_SECRET" />
                </el-form-item>
                <el-form-item v-if="value=='SPARKAI'" label="API_KEY">
                    <el-input v-model="providers_info.SPARKAI.API_KEY" />
                </el-form-item>
                <!-- API_SECRET (for SPARKAI) -->
                <el-form-item v-if="value=='SPARKAI'" label="BASE_URL">
                    <el-input v-model="providers_info.SPARKAI.BASE_URL" />
                </el-form-item>
                <el-form-item v-if="value=='SPARKAI'" label="DOMAIN">
                    <el-input v-model="providers_info.SPARKAI.DOMAIN" />
                </el-form-item>

                <!-- DOUBAO -->
                <!-- API_SECRET (for SPARKAI) -->
                <el-form-item v-if="value=='DOUBAO'" label="API_KEY">
                    <el-input v-model="providers_info.DOUBAO.API_KEY" />
                </el-form-item>
                <!-- DOMAIN (for SPARKAI) -->
                <el-form-item v-if="value=='DOUBAO'" label="BASE_URL">
                    <el-input v-model="providers_info.DOUBAO.BASE_URL" />
                </el-form-item>
                <el-form-item v-if="value=='DOUBAO'" label="MODEL">
                    <el-input v-model="providers_info.DOUBAO.MODEL" />
                </el-form-item>


                <!-- ZHIPUAI -->
                <el-form-item v-if="value=='ZHIPUAI'" label="API_KEY">
                    <el-input v-model="providers_info.ZHIPUAI.API_KEY" />
                </el-form-item>
                <el-form-item v-if="value=='ZHIPUAI'" label="MODEL">
                    <el-input v-model="providers_info.ZHIPUAI.MODEL" />
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
import type { ProvidersInfoType } from '../type/provider';
export default defineComponent({
    name: 'ProviderSettingBox',
    setup() {
        const options = [
            { value: 'OPENAI', label: 'OPENAI' },
            { value: 'ZHIPUAI', label: 'ZHIPUAI' },
            { value: 'DOUBAO', label: 'DOUBAO' },
            { value: 'SPARKAI', label: 'SPARKAI' },
        ];

        const providers_info = ref<ProvidersInfoType>({
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
                BASE_URL: "",
                DOMAIN: "",
            },
        });

        const value = ref<string>(options[0].value);

        const submitProvider = async () => {
            // if (!providers_info[value.value].API_KEY) {
            //     ElMessage.error('API_KEY不能为空');
            //     return;
            // }

            if (providers_info.value.DOUBAO == undefined && value.value == 'DOUBAO') {
                ElMessage.error('请先设置DOUBAO的API_KEY和BASE_URL');
                return;
            }

            if (providers_info.value.SPARKAI == undefined && value.value == 'SPARKAI') {
                ElMessage.error('请先设置SPARKAI的APP_ID, API_SECRET, BASE_URL, DOMAIN');
                return;
            }
            if (providers_info.value.OPENAI == undefined && value.value == 'OPENAI') {
                ElMessage.error('请先设置OPENAI的API_KEY和BASE_URL');
                return;
            }
            if (providers_info.value.ZHIPUAI == undefined && value.value == 'ZHIPUAI') {
                ElMessage.error('请先设置ZHIPUAI的API_KEY和MODEL');
                return;
            }
            let data = {};
            if (value.value == 'DOUBAO') {
                data = {
                    provider: value.value,
                    api_key: providers_info.value.DOUBAO.API_KEY,
                    config:JSON.stringify(providers_info.value.DOUBAO)
                }
            }else if(value.value == 'SPARKAI'){
                data = {
                    provider: value.value,
                    api_key: providers_info.value.SPARKAI.API_KEY,
                    config:JSON.stringify(providers_info.value.SPARKAI)
                }
            }else if(value.value == 'OPENAI'){
                data = {
                    provider: value.value,
                    api_key: providers_info.value.OPENAI.API_KEY,
                    config:JSON.stringify(providers_info.value.OPENAI)
                }
            }else if(value.value == 'ZHIPUAI'){
                data = {
                    provider: value.value,
                    api_key: providers_info.value.ZHIPUAI.API_KEY,
                    config:JSON.stringify(providers_info.value.ZHIPUAI)
                }
            }
            
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
<style></style>