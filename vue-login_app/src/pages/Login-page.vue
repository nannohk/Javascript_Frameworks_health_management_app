<template>
    <div class="row container py-5 h-100 d-flex justify-content-center align-items-center">
        <div class="col-md-4 shadow card text-black">
            <div class="mb-md-5 mt-md-4 pb-5 align-items-center">
                <div>
                    <h3 class="text-center fw-bold mb-2 text-uppercase" style="color: #0D6EFD;">Login</h3>
                    <hr />
                </div>
                <form @submit.prevent="submitLogin">
                    <div class="form-outline form-white mb-4">
                        <label style="color: #0D6EFD;">Email</label>
                        <input type="email" class="form-control form-control-lg" placeholder="Enter email"
                            v-model="email">

                    </div>
                    <div class="error text-danger" v-if="this.errMail">
                        {{ this.errMail }}
                    </div>
                    <div class="form-outline form-white mb-4">
                        <label style="color: #0D6EFD;">Password</label>
                        <input type="password" class="form-control form-control-lg" placeholder="Enter password"
                            v-model="password">

                    </div>
                    <div class="error text-danger" v-if="this.errPass">
                        {{ this.errPass }}
                    </div>
                    <div class="text-center mt-5">
                        <button type="submit" class="btn-primary btn btn-outline-white btn-lg px-5">Login</button>
                    </div>
                </form>

                <div class="mt-2 text-center">
                    <p class="mb-0">Don't have an account? <a @click="signUp" class="fw-bold" style="cursor: pointer;" >Sign Up</a>
                    </p>
                    <!-- <button type="button" class="btn btn-primary" @click="signUp">Sign Up</button> -->
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
                url: 'http://localhost:1500/login',
                email: this.email,
                password: this.password,
                purpose: 'login',
                headers: {
                    'Content-Type': 'application/json'
                }
            }

            await axios.post('http://localhost:5000/login', options).then((res) => {
                if (res.data.status === 'success') {
                    console.log(res.data.status);

                    localStorage.setItem('email', this.email);
                    localStorage.setItem('role', res.data.role);
                    localStorage.setItem('name',res.data.fullname);
                    
                    // if the user doesn't have a profile, direct them to the profile page
                    if (res.data.fullname === null) {
                        router.push('/profile-page');
                    } else {
                        //get the role and detemine the page to direct the user to the right page
                        if (res.data.role === 'admin') {
                            router.push('/admin-home-page');
                        } else if (res.data.role === 'caregiver') {
                            router.push('/caregiver-home-page');
                        } else if (res.data.role === 'manager') {
                            router.push('/manager-home-page');
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