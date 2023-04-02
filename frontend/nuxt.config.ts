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
        siteKey: process.env.TURNSTILE_SITE,
    },
    apiParty: {
        endpoints: {
            api: {
                url: process.env.API_URL || "http://localhost:3000",
            },
        },
    },
    runtimeConfig: {
        turnstile: {
            secretKey: process.env.TURNSTILE_SECRET,
        },
    },
});
