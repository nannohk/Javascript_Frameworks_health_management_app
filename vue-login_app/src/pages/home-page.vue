<template>
    <div class="row">
        <div class="col-md-6 offse-md-3">
           <h1>Sign Out!</h1>
           <button class="btn btn-primary" @click="SignOut">Sign Out</button>
        </div>
    </div>
</template>

<script>
import router from '@/router';
export default {
    methods: {
        SignOut() {
            router.push('./login-page');
        }
    }
}
</script>