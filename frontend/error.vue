<template>
    <v-container>
        <v-row class="py-16" justify="center" align="center">
            <v-col cols="auto">
                <h1 class="text-h3 text-center">404 - Page not found</h1>
                <p class="mt-8 text-medium-emphasis text-center">
                    The page you are looking for does not exist.
                </p>
                <v-btn block class="mt-8" color="primary" to="/" :ripple="false"
                    >Go to home</v-btn
                >
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
    useHead({
        title: "404 - Page not found",
    });
</script>
