<template>
    <div class="row container py-5 h-100 d-flex justify-content-center align-items-center">
        <div class="col-md-4 shadow card text-black">
            <div class="mb-md-5 mt-md-4 pb-5 align-items-center">
                <div>
                    <h3 class="text-center fw-bold mb-2 text-uppercase" style="color: #0D6EFD;">Sign Up</h3>
                    <hr />
                </div>
                <form @submit.prevent="signUp">
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

                    <!-- <div class="col-8 form-group">
                        <label style="color: #0D6EFD;">Role</label>
                        <select class="form-control" v-model="role">
                            <option value="manager">Manager</option>
                            <option value="caregiver">Caregiver</option>
                        </select>
                    </div> -->

                    <div class="text-center my-3">
                        <button type="submit" class="btn-primary btn btn-outline-white btn-lg px-5">Sign Up</button>
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
            role: '',
            errMail: '',
            errPass: '',
        }
    },

    methods: {
        async signUp() {
            const options = {
                method: 'post',
                url: 'http://localhost:5000/signUp',
                email: this.email,
                password: this.password,
                role: 'caregiver',
                purpose: 'signup',
                headers: {
                    'Content-Type': 'application/json'
                }
            }

            await axios.post('http://localhost:5000/signUp', options).then((res) => {
                if (res.data.message === 'user created') {
                    console.log(res.data.message);
                    localStorage.setItem('email', this.email);
                    localStorage.setItem('role', this.role);
                    router.push('/login-page');
                } else {
                    console.log(res.data.message);
                }
            }).catch((err) => {
                console.log(err);
            })

        }
    }

}
</script>