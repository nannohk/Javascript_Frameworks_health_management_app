<template>
    <div class="row col-md-8 form-group shadow align-items-center">
        <div>
            <h3>Profile</h3>
            <hr />
        </div>
        <div class="avatar-upload">
            <div class="avatar-edit">
                <input type='file' id="imageUpload" accept=".png, .jpg, .jpeg" />
                <label for="imageUpload"></label>
            </div>
            <div class="avatar-preview">
                <div id="imagePreview" style="background-image: url(https://i.imgur.com/8kLWJjA.png);">
                </div>
            </div>
        </div>
        <div class="col-12 form-group">
            <label class="col-form-label col-form-label-lg">Full Name</label>
            <input type="text" class="form-control form-control-lg" placeholder="Enter full name" v-model="fullName" />
        </div>
        <div class="col-12 form-group">
            <label class="col-form-label col-form-label-lg">Address</label>
            <input type="text" class="form-control form-control-lg" placeholder="Enter address" v-model="address" />
        </div>
        <div class="col-12 form-group">
            <label class="col-form-label col-form-label-lg">What is your gender?</label>
            <select class="form-control" v-model="gender">
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
            </select>
        </div>
        <div class="col-12 form-group">
            <label class="col-form-label col-form-label-lg">Do you have a driver's license?</label>
            <input class="form-check-input mt-3" type="checkbox" v-model="license">
        </div>


        <div class="col-12 form-group text-center">
            <button class="btn btn-primary btn-md col-4" @click="submitProfile">Submit</button>
        </div>
    </div>
</template>

<script>
import router from '@/router';
import axios from 'axios';
// import email  from '@/pages/Login-page';

export default {
    methods: {
        async submitProfile() {
            const email = localStorage.getItem('email');
            const profile = {
                method: 'post',
                url: 'http://localhost:1500/',
                email: email,
                fullName: this.fullName,
                address: this.address, gender: this.gender,
                license: this.license,
                purpose: 'profileUpdate',
                headers: {
                    'Content-Type': 'application/json'
                }
            }

            await axios.post('http://localhost:1500/', profile).then((res) => {
                if (res.data.status === 'success') {
                    console.log(res.data.status);
                    //get the role and detemine the page to direct the user to
                    const role = localStorage.getItem('role');
                    if (role === 'admin') {
                        router.push('/admin-home-page');
                    } else  {
                        router.push('/client-home-page');
                    }
                } else {
                    console.log(res.data.status);
                }
            }).catch((err) => {
                console.log(err);
            })


        }
    },

    data() {
        return {
            fullName: '',
            address: '',
            license: false,
            gender: '',
        }
    }
}
</script>