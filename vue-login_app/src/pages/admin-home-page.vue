<template>
    <div class="row">
        <div class="col-md-6 offse-md-3">
            <h1>Sign Out!</h1>
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
        <!-- <tbody class="d-flex align-items-center">
            <tr v-for="user in users" :key="user.email">
                <td>{{ user.fullname }}</td>
                <td>{{ user.gender }}</td>
                <td>{{ user.email }}</td>
                <td>{{ user.address }}</td>
                <td v-if="user.license == 1">yes</td>
                <td v-else>no</td>
                <td>{{ user.role }}</td>
            </tr>

        </tbody> -->
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
                // return '../assets/whiteBackground.png'
            }
            return ('data:image/png;base64,' + person.profileImage);
        },
        SignOut() {
            localStorage.clear();
            router.push('./login-page');
        }
        ,

        async getAdminData() {

            const profile = {
                method: 'post',
                url: 'http://localhost:5000/',
                purpose: 'getAdminList',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            await axios.post('http://localhost:5000/getAdminList', profile).then((res) => {
                if (res.data.status === 'success') {
                    console.log(res.data.list);
                    this.users = res.data.list;
                } else {
                    console.log(res.data.status);
                }
            }).catch((err) => {
                console.log(err);
            })

        }
    },
    mounted: function () {
        this.getAdminData();
    }
}

</script>