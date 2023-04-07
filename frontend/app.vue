<template>
    <NuxtLayout>
        <NuxtPage />
    </NuxtLayout>
</template>

<script setup>
    useHead({
        htmlAttrs: {
            lang: "en",
        },
        titleTemplate: "%s - GetStory.io",
    });
    useServerSeoMeta({
        description:
            "Fastest tool ever for downloading Instagram stories anonymously 100%, no installation required, no need for an Instagram account.",
        ogImage: "https://getstory.io/og.png",
    });
</script>
