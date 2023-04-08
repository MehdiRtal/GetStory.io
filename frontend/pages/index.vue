<template>
    <v-overlay
        v-model="overlay"
        scrim="black"
        class="align-center justify-center">
        <!-- <v-text-field v-model="token" /> -->
        <Turnstile
            v-model:model-value="token"
            @update:model-value="loadStories" />
    </v-overlay>

    <v-sheet class="py-16" color="background" border="b">
        <v-container>
            <h1 class="text-h4 text-md-h3">Instagram Story Saver</h1>
            <h2 class="mt-3 text-body-1 text-medium-emphasis">
                Download Instagram Stories quickly, easily and only in good
                quality. Seemed impossible? Now it is real
            </h2>
            <v-chip-group class="mt-3" variant="outlined">
                <v-chip
                    class="text-success"
                    prepend-icon="mdi-check"
                    text="Anonymous" />
                <v-chip
                    class="text-success"
                    prepend-icon="mdi-check"
                    text="Fast" />
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
                hint="Example: Alex"
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
                    center-active
                    v-if="stories.length"
                    class="mt-8"
                    show-arrows>
                    <v-slide-group-item v-for="story in stories" :key="story">
                        <v-card border class="mr-8" width="225">
                            <v-img
                                height="400"
                                cover
                                :src="cdn(story.thumbnail)" />
                            <v-card-text>
                                <v-row justify="center" align="center">
                                    <v-col
                                        cols="auto"
                                        v-if="story.type == 'Video'"
                                        class="mr-2">
                                        <v-btn
                                            size="small"
                                            color="success"
                                            icon="mdi-play"
                                            :href="cdn(story.url)"
                                            target="_blank" />
                                    </v-col>
                                    <v-col cols="auto">
                                        <v-btn
                                            size="small"
                                            variant="outlined"
                                            color="success"
                                            @click="
                                                downloadStory(
                                                    cdn(story.url),
                                                    story.type
                                                )
                                            "
                                            icon="mdi-download" /></v-col></v-row
                            ></v-card-text>
                        </v-card>
                    </v-slide-group-item>
                </v-slide-group>
            </v-slide-y-transition>
        </v-container>
    </v-sheet>

    <v-sheet class="py-16">
        <v-container>
            <p class="text-h4 text-center">
                Enjoy the amazing features of GetStory.io
            </p>
            <p class="text-success mt-3 text-center">
                Explore our top features and benefits, designed to make your
                Instagram experience seamless, efficient, and enjoyable.
            </p>
            <v-row justify="space-between" class="mt-16">
                <v-col md="5" cols="12">
                    <p class="text-h5">Privacy and security</p>
                    <p class="mt-4">
                        Trust our Instagram story saver with your privacy, as we
                        never store user information or require unnecessary
                        permissions.
                    </p>
                </v-col>
                <v-col md="5" cols="12" class="text-md-end mt-md-0 mt-8"
                    ><p class="text-h5">Speed and efficiency</p>
                    <p class="mt-4">
                        Save time with our fast and efficient story saver,
                        making Instagram story download a breeze.
                    </p></v-col
                >
            </v-row>
            <v-row justify="space-between" class="mt-8">
                <v-col md="5" cols="12">
                    <p class="text-h5">High-quality downloads</p>
                    <p class="mt-4">
                        Get the best quality with our Instagram story saver,
                        preserving the original resolution and quality of your
                        favorite Stories.
                    </p>
                </v-col>
                <v-col md="5" cols="12" class="text-md-end mt-md-0 mt-8"
                    ><p class="text-h5">No watermarks</p>
                    <p class="mt-4">
                        Enjoy a clean, watermark-free downloads with our
                        Instagram story saver.
                    </p></v-col
                >
            </v-row>
            <v-row justify="space-between" class="mt-8">
                <v-col md="5" cols="12">
                    <p class="text-h5">User-friendly interface</p>
                    <p class="mt-4">
                        Experience the simplicity of our Instagram story
                        downloader with an intuitive, easy-to-use interface &
                        friendly captcha that gets solved by itself within two
                        seconds, so you don't have to deal with solving any
                        challenges manually.
                    </p>
                </v-col>
                <v-col md="5" cols="12" class="text-md-end mt-md-0 mt-8"
                    ><p class="text-h5">Platform compatibility</p>
                    <p class="mt-4">
                        Our story saver is compatible with various devices and
                        operating systems, including Windows, macOS, Android,
                        and iOS, making Instagram story download accessible for
                        everyone.
                    </p></v-col
                >
            </v-row>
        </v-container>
    </v-sheet>

    <v-sheet class="py-16" color="background" border="t">
        <v-container>
            <h2 class="text-h4 text-center">Frenquently Asked Questions</h2>
            <p class="text-success mt-3 text-center">
                We have prepared answers to some of the questions that might
                come to your mind
            </p>
            <v-expansion-panels class="mt-8 border rounded" variant="accordion">
                <v-expansion-panel v-for="faq in faqs" :key="faq">
                    <v-expansion-panel-title>
                        <h3 class="text-body-2">{{ faq.title }}</h3>
                    </v-expansion-panel-title>
                    <v-expansion-panel-text>
                        {{ faq.text }}
                    </v-expansion-panel-text>
                </v-expansion-panel>
            </v-expansion-panels>
        </v-container>
    </v-sheet>
</template>

<script setup>
    useHead({
        title: "Instagram Story Saver - Download & View Instagram Stories Anonymously",
    });
    useServerSeoMeta({
        description:
            "Fastest tool ever for downloading Instagram stories anonymously 100%, no installation required, no need for an Instagram account.",
        ogImage: "https://getstory.io/og.png",
    });
    const faqs = ref([
        {
            title: "Will my account appear in viewers list when watching or saving the story?",
            text: "Don't worry, your account won't show up in the viewers list for the story. You can watch or save stories in complete privacy.",
        },
        {
            title: "Can I save Instagram stories from a private account?",
            text: "Unfortunately, GetStory.io doesn't support saving from private accounts. Account has to be 'public'.",
        },
        {
            title: "How do I download Instagram stories?",
            text: "To download or save Instagram stories, you can type/paste username in input field at top of page for account you want to save their stories. You can also paste direct link to story, and we'll take care of it for you.",
        },
        {
            title: "I'm trying to download Instagram story, but it's playing instead. What should I do?",
            text: "The reason for this is the browser you're using. If you want a recommendation, use Safari on iOS، Google Chrome on Android. They work well.",
        },
        {
            title: "Is GetStory.io safe?",
            text: "You don't have to create an account or provide any personal or private information, and we don't keep records of any downloads that happen on our website, nor do we ask you to install any tools or applications on your device to use our website. So yeah, you can say GetStory.io is completely safe.",
        },
        {
            title: "I ran into a problem while using GetStory.io.",
            text: "As you know, technical errors can happen from time to time, so you can give it another try, it might work. If the error persists even after trying again, you can reach out to us through the 'contact us page'. We recommend providing a screenshot or a detailed description of the issue you encountered so that we can fix it in the near future.",
        },
        {
            title: "I couldn't get past Cloudflare captcha, What's the way forward?",
            text: "Sorry about that, but it's necessary to use captcha to protect our API from unwanted requests. If you can't get past the captcha, try refreshing page & trying again. Also, we recommend deleting cookies from your browser before trying.",
        },
        {
            title: "Can I save Instagram stories on my iPhone?",
            text: "Undoubtedly, Instagram stories can be downloaded on both iOS & Android devices, including smartphones & tablets. We have tried and tested our tool on various operating systems and browsers, and it operates seamlessly.",
        },
    ]);
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

    function cdn(url) {
        return `https://cdn.getstory.io/?q=${encodeURIComponent(url)}`;
    }

    async function downloadStory(url, type) {
        const response = await $fetch(url, {
            method: "GET",
            responseType: "blob",
        });
        const link = document.createElement("a");
        link.href = window.URL.createObjectURL(response);
        if (type === "Video") {
            link.download = `getstory-io_${new Date().getTime()}.mp4`;
        }
        if (type === "Image") {
            link.download = `getstory-io_${new Date().getTime()}.jpg`;
        }
        link.click();
    }

    async function loadStories() {
        async function getStories() {
            const response = await $api("/instagram/stories", {
                method: "GET",
                query: {username: username.value, turnstile_token: token.value},
            }).catch((e) => {
                throw e.data.data.message;
            });
            return response.stories;
        }
        if (error.value) {
            error.value = "";
        }
        if (stories.value.length) {
            stories.value = [];
        }
        overlay.value = false;
        loading.value = true;
        try {
            stories.value = await getStories();
        } catch (e) {
            error.value = e;
        }
        loading.value = false;
    }

    watch(username, async () => {
        error.value = "";
    });
</script>
