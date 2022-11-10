<template>
    <div class="row">
        <div class="col-md-4 shadow bg-white">
            <div>
                <div>
                    <h3>Login</h3>
                    <hr />
                </div>
                <form @submit.prevent="submitLogin">
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
                        <button type="submit" class="btn btn-primary">Login</button>
                    </div>
                </form>

                <div class="my-3" >
                        <button type="button" class="btn btn-primary" @click="signUp">Sign Up</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

import axios from 'axios';
import router from '@/router';
// import signInValidations from '../services/signInValidations';

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
        signUp() {
            router.push('/signup-page');
        },

        async submitLogin() {
            const options = {
                method: 'post',
                url: 'http://localhost:1500/',
                email: this.email,
                password: this.password,
                purpose: 'login',
                headers: {
                    'Content-Type': 'application/json'
                }
            }

            await axios.post('http://localhost:1500/', options).then((res) => {
                if (res.data.status === 'success') {
                    console.log(res.data.status);

                    localStorage.setItem('email', this.email);
                    localStorage.setItem('role', res.data.role);
                    // if the user doesn't have a profile, direct them to the profile page
                    if(res.data.fullname === null) {
                        router.push('/profile-page');
                    } else {
                        //get the role from the server and detemine the page to direct the user to the right page
                        if(res.data.role === 'admin') {
                            router.push('/admin-home-page');
                        } else {
                            router.push('/client-home-page');
                        }
                    }
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