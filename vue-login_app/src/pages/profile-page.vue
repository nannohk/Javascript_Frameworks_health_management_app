<template>
        <div class="row mt-3">
        <div class="col-md-6 offset-md-8">
            <button class="btn btn-primary"  @click="Home">Home</button>
            <button class="btn btn-primary" @click="SignOut" style="margin-left:1%">Sign Out</button> 
        </div>
    </div>

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
            <label class="col-form-label col-form-label-lg">Phone Number</label>
            <input type="phone" class="form-control form-control-lg" placeholder="555 555 5555" v-model="phoneNumber" />
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

    <div class="row container py-5 h-100 d-flex justify-content-center align-items-center">
        <form @submit.prevent="submitIMG" enctype="multipart/form-data"
            class="section form-group mt-3 shadow col-md-5 ">
            <div class="row container">
                <div class="col-form-label col-form-label-lg">
                    <label for="imageUpload">Upload File</label>
                    <input class="small" type='file' accept=".png, .jpg, .jpeg" @change="onFileSelected" />
                </div>
            </div>
            <div class="field">
                <button class="btn btn-primary col-3" @click="submitIMG"> Upload Image</button>
            </div>
        </form>
    </div>

</template>

<script>
import router from '@/router';
import axios from 'axios';

export default {
    methods: {
        SignOut() {
            localStorage.clear();
            router.push('./login-page');
        },
        Home() {
            if (localStorage.getItem('role') == 'admin') {
                router.push('./admin-home-page');
            } else if (localStorage.getItem('role') == 'manager') {
                router.push('./manager-home-page');
            } else if (localStorage.getItem('role') == 'caregiver') {
                router.push('./caregiver-home-page');
            }
        }
        ,

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
                phoneNumber: this.phoneNumber,
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
                    } else if (role === 'caregiver') {
                        router.push('/caregiver-home-page');
                    } else if (role === 'manager') {
                        router.push('/manager-home-page');
                    }

                } else {
                    console.log(res.data.status);
                }
            }).catch((err) => {
                console.log(err);
            })


        },
        async getClientData() {

            const profile = {
                method: 'post',
                email: localStorage.getItem('email'),
                url: 'http://localhost:5000/',
                purpose: 'getClientData',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            await axios.post('http://localhost:5000/getClientData', profile).then((res) => {
                if (res.data.status === 'success') {
                    var list = res.data.list;
                    this.user = { list };
                    this.fullName = list.fullname;
                    this.address = list.address;
                    this.license = list.license;
                    this.phoneNumber = list.phoneNumber;
                    this.gender = list.gender;
                    this.imgUrl = 'data:image/png;base64,' + res.data.list.profileImage;
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
            phoneNumber: '000 000 000',
            gender: '',
            selectedFile: "",
            message: '',
            user: {},
            imgUrl: '',
        }
    },

    mounted: function () {
        this.getClientData();
    }
}
</script>