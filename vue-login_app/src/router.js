import { createRouter, createWebHistory } from "vue-router";
import Login from "./pages/Login-page.vue";
import AdminHome from "./pages/admin-home-page.vue";
import ClientHome from "./pages/client-home-page.vue";
import Profile from "./pages/profile-page.vue";
import SignUp from "./pages/signup-page.vue";

const routes = [
    {path:'/login-page', component: Login},
    {path:'/admin-home-page', component: AdminHome},
    {path:'/client-home-page', component: ClientHome},
    {path:'/profile-page', component: Profile},
    {path:'/signup-page', component: SignUp},
    ];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;