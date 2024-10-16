// types.ts
export type ProvidersInfoType = {
    OPENAI: {
        API_KEY: string;
        BASE_URL: string;
        MODEL: string;
    };
    ZHIPUAI: {
        API_KEY: string;
        MODEL: string;
    };
    DOUBAO: {
        API_KEY: string;
        BASE_URL: string;
        MODEL: string;
    };
    SPARKAI: {
        APP_ID: string;
        API_KEY: string;
        API_SECRET: string;
        BASE_URL: string;
        DOMAIN: string;
    };
};
