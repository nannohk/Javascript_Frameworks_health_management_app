<template>
    <div class="container py-5 justify-content-center align-items-center">
        <div class="text-center">
            <h1>Patient Information</h1>
            <hr />
        </div>

        <div class="card">
            <MDBAccordion v-model="activeItem" stayOpen>
                <MDBAccordionItem headerTitle="Patient Information" collapseId="patient">
                    <form class="row container h-100  justify-content-center align-items-center">
                        <div class="row">
                            <div class="col">
                                <label class="col-form-label">Full Name</label>
                                <input type="text" class="form-control" placeholder="Full Name">
                            </div>
                            <div class="col">
                                <label class="col-form-label">Gender</label>
                                <select class="form-control" v-model="gender">
                                    <option value="male">Male</option>
                                    <option value="female">Female</option>
                                    <option value="other">Other</option>
                                </select>
                            </div>
                            <div class="form-group col">
                                <label class="col-form-label">Date of Birth</label>
                                <input type="text" class="form-control" placeholder="Date of Birth (YYYY-MM-DD)">
                            </div>
                        </div>
                        <div class="row">
                            <div class="form-group col">
                                <label class="col-form-label">Address</label>
                                <input type="text" class="form-control" placeholder="211B Baker Street London, England">
                            </div>
                            <div class="form-group col">
                                <label class="col-form-label">Phone Number</label>
                                <input type="text" class="form-control" placeholder="506 555 5555">
                            </div>
                        </div>
                        <div class="row">
                            <div class="form-group col">
                                <label class="col-form-label">Employer</label>
                                <input type="text" class="form-control" placeholder="UNB">
                            </div>
                            <div class="form-group col">
                                <label class="col-form-label">Employer Address</label>
                                <input type="text" class="form-control" placeholder="100 Tucker Park Road">
                            </div>
                            <div class="form-group col">
                                <label class="col-form-label">Position</label>
                                <input type="text" class="form-control" placeholder="Professor">
                            </div>
                        </div>
                    </form>
                </MDBAccordionItem>

                <MDBAccordionItem headerTitle="Emergency Contact Information" collapseId="emergency">
                    <form class="row container h-100  justify-content-center align-items-center">
                        <div class="row">
                            <div class="col-8">
                                <label class="col-form-label">Insurance Company</label>
                                <input type="text" class="form-control" placeholder="Insurance Company Name">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-2">
                                <label class="col-form-label">Policy Number</label>
                                <input type="text" class="form-control" placeholder="86464 687815 89846">
                            </div>
                            <div class="col-2">
                                <label class="col-form-label">Group Number</label>
                                <input type="text" class="form-control" placeholder="1738 5494">
                            </div>
                        </div>
                        <div class="row">
                            <div class="form-group col-7">
                                <label class="col-form-label">Insured Party</label>
                                <input type="text" class="form-control" placeholder="Insured Party">
                            </div>
                            <div class="form-group col-3">
                                <label class="col-form-label">Relationship</label>
                                <input type="text" class="form-control" placeholder="Brother/Sister/...">
                            </div>
                        </div>
                    </form>
                </MDBAccordionItem>
                <MDBAccordionItem headerTitle="Insurance" collapseId="insurance">
                    <form class="row container h-100  justify-content-center align-items-center">
                        <div class="row">
                            <div class="col">
                                <label class="col-form-label">Insurance Company</label>
                                <input type="text" class="form-control" placeholder="Insurance Company Name">
                            </div>
                            <div class="form-group col">
                                <label class="col-form-label">Insured Party</label>
                                <input type="text" class="form-control" placeholder="Insured Party">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <label class="col-form-label">Policy Number</label>
                                <input type="text" class="form-control" placeholder="86464 687815 89846">
                            </div>
                            <div class="col">
                                <label class="col-form-label">Group Number</label>
                                <input type="text" class="form-control" placeholder="1738 5494">
                            </div>
                            <div class="form-group col">
                                <label class="col-form-label">Relationship</label>
                                <input type="text" class="form-control" placeholder="Brother/Sister/...">
                            </div>
                        </div>


                    </form>
                </MDBAccordionItem>
            </MDBAccordion>
        </div>
    </div>
</template>

<script>
import router from '@/router';
import axios from 'axios';
import { MDBAccordion, MDBAccordionItem } from "mdb-vue-ui-kit";
import { ref } from "vue";

export default {
    components: {
        MDBAccordion,
        MDBAccordionItem
    },

    data() {
        return {
            users: [],
            activeItem: ref('patient')
        }
    },
    methods: {
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