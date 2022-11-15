<template>
    <h1> home</h1>
    <div class="my-3">
                    <button type="button" class="btn btn-primary" @click="Profile">Profile</button>
                </div>
    <!-- <div>
        <img class="h-24 w-24 round-full object-cover" src="{{this.imgUrl}}"/>
    </div> -->
    <table class="table table-striped mt-4">
        <thead>
            <tr>
                <th scope="col">Full Name</th>
                <th scope="col">Gender</th>
                <th scope="col">Email</th>
                <th scope="col">Address</th>
                <th scope="col">License</th>
                <th scope="col">Role</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="user in users" :key="user.email">
                <td>{{ user.fullname }}</td>
                <td>{{ user.gender }}</td>
                <td>{{ user.email }}</td>
                <td>{{ user.address }}</td>
                <td v-if="user.license == 1">yes</td>
                <td v-else>no</td>
                <td>{{ user.role }}</td>
            </tr>

        </tbody>
    </table>

    <div class="row">
        <div class="col-md-6 offse-md-3">
            <h1>Sign Out!</h1>
            <button class="btn btn-primary" @click="SignOut">Sign Out</button>
        </div>
    </div>
</template>

<script>
import router from '@/router';
import axios from 'axios';
export default {
    data() {
        return {
            users: [],
            profileImage:null,
            imgUrl:'',
        }
    },
    methods: {
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
                url: 'http://localhost:1500/',
                purpose: 'getClientData',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            await axios.post('http://localhost:1500/', profile).then((res) => {
                if (res.data.status === 'success') {
                    this.users = res.data.list;
                    this.profileImage = res.data.list[0].profileImage;
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