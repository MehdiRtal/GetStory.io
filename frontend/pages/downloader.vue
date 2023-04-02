<template>
    <v-overlay
        v-model="overlay"
        scrim="black"
        class="align-center justify-center">
        <v-text-field v-model="token" />
        <!-- <Turnstile v-model="token" /> -->
    </v-overlay>

    <v-sheet class="py-16" color="background" border="b">
        <v-container>
            <p class="text-h4 text-md-h3">Instagram Stories Downloader</p>
            <p class="mt-3 text-medium-emphasis">
                Download Instagram Stories quickly, easily and only in good
                quality. Seemed impossible? Now it is real
            </p>
            <v-chip-group class="mt-3" variant="outlined">
                <v-chip
                    class="text-success"
                    prepend-icon="mdi-check"
                    text="Fast" />
                <v-chip
                    class="text-success"
                    prepend-icon="mdi-check"
                    text="High Quality" />
                <v-chip
                    class="text-success"
                    prepend-icon="mdi-check"
                    text="Free" />
            </v-chip-group>
            <v-text-field
                v-model="username"
                :disabled="loading"
                :loading="loading"
                class="mt-8 mx-auto"
                prepend-inner-icon="mdi-account"
                append-inner-icon="mdi-send"
                clearable
                label="Enter Username"
                hint="Example: Cristiano"
                variant="outlined"
                maxlength="30"
                counter
                bg-color="surface"
                :error-messages="error"
                persistent-hint
                @click:append-inner="overlay = !overlay"
                :rules="[rules.username]" />
            <v-slide-y-transition>
                <v-slide-group
                    v-if="stories.length != 0"
                    class="mt-8"
                    show-arrows>
                    <v-slide-group-item v-for="story in stories" :key="story">
                        <v-hover v-slot="{isHovering, props}">
                            <v-card
                                border
                                class="mr-8"
                                width="225"
                                v-bind="props">
                                <v-img
                                    height="400"
                                    cover
                                    :src="
                                        'https://cdn.mehdirtal7.workers.dev/?q=' +
                                        encodeURIComponent(story.thumbnail)
                                    " />
                                <v-overlay
                                    :model-value="isHovering"
                                    contained
                                    scrim="black"
                                    class="align-center justify-center">
                                    <v-btn
                                        v-if="story.type == 'Video'"
                                        icon="mdi-play"
                                        :href="story.url" />
                                    <v-btn
                                        icon="mdi-download"
                                        :href="story.url" />
                                </v-overlay>
                            </v-card>
                        </v-hover>
                    </v-slide-group-item>
                </v-slide-group>
            </v-slide-y-transition>
        </v-container>
    </v-sheet>

    <v-sheet class="py-16">
        <v-container>
            <v-row justify="space-between">
                <v-col md="6" cols="12">
                    <p class="text-h4">New customization system</p>
                    <p class="text-success mt-3">Global Defaults</p>
                    <strong class="mt-3"> Version 3 Only </strong>
                    <p class="mt-8">
                        Vuetify 3 has an unprecedented level of customization
                        options that make implementing any design system easy.
                    </p>
                    <p class="mt-3">
                        Assign default values for all components in the library,
                        including nested support.
                    </p>
                </v-col>
                <v-col md="6" cols="12">
                    <v-img
                        class="ml-md-auto mx-auto mx-md-0 mt-8 mt-md-0 rounded"
                        width="400"
                        transition="slide-y-transition"
                        src="https://cdn.vuetifyjs.com/store/themes/vite-free/chips-bar.png" />
                </v-col>
            </v-row>
            <v-divider class="my-16" />
            <v-row justify="space-between">
                <v-col md="6" cols="12">
                    <v-img
                        class="mr-md-auto mx-auto mx-md-0 mb-8 mb-md-0 rounded"
                        width="400"
                        transition="slide-y-transition"
                        src="https://cdn.vuetifyjs.com/store/themes/vite-free/slider.png" />
                </v-col>
                <v-col md="6" cols="12" class="text-end">
                    <p class="text-h4">Rebuilt from the ground up</p>
                    <p class="text-success mt-3">Composition API</p>
                    <p class="mt-8">
                        Vuetify 3 uses the Vue composition API to build
                        easy-to-use and feature rich components that work out of
                        the box.
                    </p>
                    <p class="mt-3">
                        <strong>How to use:</strong>

                        Services are now accessed through
                        <strong>use functions</strong> that follow the Vue 3
                        nomenclature and code styling.
                    </p>
                </v-col>
            </v-row>
            <v-divider class="my-16" />
            <v-row justify="space-between">
                <v-col md="6" cols="12">
                    <p class="text-h4">The most complete version yet</p>
                    <p class="text-success mt-3">Available now!</p>
                    <p class="mt-8">
                        The latest version is almost here. Use one of our free
                        themes to get a head start!
                    </p>
                    <p class="mt-3">
                        This theme is designed to demonstrate a basic single
                        page application using Vuetify 3.
                    </p>
                </v-col>
                <v-col md="6" cols="12">
                    <v-img
                        class="ml-md-auto mx-auto mx-md-0 mt-8 mt-md-0 rounded"
                        width="400"
                        transition="slide-y-transition"
                        src="https://cdn.vuetifyjs.com/store/themes/vite-free/layout.png" />
                </v-col>
            </v-row>
        </v-container>
    </v-sheet>

    <v-sheet class="py-16" color="background" border="t">
        <v-container>
            <p class="text-h4 text-center">Frequently Asked Questions</p>
            <p class="text-success mt-3 text-center">
                Here are some of the most frequently asked questions
            </p>
            <v-expansion-panels class="mt-8 border rounded" variant="accordion">
                <v-expansion-panel
                    v-for="i in 3"
                    :key="i"
                    title="Title"
                    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima">
                </v-expansion-panel>
            </v-expansion-panels>
        </v-container>
    </v-sheet>
</template>

<script setup>
    import {useDisplay} from "vuetify";

    const {name, mdAndUp} = useDisplay();
    const width = computed(() => {
        switch (name.value) {
            case "xs":
                return "100%";
            case "sm":
                return "100%";
            case "md":
                return "70%";
            case "lg":
                return "70%";
            case "xl":
                return "70%";
            case "xxl":
                return "70%";
        }
    });
    const username = ref("");
    const overlay = ref(false);
    const token = ref("");
    const loading = ref(false);
    const error = ref("");
    const stories = ref([]);
    const rules = ref({
        username: (value) => {
            const pattern = /^[\w](?!.*?\.{2})[\w.]{1,28}[\w]$/;
            return pattern.test(value) || "Invalid username";
        },
    });

    watch(token, async () => {
        stories.value = [];
        overlay.value = false;
        loading.value = true;
        try {
            stories.value = await getStories(username.value, token.value);
        } catch (e) {
            error.value = e;
        }
        loading.value = false;
        token.value = "";
    });

    watch(username, async () => {
        error.value = "";
    });

    async function getStories(username, token) {
        const response = await $api("/instagram/stories", {
            method: "GET",
            query: {username: username, turnstile_token: token},
        }).catch((e) => {
            throw e.data.data.message;
        });
        return response.stories;
    }
</script>
