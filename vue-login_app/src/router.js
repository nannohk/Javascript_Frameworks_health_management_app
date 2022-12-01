import { createRouter, createWebHistory } from "vue-router";
import Login from "./pages/Login-page.vue";
import AdminHome from "./pages/admin-home-page.vue";
import ClientHome from "./pages/client-home-page.vue";
import Profile from "./pages/profile-page.vue";
import SignUp from "./pages/signup-page.vue";
import IndexPage from "./pages/index-page.vue";
import PatientPage from "./pages/patients-page.vue";

const routes = [
    { path: '/login-page', component: Login, meta: { auth: false } },
    { path: '/admin-home-page', component: AdminHome, meta: { auth: true } },
    { path: '/client-home-page', component: ClientHome, meta: { auth: true } },
    { path: '/profile-page', component: Profile, meta: { auth: true } },
    { path: '/signup-page', component: SignUp, meta: { auth: false } },
    {path: '/index-page', component: IndexPage, meta: { auth: true } },
    {path: '/patients-page', component: PatientPage, meta: { auth: true } },
    { path: '/', redirect: '/login-page' },
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    if (to.meta.auth && !localStorage.getItem('email')) {
        next('/login-page');
    // } else if(!to.meta.auth && localStorage.getItem('email'))
    // {
    //     next('/login-page');
    } else {
        next();
    }
})

export default router;