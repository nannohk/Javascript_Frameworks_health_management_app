<template>
    <div class="my-3 col-md-6 offset-md-8">
        <button type="button" class="btn btn-primary" @click="Profile">Profile</button>
        <button style="margin-left:1%" class="btn btn-primary" @click="addPatient">Add Patient</button>
        <button style="margin-left:1%" class="btn btn-primary" @click="SignOut">Sign Out</button>
    </div>

   
    <table class="table mt-4 align-middle mb-0 bg-white" style="border:black">
        <thead class="bg-light">
            <tr>
                <th scope="col"></th>
                <th scope="col">Full Name</th>
                <th scope="col">Gender</th>
                <th scope="col">Email</th>
                <th scope="col">Address</th>
                <th scope="col">Phone Number</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="user in users" :key="user.caregiverEmail">
                <td>
                    <div class="align-items-center">
                        <img :src=getImgUrl(user) alt="" style="width: 80px; height: 80px"
                            class="rounded-circle" />
                    </div>
                </td>
                <td>

                    <p class="fw-normal mb-1">{{ user.fullname }}</p>
                </td>
                <td>
                    <p class="fw-normal mb-1">{{ user.gender }}</p>
                </td>
                <td>
                    <p class="fw-normal mb-1">{{ user.email }}</p>
                </td>
                <td>
                    <p class="fw-normal mb-1">{{ user.address }}</p>
                </td>
                <td>
                    <p class="fw-normal mb-1">{{ user.phoneNumber }}</p>
                </td>
              
            </tr>
        </tbody>
    </table>


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
        getImgUrl(person) {
            if (person.profileImage == null) {

                return 'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y'
                // return '../assets/whiteBackground.png'
            }
            return ('data:image/png;base64,' + person.profileImage);
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

        async getMyPatients() {

            const profile = {
                method: 'post',
                email: localStorage.getItem('email'),
                url: 'http://localhost:5000/',
                purpose: 'getClientData',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            await axios.post('http://localhost:5000/getMyPatients', profile).then((res) => {
                if (res.data.status === 'success') {
                    var list = res.data.list;
                    this.users = list;
                    console.log(this.users);
                    localStorage.setItem('name', this.users.list.fullname);
                    this.imgUrl = 'data:image/png;base64,' + res.data.list.profileImage;
                } else {
                    console.log(res.data.status);
                }
            }).catch((err) => {
                console.log(err);
            })

        },
        // async getPatientData() {

        //     const profile = {
        //         method: 'post',
        //         url: 'http://localhost:5000/',
        //         headers: {
        //             'Content-Type': 'application/json'
        //         }
        //     }
        //     await axios.post('http://localhost:5000/getPatientList', profile).then((res) => {
        //         if (res.data.status === 'success') {
        //             console.log(res.data);
        //             // this.users = res.data.list;
        //         } else {
        //             console.log(res.data.status);
        //         }
        //     }).catch((err) => {
        //         console.log(err);
        //     })

        // }

    },
    mounted: function () {
        this.getMyPatients();
    }
}

</script>