<template>
    <div class="row">
        <div class="col-md-6 offse-md-3">
           <h1>Welcome!!</h1>
           <button class="btn btn-primary" @click="Back">Back</button>
        </div>
    </div>
</template>

<script>
import router from '@/router';
export default {
    methods: {
        Back() {
            router.push('./login-page');
        }
    }
}
</script>