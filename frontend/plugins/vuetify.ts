import {createVuetify} from "vuetify";

export default defineNuxtPlugin((nuxtApp) => {
    const vuetify = createVuetify({
        defaults: {
            global: {
                flat: true,
                ripple: false,
                elevation: 0,
            },
            VRow: {
                noGutters: true,
            },
            VAppBar: {
                border: "b",
            },
            VFooter: {
                border: "t",
            },
        },
        theme: {
            defaultTheme: "dark",
            themes: {
                dark: {
                    colors: {
                        primary: "#1c466f",
                        background: "#181818",
                    },
                },
                light: {
                    colors: {
                        primary: "#1697f6",
                        background: "#f5f5f5",
                        surface: "#fff",
                    },
                },
            },
        },
        ssr: true,
    });

    nuxtApp.vueApp.use(vuetify);
});
