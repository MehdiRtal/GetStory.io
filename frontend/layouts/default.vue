<template>
    <v-app :theme="theme">
        <v-app-bar>
            <v-container>
                <v-row
                    align="center"
                    justify="space-between"
                    class="ml-md-n4 mr-md-n4 ml-n3 mr-n3">
                    <v-col cols="auto">
                        <v-btn prepend-icon="mdi-vuetify" class="text-h6" to="/"
                            >InstaTools</v-btn
                        >
                    </v-col>
                    <v-col cols="auto" class="d-md-inline d-none">
                        <v-menu
                            open-on-hover
                            location="bottom right"
                            transition="scale-transition"
                            open-delay="0"
                            close-delay="0">
                            <template v-slot:activator="{props}">
                                <v-btn
                                    class="text-body-2"
                                    append-icon="mdi-chevron-down"
                                    v-bind="props">
                                    Instagram
                                </v-btn>
                            </template>
                            <v-list density="compact" nav border>
                                <v-list-item
                                    title="Stories Downloader"
                                    value
                                    to="/downloader" />
                                <v-list-item title="Post Downloader" value />
                            </v-list>
                        </v-menu>
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
                <v-list-group>
                    <template v-slot:activator="{props}">
                        <v-list-item title="Instagram" v-bind="props" />
                    </template>
                    <v-list-item title="Stories Downloader" to="/downloader" />
                    <v-list-item title="Post Downloader" />
                </v-list-group>
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
                            {{ new Date().getFullYear() }} SmTools, LLC
                        </p>
                    </v-col>
                    <v-col md="auto" cols="12" order="1" order-md="2">
                        <v-btn
                            v-for="item in footer"
                            :key="item"
                            class="text-body-2"
                            :to="item.to"
                            >{{ item.text }}</v-btn
                        >
                    </v-col>
                </v-row>
            </v-container>
        </v-footer>
    </v-app>
</template>

<script setup>
    const drawer = ref(false);
    const theme = ref("dark");
    const footer = ref([
        {text: "About us", to: "/about"},
        {text: "Contact", to: "/contact"},
        {text: "Terms", to: "/terms"},
    ]);
</script>
