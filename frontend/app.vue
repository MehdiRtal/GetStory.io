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
        ogTitle: "GetStory.io",
        ogDescription:
            "Download Instagram Stories quickly, easily and only in good quality. Seemed impossible? Now it is real.",
    });
</script>
