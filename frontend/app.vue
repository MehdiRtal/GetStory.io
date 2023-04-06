<template>
    <NuxtLayout>
        <NuxtPage />
    </NuxtLayout>
</template>

<script setup>
    useHead({
        titleTemplate: "%s - GetStory.io",
    });
    useServerSeoMeta({
        description:
            "Fastest tool ever for downloading Instagram stories anonymously 100%, no installation required, no need for an Instagram account.",
    });
</script>
