<template>
    <div class="row">
        <div class="col-md-4 shadow bg-white">
            <div>
                <div>
                    <h3>Sign Up</h3>
                    <hr />
                </div>
                <form @submit.prevent="signUp">
                    <div class="form-group">
                        <label>Email</label>
                        <input type="email" class="form-control" placeholder="Enter email" v-model="email">

                    </div>
                    <div class="error text-danger" v-if="this.errMail">
                        {{ this.errMail }}
                    </div>
                    <div class="form-group">
                        <label>Password</label>
                        <input type="password" class="form-control" placeholder="Enter password" v-model="password">

                    </div>
                    <div class="error text-danger" v-if="this.errPass">
                        {{ this.errPass }}
                    </div>
                    <div class="my-3">
                        <button type="submit" class="btn btn-primary">Sign Up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>

import axios from 'axios';
import router from '@/router';

export default {
    data() {
        return {
            email: '',
            password: '',
            errMail: '',
            errPass: '',
        }
    },

    methods: {
        async signUp() {
            const options = {
                method: 'post',
                url: 'http://localhost:1500/',
                email: this.email,
                password: this.password,
                role: 'client',
                purpose: 'signup',
                headers: {
                    'Content-Type': 'application/json'
                }
            }

            await axios.post('http://localhost:1500/', options).then((res) => {
                if (res.data.status === 'creation success') {
                    console.log(res.data.status);
                    localStorage.setItem('email', this.email);
                    router.push('/profile-page');
                } else {
                    console.log(res.data.status);
                }
            }).catch((err) => {
                console.log(err);
            })

        }
    }

}
</script>