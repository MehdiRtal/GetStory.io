import vuetify from "vite-plugin-vuetify";

export default defineNuxtConfig({
    app: {
        head: {
            title: "GetStory.io",
        },
    },
    telemetry: false,
    css: ["vuetify/styles", "@mdi/font/css/materialdesignicons.min.css"],
    build: {
        transpile: ["vuetify"],
    },
    typescript: {
        shim: false,
    },
    modules: [
        "@nuxt/devtools",
        "@nuxtjs/google-fonts",
        "@nuxtjs/turnstile",
        "nuxt-api-party",
        async (options, nuxt) => {
            // @ts-ignore
            // prettier-ignore
            nuxt.hooks.hook("vite:extendConfig", (config) => config.plugins.push(vuetify()));
        },
    ],
    googleFonts: {
        display: "swap",
        families: {
            Roboto: true,
        },
    },
    turnstile: {
        siteKey: process.env.TURNSTILE_SITE_KEY,
        secretKey: process.env.TURNSTILE_SECRET_KEY,
    },
    apiParty: {
        endpoints: {
            api: {
                url: "http://127.0.0.1:8000",
            },
        },
    },
});
