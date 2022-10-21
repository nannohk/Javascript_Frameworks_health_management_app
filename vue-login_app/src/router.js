import { createRouter, createWebHistory } from "vue-router";
import Login from "./pages/Login-page.vue";

const routes = [
    {path:'/login-page', component: Login}
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;