<template>
    <form @submit.prevent="submitIMG" enctype="multipart/form-data" class="section form-group mt-5 shadow col-md-5 ">
        <div class="row container">
            <div class="col-form-label col-form-label-lg">
                   <label for="imageUpload">Upload File</label>
                <img src='../assets/test@gmail.com.png' alt="" style="width: 80px; height: 80px"
                    class="rounded-circle" />
                    <input class="small" type='file' accept=".png, .jpg, .jpeg"
                @change="onFileSelected" />
            </div>
         
  
        </div>
        <div class="field">
            <button class="btn btn-primary col-3" @click="submitIMG"> Upload Image</button>
        </div>
    </form>

    <br />
    <div class="row container py-5 h-100 d-flex justify-content-center align-items-center">
        <div class="row col-md-8 form-group ">
            <div>
                <h3>Profile</h3>
                <hr />
            </div>
        </div>
        <div class="col-8 form-group">
            <label class="col-form-label col-form-label-lg">Full Name</label>
            <input type="text" class="form-control form-control-lg" placeholder="Enter full name" v-model="fullName" />
        </div>
        <div class="col-8 form-group">
            <label class="col-form-label col-form-label-lg">Address</label>
            <input type="text" class="form-control form-control-lg" placeholder="Enter address" v-model="address" />
        </div>
        <div class="col-8 form-group">
            <label class="col-form-label col-form-label-lg">What is your gender?</label>
            <select class="form-control" v-model="gender">
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
            </select>
        </div>
        <div class="col-8 form-group">
            <label class="col-form-label col-form-label-lg">Do you have a driver's license?</label>
            <input class="form-check-input mt-3" type="checkbox" v-model="license">
        </div>


        <div class="col-8 form-group text-center">
            <button class="btn btn-primary btn-md col-4" @click="submitProfile">Submit</button>
        </div>
    </div>
</template>

<script>
import router from '@/router';
import axios from 'axios';

export default {
    methods: {
        onFileSelected(event) {
            this.selectedFile = event.target.files[0];
        },

        async submitIMG() {
            const formData = new FormData();
            formData.append('file', this.selectedFile);
            formData.append('headers', {
                'Content-Type': 'multipart/form-data',
            });

            formData.append('newFileName', localStorage.getItem('email'));
            try {
                await axios.post('http://localhost:5000/profileUpload', formData);
            } catch (error) {
                console.log(error);
            }
        },

        async submitProfile() {
            const email = localStorage.getItem('email');
            const profile = {
                method: 'post',
                url: 'http://localhost:5000/',
                email: email,
                fullName: this.fullName,
                address: this.address, gender: this.gender,
                license: this.license,
                purpose: 'profileUpdate',
                headers: {
                    'Content-Type': 'application/json, multipart/form-data'
                }
            }

            await axios.post('http://localhost:5000/updateProfile', profile).then((res) => {
                if (res.data.status === 'success') {
                    console.log(res.data.status);
                    //get the role and detemine the page to direct the user to
                    const role = localStorage.getItem('role');
                    if (role === 'admin') {
                        router.push('/admin-home-page');

                    } else {
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
            selectedFile: "",
            message: ''
        }
    }
}
</script>