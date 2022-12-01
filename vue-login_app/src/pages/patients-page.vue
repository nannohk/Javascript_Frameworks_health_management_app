<template>
    <div class="row">
        <div class="col-md-6 offse-md-3">
            <button class="btn btn-primary" @click="SignOut">Sign Out</button> 
        </div>
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
                <th scope="col">License</th>
                <th scope="col">Role</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="user in users" :key="user.email">
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
                <td v-if="user.license == 1">
                    <p class="fw-normal mb-1">Yes</p>
                </td>
                <td v-else>
                    <p class="fw-normal mb-1">No</p>
                </td>
                <td>
                    <p class="fw-normal mb-1">{{ user.role }}</p>
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
            users: []
        }
    },
    methods: {
        getImgUrl(person) {
            if (person.profileImage == null) {

                return 'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y'
            }
            return ('data:image/png;base64,' + person.profileImage);
        },
        SignOut() {
            localStorage.clear();
            router.push('./login-page');
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
        this.getPatientData();
    }
}

</script>