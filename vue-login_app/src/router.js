import { createRouter, createWebHistory } from "vue-router";
import Login from "./pages/Login-page.vue";
import Home from "./pages/home-page.vue";
import Profile from "./pages/profile-page.vue";

const routes = [
    {path:'/login-page', component: Login},
    {path:'/home-page', component: Home},
    {path:'/profile-page', component: Profile},
    ];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;