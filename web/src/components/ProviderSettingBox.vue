<template>
    <el-card class="box-card">
        <template #header>
            <div class="card-header">
                <el-select v-model="value"
                placeholder="Select"
                size="large"
                style="width: 240px">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                />
                </el-select>
            </div>
        </template>
        
    </el-card>
</template>
<script lang="ts">
import {ref} from 'vue'


</script>