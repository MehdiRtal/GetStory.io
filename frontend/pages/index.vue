<template>
    <v-overlay
        v-model="overlay"
        scrim="black"
        class="align-center justify-center">
        <!-- <v-text-field v-model="token" /> -->
        <Turnstile v-model="token" />
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
                <v-slide-group v-if="stories" class="mt-8" show-arrows>
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
                                        'https://cdn.getstory.io/?q=' +
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
                                        :href="story.url"
                                        target="_blank" />
                                    <v-btn
                                        download
                                        icon="mdi-download"
                                        :href="
                                            'https://cdn.getstory.io/?q=' +
                                            encodeURIComponent(story.url)
                                        " />
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
                    title="Will my account appear in viewers list when watching or saving the story?"
                    text="Don't worry, your account won't show up in the viewers list for the story. You can watch or save stories in complete privacy.">
                </v-expansion-panel>
                <v-expansion-panel
                    title="Can I save Instagram stories from a private account?"
                    text="Unfortunately, GetStory.io doesn't support saving from private accounts. Account has to be 'public'.">
                </v-expansion-panel>
                <v-expansion-panel
                    title="How do I download Instagram stories?"
                    text="To download or save Instagram stories, you can type/paste username in input field at top of page for account you want to save their stories. You can also paste direct link to story, and we'll take care of it for you.">
                </v-expansion-panel>
                <v-expansion-panel
                    title="I'm trying to download Instagram story, but it's playing instead. What should I do?"
                    text="The reason for this is the browser you're using. If you want a recommendation, use Safari on iOS، Google Chrome on Android. They work well.">
                </v-expansion-panel>
                <v-expansion-panel
                    title="Is GetStory.io safe?"
                    text="You don't have to create an account or provide any personal or private information, and we don't keep records of any downloads that happen on our website, nor do we ask you to install any tools or applications on your device to use our website. So yeah, you can say GetStory.io is completely safe.">
                </v-expansion-panel>
                <v-expansion-panel
                    title="I ran into a problem while using GetStory.io."
                    text="As you know, technical errors can happen from time to time, so you can give it another try, it might work. If the error persists even after trying again, you can reach out to us through the 'contact us page'. We recommend providing a screenshot or a detailed description of the issue you encountered so that we can fix it in the near future.">
                </v-expansion-panel>
                <v-expansion-panel
                    title="I couldn't get past Cloudflare captcha, What's the way forward?"
                    text="Sorry about that, but it's necessary to use captcha to protect our API from unwanted requests. If you can't get past the captcha, try refreshing page & trying again. Also, we recommend deleting cookies from your browser before trying.">
                </v-expansion-panel>
                <v-expansion-panel
                    title="Can I save Instagram stories on my iPhone?"
                    text="Undoubtedly, Instagram stories can be downloaded on both iOS & Android devices, including smartphones & tablets. We have tried and tested our tool on various operating systems and browsers, and it operates seamlessly.">
                </v-expansion-panel>
            </v-expansion-panels>
        </v-container>
    </v-sheet>
</template>

<script setup>
    useHead({
        title: "Home",
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
        if (token.value) {
            if (stories.value) {
                stories.value = [];
            }
            overlay.value = false;
            loading.value = true;
            try {
                stories.value = await getStories(username.value, token.value);
            } catch (e) {
                error.value = e;
            }
            loading.value = false;
            token.value = "";
        }
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
