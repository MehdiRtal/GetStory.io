<template>
    <v-sheet class="py-16" color="background">
        <v-container>
            <v-responsive width="900" class="mx-auto">
                <p class="text-h4 text-md-h3 text-center">
                    Tell us about yourself
                </p>
                <p class="mt-3 text-medium-emphasis text-center">
                    If you have business inquiries or other questions, please
                    fill out the following form to contact us. Thank you.
                </p>

                <v-form class="mt-8">
                    <v-text-field
                        counter="10"
                        label="Enter your name"
                        variant="outlined"
                        bg-color="surface"></v-text-field>
                    <v-text-field
                        counter="10"
                        label="Enter your email"
                        variant="outlined"
                        bg-color="surface"></v-text-field>
                    <v-textarea
                        label="Your message"
                        bg-color="surface"
                        variant="outlined"></v-textarea>
                    <v-btn
                        border
                        size="large"
                        class="text-body-1"
                        block
                        color="primary"
                        >Send</v-btn
                    >
                </v-form>
            </v-responsive>
        </v-container>
    </v-sheet>
</template>

<script setup>
    useHead({
        title: "Contact",
    });
</script>
