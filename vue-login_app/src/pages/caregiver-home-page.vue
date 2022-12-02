<template>
    <div class="my-3 col-md-6 offse-md-3">
        <button type="button" class="btn btn-primary" @click="Profile">Profile</button>

        <button style="margin-left:10%" class="btn btn-primary" @click="addPatient">Add Patient</button>

        <button class="btn btn-primary" style="margin-left:10%"  @click="viewPatients">My Patients</button>

        <button style="margin-left:10%" class="btn btn-primary" @click="SignOut">Sign Out</button>


    </div>

    <div class="row container py-5  d-flex justify-content-center align-items-center shadow col-md-8">

        <div class="row col-md-8 form-group">
            <div>
                <h3>Profile <img v-bind:src="this.imgUrl" alt="" style="margin-left: 20%; height: 100px"
                        class="rounded-circle" /></h3>
                <hr />
            </div>
        </div>

        <div v-for="user in users" :key="user.email" class="row col-md-8 form-group ">
            <div class="col-8 form-group ">
                <label class="col-form-label col-form-label-lg">Full Name</label>
                <input type="text" class="form-control form-control-lg" placeholder="Enter full name"
                    :value="user.fullname" />
            </div>
            <div class="col-8 form-group">
                <label class="col-form-label col-form-label-lg">Email</label>
                <input type="text" class="form-control form-control-lg" placeholder="Enter full name"
                    :value="user.email" />
            </div>
            <div class="col-8 form-group">
                <label class="col-form-label col-form-label-lg">Address</label>
                <input type="text" class="form-control form-control-lg" placeholder="Enter full name"
                    :value="user.address" />
            </div>
            <div class="col-8 form-group">
                <label class="col-form-label col-form-label-lg">Gender</label>
                <input type="text" class="form-control form-control-lg" placeholder="Enter full name"
                    :value="user.gender" />
            </div>
            <div class="col-8 form-group">
                <label class="col-form-label col-form-label-lg">Do you have a driver's license?</label>
                <input class="form-check-input mt-3" type="checkbox" :checked="user.license" />
            </div>
            <div class="col-8 form-group">
                <label class="col-form-label col-form-label-lg">Role</label>
                <input type="text" class="form-control form-control-lg" placeholder="Enter full name"
                    :value="user.role" />
            </div>
        </div>
    </div>


</template>

<script>
import router from '@/router';
import axios from 'axios';

export default {
    data() {
        return {
            users: {},
            imgUrl: '',
        }
    },
    methods: {
        viewPatients() {
            router.push('./patients-page');
        },
        
        addPatient() {
            router.push('/patientForm-page');
        },
        Profile() {
            router.push('/profile-page');
        },

        SignOut() {
            localStorage.clear();
            router.push('./login-page');
        }
        ,

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
                    this.users = { list };
                    localStorage.setItem('name', this.users.list.fullname);
                    this.imgUrl = 'data:image/png;base64,' + res.data.list.profileImage;
                } else {
                    console.log(res.data.status);
                }
            }).catch((err) => {
                console.log(err);
            })

        },
        async getPatientData() {

            const profile = {
                method: 'post',
                url: 'http://localhost:5000/',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            await axios.post('http://localhost:5000/getPatientList', profile).then((res) => {
                if (res.data.status === 'success') {
                    console.log(res.data);
                    // this.users = res.data.list;
                } else {
                    console.log(res.data.status);
                }
            }).catch((err) => {
                console.log(err);
            })

        }

    },
    mounted: function () {
        this.getClientData();
    }
}

</script>