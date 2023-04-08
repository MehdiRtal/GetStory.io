import vuetify from "vite-plugin-vuetify";

export default defineNuxtConfig({
    telemetry: false,
    css: ["vuetify/styles", "@mdi/font/css/materialdesignicons.min.css"],
    build: {
        transpile: ["vuetify"],
    },
    modules: [
        "@nuxtjs/robots",
        "@nuxt/devtools",
        "@nuxtjs/turnstile",
        "nuxt-api-party",
        "nuxt-gtag",
        "@nuxtjs/google-fonts",
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
                url: process.env.API_URL!,
            },
        },
    },
    gtag: {
        id: process.env.GTAG_ID,
        loadingStrategy: "async",
    },
});
