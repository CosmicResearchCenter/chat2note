/// <reference types="vite/client" />
// src/env.d.ts
interface ImportMetaEnv {
    readonly VITE_BASE_URL: string;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}
