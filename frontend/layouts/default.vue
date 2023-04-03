<template>
    <v-app :theme="theme">
        <v-app-bar>
            <v-container>
                <v-row
                    align="center"
                    justify="space-between"
                    class="ml-md-n4 mr-md-n4 ml-n3 mr-n3">
                    <v-col cols="auto">
                        <v-btn
                            href="/"
                            prepend-icon="mdi-vuetify"
                            class="text-h6"
                            >GetStory.io</v-btn
                        >
                    </v-col>
                    <v-col cols="auto" class="d-md-inline d-none">
                        <v-btn
                            v-for="item in header"
                            :key="item"
                            class="text-body-2"
                            :to="item.to"
                            >{{ item.title }}</v-btn
                        >
                    </v-col>
                    <v-col cols="auto" class="d-md-none">
                        <v-btn
                            class="d-md-none"
                            icon="mdi-menu"
                            variant="text"
                            @click.stop="drawer = !drawer" />
                    </v-col>
                </v-row>
            </v-container>
        </v-app-bar>
        <v-navigation-drawer temporary location="right" v-model="drawer">
            <v-list density="compact" nav>
                <v-list-item
                    v-for="item in header"
                    :key="item"
                    :title="item.title"
                    :to="item.to" />
            </v-list>
        </v-navigation-drawer>

        <v-main>
            <slot />
        </v-main>

        <v-footer>
            <v-container>
                <v-row
                    align="center"
                    justify="center"
                    justify-md="space-between"
                    class="ml-md-n4 mr-md-n4 ml-n3 mr-n3">
                    <v-col md="auto" cols="12" order="2" order-md="1">
                        <p class="text-body-2">
                            Copyright &copy;
                            {{ new Date().getFullYear() }} GetStory.io, LLC
                        </p>
                    </v-col>
                    <v-col md="auto" cols="12" order="1" order-md="2">
                        <v-icon icon="mdi-vuetify" />
                    </v-col>
                </v-row>
            </v-container>
        </v-footer>
    </v-app>
</template>

<script setup>
    const drawer = ref(false);
    const theme = ref("dark");
    const header = ref([
        {title: "About", to: "/about"},
        {title: "Contact", to: "/contact"},
        {title: "Terms & Services", to: "/terms"},
    ]);
</script>
