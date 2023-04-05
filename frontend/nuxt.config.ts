import vuetify from "vite-plugin-vuetify";

export default defineNuxtConfig({
    telemetry: false,
    css: ["vuetify/styles", "@mdi/font/css/materialdesignicons.min.css"],
    build: {
        transpile: ["vuetify", "file-saver"],
    },
    modules: [
        "@nuxtjs/robots",
        "@nuxt/devtools",
        "@nuxtjs/google-fonts",
        "@nuxtjs/turnstile",
        "nuxt-api-party",
        "nuxt-gtag",
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
        id: "G-9J22ZE85RX",
    },
});
